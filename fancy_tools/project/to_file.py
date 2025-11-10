#!/usr/bin/env python3
"""
Project to file converter.

This module scans a project directory and generates a single Markdown file
containing the entire codebase with syntax highlighting and file tree structure.
"""

import os
import argparse
import sys
from collections.abc import Generator
from pathlib import Path
from typing import Set

# Language mapping for syntax highlighting in Markdown code blocks
LANG_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.html': 'html',
    '.css': 'css',
    '.scss': 'scss',
    '.json': 'json',
    '.xml': 'xml',
    '.yml': 'yaml',
    '.yaml': 'yaml',
    '.md': 'markdown',
    '.sh': 'bash',
    '.java': 'java',
    '.c': 'c',
    '.cpp': 'cpp',
    '.go': 'go',
    '.rs': 'rust',
    '.php': 'php',
    '.rb': 'ruby',
    '.sql': 'sql',
    '.dockerfile': 'dockerfile',
    'Dockerfile': 'dockerfile',
}


def get_language_identifier(filename: str) -> str:
    """
    Determine the language identifier for a Markdown code block based on file extension.

    This function maps file extensions to their corresponding language identifiers
    for proper syntax highlighting in Markdown code blocks. Special files like
    'Dockerfile' are handled separately.

    Args:
        filename: The name of the file (can be basename or full path).

    Returns:
        str: Language identifier for syntax highlighting (e.g., 'python', 'javascript').
             Returns 'plaintext' if the extension is not recognized.

    Example:
        >>> get_language_identifier('script.py')
        'python'
        >>> get_language_identifier('Dockerfile')
        'dockerfile'
    """
    # Handle special cases like 'Dockerfile' without extension
    if os.path.basename(filename) in LANG_MAP:
        return LANG_MAP[os.path.basename(filename)]

    # Handle standard extensions
    _, ext = os.path.splitext(filename)
    return LANG_MAP.get(ext.lower(), 'plaintext')


