#!/usr/bin/env python3
"""
Fancy Tools - Unified CLI entry point.

This module provides a unified command-line interface for all Fancy Tools
functionality, organized into logical subcommands.
"""

import click
from rich.console import Console

from pocket import __version__

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="pocket")
def cli():
    """
    Pocket - A collection of developer productivity tools.

    Available commands:
    - markdown: Render markdown files in terminal
    - project: Project management tools (export to file, etc.)
    - templates: Manage agent templates and cheatsheets
    - pdf: PDF conversion tools (coming soon)
    - web: Web utilities (coming soon)

    Examples:
        pocket markdown render README.md
        pocket project to-file . -o project.md
        pocket templates list
    """
    pass


# ==================== Markdown Commands ====================
@cli.group(name="markdown")
def markdown_group():
    """Markdown rendering and conversion tools."""
    pass


@markdown_group.command(name="render")
@click.argument('file', type=click.Path(exists=True))
@click.option('--width', '-w', type=int, help='Output width in characters.')
def markdown_render(file: str, width: int):
    """
    Render a Markdown file beautifully in the terminal.

    This command reads a Markdown file and displays it with enhanced formatting,
    syntax highlighting, and beautiful terminal rendering using the Rich library.

    Args:
        file: Path to the Markdown file to render.
        width: Optional output width in characters for wrapping.

    Examples:
        pocket markdown render README.md
        pocket markdown render docs/guide.md -w 100
    """
    from pocket.markdown.renderer import markd
    from pathlib import Path

    # Call the markd function with the file
    ctx = click.Context(markd)
    ctx.invoke(markd, file=Path(file), output=None, input=None)


# ==================== Project Commands ====================
@cli.group(name="project")
def project_group():
    """Project management and export tools."""
    pass


@project_group.command(name="to-file")
@click.option(
    '-p', '--path',
    default='.',
    help='Root directory of the project to scan.'
)
@click.option(
    '-o', '--output',
    default=None,
    help='Output Markdown file name.'
)
@click.option(
    '-e', '--exclude',
    default="env,.env,venv,.venv,.gitignore,.git,.vscode,.idea,.cursor,lib,bin,site-packages,node_modules,__pycache__,.DS_Store",
    help='Comma-separated list of files/directories to exclude.'
)
def project_to_file(path: str, output: str, exclude: str):
    """
    Export entire project to a single Markdown file.

    This command scans a project directory and generates a single Markdown
    file containing the file tree structure and all source code with syntax
    highlighting. Useful for documentation, code reviews, or AI analysis.

    Args:
        path: Root directory of the project to scan (default: current directory).
        output: Name of the output Markdown file (default: <project_name>-1-file.md).
        exclude: Comma-separated list of files/directories to exclude from export.

    Examples:
        pocket project to-file
        pocket project to-file -p ./my-project -o export.md
        pocket project to-file -e "node_modules,dist,build"
    """
    from pocket.project.to_file import create_codebase_markdown

    create_codebase_markdown(path, output, exclude)


# ==================== Templates Commands ====================
@cli.group(name="templates")
def templates_group():
    """Manage agent templates and development cheatsheets."""
    pass


@templates_group.command(name="list")
@click.option(
    '--type', '-t',
    type=click.Choice(['templates', 'cheatsheets', 'all'], case_sensitive=False),
    default='all',
    help='Type of items to list.'
)
def templates_list(type: str):
    """
    List available templates and cheatsheets.

    Displays a formatted table showing all available templates and/or cheatsheets
    with their names and descriptions.

    Args:
        type: Filter by type - 'templates', 'cheatsheets', or 'all' (default: all).

    Examples:
        pocket templates list
        pocket templates list --type templates
        pocket templates list -t cheatsheets
    """
    from pocket.templates_and_cheatsheets.cli import list_items

    ctx = click.Context(list_items)
    ctx.invoke(list_items, type=type)


@templates_group.command(name="view")
@click.argument('name', type=str)
@click.option(
    '--type', '-t',
    type=click.Choice(['template', 'cheatsheet'], case_sensitive=False),
    help='Type of item to view.'
)
def templates_view(name: str, type: str):
    """
    View a template or cheatsheet in the terminal.

    Renders the template or cheatsheet content with Markdown formatting
    directly in the terminal for quick reference.

    Args:
        name: Name of the template or cheatsheet (without .md extension).
        type: Type of item to view - 'template' or 'cheatsheet' (auto-detected if omitted).

    Examples:
        pocket templates view unit_tests_agent
        pocket templates view SQL -t cheatsheet
    """
    from pocket.templates_and_cheatsheets.cli import view_item

    ctx = click.Context(view_item)
    ctx.invoke(view_item, name=name, type=type)


