#!/usr/bin/env python3
"""
Markdown renderer using Rich library.

This module provides functionality to read and render Markdown files
beautifully in the terminal using the Rich library for enhanced formatting
and syntax highlighting.

Combines functionality from both fancy_md.py and markd.py.
"""

from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.markdown import Markdown
from rich import errors


def read_markdown_file(file_path: Path) -> str:
    """
    Read the contents of a Markdown file.

    Args:
        file_path: Path to the Markdown file to read.

    Returns:
        The file contents as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the path is not a file.
        PermissionError: If the file cannot be read.
        IOError: If there's an error reading the file.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    try:
        return file_path.read_text(encoding='utf-8')
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot read {file_path}")
    except Exception as e:
        raise IOError(f"Error reading file {file_path}: {e}")


def render_markdown(content: str, console: Optional[Console] = None) -> None:
    """
    Render Markdown content to the terminal using Rich.

    Args:
        content: The Markdown content to render.
        console: Optional Console instance. If not provided, a new one is created.

    Raises:
        errors.MarkdownError: If there's an error rendering the markdown.
    """
    if console is None:
        console = Console()

    try:
        md = Markdown(content)
        console.print(md)
    except errors.MarkdownError as e:
        console.print(f"[red]Error rendering Markdown:[/red] {e}", style="bold")
        raise


@click.command()
@click.argument(
    'file_arg',
    type=click.Path(exists=True, path_type=Path),
    required=False
)
@click.option(
    '-f', '--file',
    type=click.Path(exists=True, path_type=Path),
    help='Path to the Markdown file to render.'
)
@click.option(
    '-o', '--output',
    type=click.Path(path_type=Path),
    help='Alternative option for input file path (for backward compatibility).'
)
@click.option(
    '-i', '--input',
    type=click.Path(path_type=Path),
    help='Alternative option for input file path.'
)
def markd(file_arg: Optional[Path], file: Optional[Path], output: Optional[Path], input: Optional[Path]) -> None:
    """
    Render Markdown files beautifully in the terminal using Rich.

    This command-line tool reads a Markdown file and displays it with enhanced
    formatting, syntax highlighting, and beautiful terminal rendering using the
    Rich library. Supports multiple input methods for flexibility.

    Args:
        file_arg: Positional argument for the file path (preferred method).
        file: File path specified via -f/--file option.
        output: File path via -o/--output option (legacy compatibility).
        input: File path via -i/--input option (legacy compatibility).

    Note:
        Priority order: file_arg > file > output > input.
        If no file is specified, the user will be prompted interactively.

    Examples:
        markd README.md
        markd -f README.md
        markd --file documentation.md
        markd -o guide.md
        markd -i ./docs/guide.md
    """
    console = Console()

    # Determine which file path to use (priority: argument > file > output > input)
    file_path = file_arg or file or output or input

    # If no file specified, prompt the user
    if file_path is None:
        file_path_str = click.prompt('Enter the path to the Markdown file', type=str)
        file_path = Path(file_path_str)

    try:
        # Read the Markdown file
        content = read_markdown_file(file_path)

        # Render the Markdown
        render_markdown(content, console)

    except FileNotFoundError as e:
        console.print(f"[red]Error:[/red] {e}", style="bold")
        raise click.Abort()
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}", style="bold")
        raise click.Abort()
    except PermissionError as e:
        console.print(f"[red]Error:[/red] {e}", style="bold")
        raise click.Abort()
    except IOError as e:
        console.print(f"[red]Error:[/red] {e}", style="bold")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}", style="bold")
        raise click.Abort()


if __name__ == '__main__':
    markd()