def generate_tree(root_dir: str, exclude: Set[str]) -> Generator[str, None, None]:
    """
    Generate a text representation of the project tree structure.

    Creates an ASCII tree visualization of the directory structure, similar to
    the Unix 'tree' command. Excludes specified files and directories from the
    output. Uses box-drawing characters (│, ├, └) for visual hierarchy.

    Args:
        root_dir: Root directory to scan.
        exclude: Set of file/directory names to exclude from the tree.

    Yields:
        str: Lines representing the tree structure with proper indentation.

    Example:
        >>> for line in generate_tree('/path/to/project', {'node_modules', '.git'}):
        ...     print(line)
        ├── src/
        │   ├── main.py
        │   └── utils.py
    """
    for root, dirs, files in os.walk(root_dir, topdown=True):
        # Modify in-place to prevent os.walk from exploring excluded directories
        dirs[:] = [d for d in dirs if d not in exclude]
        files = [f for f in files if f not in exclude]

        level = root.replace(root_dir, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''

        # Display current directory name (relative)
        if level > 0:
            yield f"{indent}{os.path.basename(root)}/"

        # Display files in current directory
        sub_indent = '│   ' * level + '├── '
        for i, f in enumerate(sorted(files)):
            # Use different prefix for last element
            prefix = '└── ' if i == len(files) - 1 else '├── '
            yield f"{'│   ' * level}{prefix}{f}"


def create_codebase_markdown(
    project_path: str,
    output_file: str,
    exclude_str: str
) -> None:
    """
    Scan a project and generate a comprehensive Markdown documentation file.

    This function walks through a project directory, generates a file tree
    visualization, and includes the content of all text-based files in a single
    Markdown document with proper syntax highlighting. Perfect for documentation,
    code reviews, or feeding entire codebases to AI tools.

    The generated Markdown file includes:
    1. Project title (based on directory name)
    2. ASCII tree structure of the project
    3. Content of each file with syntax highlighting

    Args:
        project_path: Path to the project root directory.
        output_file: Path to the output Markdown file. If None, defaults to
                    '<project_name>-1-file.md'.
        exclude_str: Comma-separated string of files/directories to exclude
                    (e.g., "node_modules,.git,__pycache__").

    Raises:
        IOError: If there's an error writing to the output file.
        SystemExit: If the project path doesn't exist or an error occurs during processing.

    Example:
        >>> create_codebase_markdown(
        ...     project_path='/path/to/my-app',
        ...     output_file='my-app.md',
        ...     exclude_str='node_modules,.git,dist'
        ... )
        🚀 Starting project scan: 'my-app'
        ...
        🎉 Success! Codebase compiled into 'my-app.md'
    """
    # Clean up paths and exclusions
    project_path = os.path.abspath(project_path)
    project_name = os.path.basename(project_path)
    exclude_set = set(exclude_str.split(','))

    # Set default output filename if not provided
    if output_file is None:
        output_file = f"{project_name}-1-file.md"

    print(f"🚀 Starting project scan: '{project_name}'")
    print(f"📂 Source directory: {project_path}")
    print(f"📋 Output file: {output_file}")
    print(f"🙈 Excluded items: {exclude_set}")

    try:
        with open(output_file, 'w', encoding='utf-8') as md_file:
            # 1. Write main title
            md_file.write(f"# {project_name}\n\n")

            # 2. Generate and write project tree
            print("🌳 Generating file tree...")
            md_file.write("```bash\n")
            md_file.write(f"{project_name}/\n")
            for line in generate_tree(project_path, exclude_set):
                md_file.write(f"{line}\n")
            md_file.write("```\n\n")
            print("✅ File tree generated.")

            # 3. Walk through files and write their content
            print("📝 Reading and writing file contents...")
            for root, dirs, files in os.walk(project_path, topdown=True):
                # Ensure we don't descend into excluded directories
                dirs[:] = [d for d in dirs if d not in exclude_set]

                for filename in sorted(files):
                    if filename in exclude_set:
                        continue

                    file_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(file_path, project_path)

                    try:
                        with open(file_path, 'r', encoding='utf-8') as file_content:
                            content = file_content.read()
                            lang = get_language_identifier(filename)

                            md_file.write("---\n\n")  # Horizontal separator
                            md_file.write(f"**`{relative_path}`**:\n")
                            md_file.write(f"```{lang}\n")
                            md_file.write(content)
                            md_file.write("\n```\n\n")

                    except UnicodeDecodeError:
                        print(f"⚠️  Warning: Cannot read file '{relative_path}' (probably binary). Skipping.")
                    except Exception as e:
                        print(f"❌ Error reading file '{relative_path}': {e}")

            print("✅ File contents written.")

    except IOError as e:
        print(f"❌ Error writing to file '{output_file}': {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"\n🎉 Success! Codebase compiled into '{output_file}'")


def main():
    """
    Entry point for CLI argument handling.

    Parses command-line arguments and initiates the project-to-file conversion
    process. This function serves as the main entry point when the script is
    run directly from the command line.

    Command-line Arguments:
        -p, --projet: Root directory of the project to scan (default: current directory).
        -o, --output: Output Markdown file name (default: '<project_name>-1-file.md').
        -e, --exclude: Comma-separated list of files/directories to exclude.

    Raises:
        SystemExit: If the specified project path doesn't exist or is not a directory.
    """
    parser = argparse.ArgumentParser(
        description="Scan a development project and generate a single Markdown file containing the entire codebase.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '-p', '--projet',
        default='.',
        help="Root directory of the project to scan.\nDefault: current directory ('.')."
    )

    parser.add_argument(
        '-o', '--output',
        default=None,
        help="Name of the output Markdown file.\nDefault: '<project_name>-1-file.md'."
    )

    default_exclude = "env,.env,venv,.venv,.gitignore,.git,.vscode,.idea,.cursor,lib,bin,site-packages,node_modules,__pycache__,.DS_Store"
    parser.add_argument(
        '-e', '--exclude',
        default=default_exclude,
        help=f"Comma-separated list of files and directories to ignore.\nDefault: \"{default_exclude}\"."
    )

    args = parser.parse_args()

    if not os.path.isdir(args.projet):
        print(f"Error: Project path '{args.projet}' does not exist or is not a directory.", file=sys.stderr)
        sys.exit(1)

    create_codebase_markdown(args.projet, args.output, args.exclude)


if __name__ == '__main__':
    main()