@templates_group.command(name="copy")
@click.argument('name', type=str)
@click.option(
    '--output', '-o',
    type=click.Path(),
    help='Output path for the copied file.'
)
@click.option(
    '--type', '-t',
    type=click.Choice(['template', 'cheatsheet'], case_sensitive=False),
    help='Type of item to copy.'
)
@click.option(
    '--force', '-f',
    is_flag=True,
    help='Overwrite existing file.'
)
def templates_copy(name: str, output: str, type: str, force: bool):
    """
    Copy a template or cheatsheet to your project.

    Copies the specified template or cheatsheet file to a destination in your
    project. Creates parent directories if they don't exist.

    Args:
        name: Name of the template or cheatsheet (without .md extension).
        output: Output path (file or directory) for the copied file.
        type: Type of item to copy - 'template' or 'cheatsheet' (auto-detected if omitted).
        force: If True, overwrite existing file without confirmation.

    Examples:
        pocket templates copy unit_tests_agent -o .agents/
        pocket templates copy SQL -o docs/cheatsheets/
    """
    from pocket.templates_and_cheatsheets.cli import copy_item
    from pathlib import Path

    output_path = Path(output) if output else None

    ctx = click.Context(copy_item)
    ctx.invoke(copy_item, name=name, output=output_path, type=type, force=force)


@templates_group.command(name="init")
@click.option(
    '--output', '-o',
    type=click.Path(),
    help='Directory for agent templates.'
)
def templates_init(output: str):
    """
    Initialize agent configuration directory with all templates.

    Creates a directory and copies all available agent templates into it.
    Useful for quickly setting up agent configurations in a new project.

    Args:
        output: Directory where agent templates will be copied (default: .AGENTS).

    Examples:
        pocket templates init
        pocket templates init -o ./agents/
    """
    from pocket.templates_and_cheatsheets.cli import init_agents
    from pathlib import Path

    output_path = Path(output) if output else Path.cwd() / ".AGENTS"

    ctx = click.Context(init_agents)
    ctx.invoke(init_agents, output=output_path)


# ==================== PDF Commands ====================
@cli.group(name="pdf")
def pdf_group():
    """PDF conversion tools."""
    pass


@pdf_group.command(name="convert")
@click.argument('input_file', type=click.Path(exists=True))
@click.option(
    '-o', '--output',
    type=click.Path(),
    help='Output PDF file path.'
)
def pdf_convert_cmd(input_file: str, output: str):
    """
    Convert text or Markdown files to PDF.

    Converts plain text (.txt) or Markdown (.md) files to PDF format.
    Output file defaults to input filename with .pdf extension.

    Args:
        input_file: Path to the input file (.txt or .md).
        output: Optional output PDF file path (default: <input_file>.pdf).

    Examples:
        pocket pdf convert document.txt
        pocket pdf convert README.md -o output.pdf
    """
    from pocket.pdf.converter import pdf_convert
    from pathlib import Path

    output_path = Path(output) if output else None

    ctx = click.Context(pdf_convert)
    ctx.invoke(pdf_convert, input_file=Path(input_file), output=output_path)


# ==================== Web Commands ====================
@cli.group(name="web")
def web_group():
    """Web utilities."""
    pass


@web_group.command(name="favicon")
@click.argument('input_file', type=click.Path(exists=True))
@click.option(
    '-o', '--output',
    type=click.Path(),
    help='Output favicon file path.'
)
@click.option(
    '--sizes',
    type=str,
    help='Custom sizes (e.g., "64x64,32x32,16x16")'
)
def web_favicon_cmd(input_file: str, output: str, sizes: str):
    """
    Convert an image to a favicon (.ico) file.

    Generates a multi-size .ico favicon file from any image format.
    Includes standard sizes for optimal browser compatibility.

    Args:
        input_file: Path to the input image file (PNG, JPG, etc.).
        output: Optional output .ico file path (default: favicon.ico).
        sizes: Custom sizes as comma-separated WxH values (e.g., "64x64,32x32").

    Examples:
        pocket web favicon logo.png
        pocket web favicon logo.png -o custom-favicon.ico
        pocket web favicon logo.png --sizes "64x64,32x32"
    """
    from pocket.web.favicon import favicon_convert
    from pathlib import Path

    output_path = Path(output) if output else None

    ctx = click.Context(favicon_convert)
    ctx.invoke(favicon_convert, input_file=Path(input_file), output=output_path, sizes=sizes)


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
