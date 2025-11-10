# Markdown Tools

Documentation for markdown rendering and conversion tools.

## Overview

The markdown tools provide beautiful terminal rendering of Markdown files with syntax highlighting and rich formatting.

## Commands

### Render Markdown File

```bash
pocket markdown render <file>
```

#### Options

- `<file>`: Path to the Markdown file to render (required)
- `--width, -w`: Output width in characters (optional)

#### Examples

```bash
# Render README
pocket markdown render README.md

# Render with custom width
pocket markdown render documentation.md -w 100

# Using standalone command (backward compatible)
markd README.md
```

## Python API

### Reading Markdown Files

```python
from pathlib import Path
from pocket.markdown.renderer import read_markdown_file

file_path = Path("README.md")
content = read_markdown_file(file_path)
```

### Rendering Markdown

```python
from pocket.markdown.renderer import render_markdown
from rich.console import Console

console = Console()
render_markdown(content, console)
```

## Features

- **Syntax Highlighting**: Automatic code block syntax highlighting
- **Rich Formatting**: Bold, italic, links, lists, tables
- **Code Blocks**: Supports all major programming languages
- **Headers**: Proper heading hierarchy rendering
- **Lists**: Ordered and unordered lists
- **Links**: Clickable links in supported terminals
- **Images**: Image placeholders (terminal-dependent)

## Supported Markdown Features

- [x] Headers (H1-H6)
- [x] Bold and italic text
- [x] Code blocks with syntax highlighting
- [x] Inline code
- [x] Lists (ordered and unordered)
- [x] Links
- [x] Tables
- [x] Blockquotes
- [x] Horizontal rules

## Error Handling

The tool handles various error conditions gracefully:

- **File not found**: Clear error message with path
- **Permission denied**: Indicates permission issues
- **Invalid file**: Checks if path is a file (not directory)
- **Encoding errors**: Handles UTF-8 encoding issues

## Examples

### Basic Usage

```bash
# Render any markdown file
markd docs/guide.md
pocket markdown render docs/guide.md
```

### Integration with Other Tools

```bash
# Generate project export and view it
pocket project to-file -o project.md
pocket markdown render project.md
```

## Tips

1. **Terminal Support**: Best experience with modern terminals (iTerm2, Windows Terminal, etc.)
2. **Color Themes**: Respects terminal color scheme
3. **Width**: Use `-w` option to adjust output width for readability
4. **Piping**: Works well with standard input/output

## Common Issues

### Colors Not Showing

Some terminals may not support 24-bit colors. Try:
- Using a modern terminal emulator
- Checking terminal color support: `echo $TERM`

### Unicode Characters

Ensure your terminal supports UTF-8 encoding:
```bash
export LANG=en_US.UTF-8
```

## Related Commands

- [`project to-file`](project_tools.md): Export project to Markdown
- [`templates view`](agent_templates.md): View templates in rendered Markdown
