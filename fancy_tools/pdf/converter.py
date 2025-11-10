#!/usr/bin/env python3
"""
PDF conversion tools.

This module provides functionality to convert text and Markdown files to PDF format.
"""

import os
import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console


console = Console()


def convert_to_pdf(input_file: Path, output_file: Path) -> None:
    """
    Convert a .txt or .md file to PDF.

    Args:
        input_file: Path to the input file (.txt or .md).
        output_file: Path to the output PDF file.

    Raises:
        ValueError: If file extension is not supported.
        FileNotFoundError: If input file doesn't exist.
    """
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    file_extension = input_file.suffix.lower()

    if file_extension == '.txt':
        convert_txt_to_pdf(input_file, output_file)
    elif file_extension == '.md':
        convert_md_to_pdf(input_file, output_file)
    else:
        raise ValueError(
            f"Unsupported file extension '{file_extension}'. "
            "Only .txt and .md are supported."
        )

    console.print(
        f"[green]✓[/green] Successfully converted '{input_file}' to '{output_file}'",
        style="bold"
    )


def convert_txt_to_pdf(input_file: Path, output_file: Path) -> None:
    """
    Convert a text file to PDF using fpdf2.

    Creates a simple PDF with Arial font at 12pt size. Each line from the text
    file is rendered as a multi-cell paragraph in the PDF.

    Args:
        input_file: Path to the input text file.
        output_file: Path to the output PDF file.

    Raises:
        ImportError: If fpdf2 library is not installed.
    """
    try:
        from fpdf import FPDF
    except ImportError:
        console.print(
            "[red]Error:[/red] fpdf2 is not installed. "
            "Install it with: pip install fpdf2",
            style="bold"
        )
        raise

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            pdf.multi_cell(0, 10, txt=line)

    pdf.output(str(output_file))


def convert_md_to_pdf(input_file: Path, output_file: Path) -> None:
    """
    Convert a Markdown file to PDF using markdown-pdf.

    Preserves Markdown formatting including headers, lists, code blocks, and
    other Markdown elements in the generated PDF document.

    Args:
        input_file: Path to the input Markdown file.
        output_file: Path to the output PDF file.

    Raises:
        ImportError: If markdown-pdf library is not installed.
    """
    try:
        from markdown_pdf import Section, MarkdownPdf
    except ImportError:
        console.print(
            "[red]Error:[/red] markdown-pdf is not installed. "
            "Install it with: pip install markdown-pdf",
            style="bold"
        )
        raise

    pdf = MarkdownPdf()

    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    pdf.add_section(Section(markdown_content))
    pdf.save(str(output_file))


@click.command()
@click.argument(
    'input_file',
    type=click.Path(exists=True, path_type=Path)
)
@click.option(
    '-o', '--output',
    type=click.Path(path_type=Path),
    help='Output PDF file path. Default: <input_file>.pdf'
)
def pdf_convert(input_file: Path, output: Optional[Path]) -> None:
    """
    Convert text or Markdown files to PDF.

    This command-line tool converts plain text (.txt) or Markdown (.md) files
    to PDF format. If no output path is specified, the PDF is saved with the
    same name as the input file but with a .pdf extension.

    Args:
        input_file: Path to the input file (.txt or .md).
        output: Optional output PDF file path (default: <input_file>.pdf).

    Raises:
        click.Abort: If the file format is unsupported or conversion fails.

    Examples:
        pocket pdf convert document.txt
        pocket pdf convert README.md -o output.pdf
        conv-to-pdf document.md output.pdf
    """
    # Determine output path
    if output is None:
        output = input_file.with_suffix('.pdf')

    # Validate output extension
    if output.suffix.lower() != '.pdf':
        console.print(
            "[red]Error:[/red] Output file must have .pdf extension.",
            style="bold"
        )
        raise click.Abort()

    try:
        convert_to_pdf(input_file, output)
    except FileNotFoundError as e:
        console.print(f"[red]Error:[/red] {e}", style="bold")
        raise click.Abort()
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}", style="bold")
        raise click.Abort()
    except ImportError:
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}", style="bold")
        raise click.Abort()


def main():
    """Main entry point for standalone script."""
    pdf_convert()


if __name__ == "__main__":
    main()
