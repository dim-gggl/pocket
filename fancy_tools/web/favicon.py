#!/usr/bin/env python3
"""
Favicon generation tools.

This module provides functionality to convert images to favicon (.ico) format
with multiple sizes for web compatibility.
"""

from pathlib import Path
from typing import Optional, List, Tuple

import click
from rich.console import Console


console = Console()

# Standard favicon sizes
DEFAULT_FAVICON_SIZES: List[Tuple[int, int]] = [
    (256, 256),
    (128, 128),
    (64, 64),
    (48, 48),
    (32, 32),
    (16, 16)
]


def convert_to_favicon(
    input_file: Path,
    output_file: Path,
    sizes: Optional[List[Tuple[int, int]]] = None
) -> None:
    """
    Convert an image to a favicon (.ico) file with multiple sizes.

    Args:
        input_file: Path to the input image file.
        output_file: Path to the output .ico file.
        sizes: List of (width, height) tuples for icon sizes.
               Defaults to standard favicon sizes.

    Raises:
        FileNotFoundError: If input file doesn't exist.
        ImportError: If PIL/Pillow is not installed.
        ValueError: If output file doesn't have .ico extension.
    """
    try:
        from PIL import Image
    except ImportError:
        console.print(
            "[red]Error:[/red] Pillow is not installed. "
            "Install it with: pip install Pillow",
            style="bold"
        )
        raise

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    if output_file.suffix.lower() != '.ico':
        raise ValueError("Output file must have .ico extension")

    if sizes is None:
        sizes = DEFAULT_FAVICON_SIZES

    # Open and convert image
    img = Image.open(input_file)
    img.save(str(output_file), format="ICO", sizes=sizes)

    console.print(
        f"[green]✓[/green] Favicon saved to '{output_file}' with {len(sizes)} sizes",
        style="bold"
    )


@click.command()
@click.argument(
    'input_file',
    type=click.Path(exists=True, path_type=Path)
)
@click.option(
    '-o', '--output',
    type=click.Path(path_type=Path),
    help='Output favicon file path. Default: favicon.ico'
)
@click.option(
    '--sizes',
    type=str,
    help='Custom sizes as comma-separated WxH values (e.g., "64x64,32x32,16x16")'
)
def favicon_convert(
    input_file: Path,
    output: Optional[Path],
    sizes: Optional[str]
) -> None:
    """
    Convert an image to a favicon (.ico) file.

    This command-line tool generates a multi-size .ico favicon file from any
    image format (PNG, JPG, etc.). The favicon includes multiple sizes for
    optimal compatibility across different devices and browsers. Default sizes
    include 256x256, 128x128, 64x64, 48x48, 32x32, and 16x16 pixels.

    Args:
        input_file: Path to the input image file (PNG, JPG, etc.).
        output: Optional output .ico file path (default: favicon.ico in current directory).
        sizes: Custom sizes as comma-separated WxH values (e.g., "64x64,32x32,16x16").

    Raises:
        click.Abort: If the conversion fails or required libraries are missing.

    Examples:
        pocket web favicon logo.png
        pocket web favicon logo.png -o custom-favicon.ico
        pocket web favicon logo.png --sizes "64x64,32x32,16x16"
        flavicon logo.png -o favicon.ico
    """
    # Determine output path
    if output is None:
        output = Path.cwd() / "favicon.ico"
    elif not str(output).endswith('.ico'):
        # Auto-add .ico extension if not present
        output = output.with_suffix('.ico')

    # Parse custom sizes if provided
    size_list = None
    if sizes:
        try:
            size_list = []
            for size_str in sizes.split(','):
                w, h = map(int, size_str.strip().split('x'))
                size_list.append((w, h))
        except (ValueError, AttributeError) as e:
            console.print(
                f"[red]Error:[/red] Invalid size format. Use 'WxH,WxH' (e.g., '64x64,32x32')",
                style="bold"
            )
            raise click.Abort()

    try:
        convert_to_favicon(input_file, output, size_list)
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
    favicon_convert()


if __name__ == "__main__":
    main()
