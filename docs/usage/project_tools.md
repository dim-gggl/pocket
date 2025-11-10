# Project Tools

Documentation for project management and export tools.

## Overview

Project tools allow you to export entire codebases to single Markdown files, making it easy to share projects, create documentation, or analyze code structure.

## Commands

### Project to File

```bash
pocket project to-file [OPTIONS]
```

#### Options

- `-p, --path TEXT`: Root directory of the project to scan (default: current directory)
- `-o, --output TEXT`: Output Markdown file name (default: `<project_name>-1-file.md`)
- `-e, --exclude TEXT`: Comma-separated list of files/directories to exclude

#### Default Exclusions

By default, the following are excluded:
- `env`, `.env`, `venv`, `.venv`
- `.gitignore`, `.git`
- `.vscode`, `.idea`, `.cursor`
- `lib`, `bin`, `site-packages`
- `node_modules`, `__pycache__`
- `.DS_Store`

## Examples

### Basic Usage

```bash
# Export current directory
pocket project to-file

# Export specific project
pocket project to-file -p ./my-project

# Custom output file
pocket project to-file -o my-export.md

# Standalone command (backward compatible)
project to-file -p . -o output.md
```

### Advanced Usage

```bash
# Custom exclusions
pocket project to-file -e "node_modules,dist,build,coverage"

# Export without tests
pocket project to-file -e "tests,__pycache__,.git"

# Large project with minimal exclusions
pocket project to-file -p ./large-project -e ".git,node_modules"
```

## Output Format

The generated Markdown file includes:

1. **Project Title**: Name of the project directory
2. **File Tree**: ASCII tree structure of the project
3. **File Contents**: Each file with:
   - Relative path
   - Syntax-highlighted code block
   - Proper language detection

### Example Output

```markdown
# MyProject

\`\`\`bash
MyProject/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
└── README.md
\`\`\`

---

**`src/main.py`**:
\`\`\`python
def main():
    print("Hello, world!")
\`\`\`

---

**`README.md`**:
\`\`\`markdown
# MyProject
...
\`\`\`
```

## Language Detection

The tool automatically detects programming languages based on file extensions:

### Supported Languages

- **Python**: `.py`
- **JavaScript/TypeScript**: `.js`, `.ts`
- **Web**: `.html`, `.css`, `.scss`
- **Data**: `.json`, `.xml`, `.yml`, `.yaml`
- **Shell**: `.sh`, `Dockerfile`
- **Compiled**: `.java`, `.c`, `.cpp`, `.go`, `.rs`
- **Scripting**: `.php`, `.rb`, `.sql`
- **Documentation**: `.md`

Unknown extensions default to `plaintext`.

## Use Cases

### 1. Code Reviews

Export project for sharing with reviewers:

```bash
pocket project to-file -p ./feature-branch -o code-review.md
```

### 2. AI Analysis

Prepare codebase for AI code analysis:

```bash
pocket project to-file -e "tests,docs,.git" -o codebase-for-ai.md
```

### 3. Documentation

Create snapshot of project structure:

```bash
pocket project to-file -o docs/project-structure.md
```

### 4. Archival

Archive project state:

```bash
pocket project to-file -o archives/project-v1.0.0.md
```

## Python API

### Basic Usage

```python
from pocket.project.to_file import create_codebase_markdown

create_codebase_markdown(
    project_path="./my-project",
    output_file="export.md",
    exclude_str="node_modules,.git,dist"
)
```

### Custom Language Detection

```python
from pocket.project.to_file import get_language_identifier

lang = get_language_identifier("app.py")  # Returns: "python"
```

### Generate Tree Only

```python
from pocket.project.to_file import generate_tree

for line in generate_tree("/path/to/project", {"node_modules", ".git"}):
    print(line)
```

## Performance

### Large Projects

For large projects:
- Use specific exclusions to reduce size
- Consider excluding test files and documentation
- Binary files are automatically skipped

### Memory Usage

The tool reads files sequentially, so memory usage is generally low even for large projects.

## Error Handling

### Common Errors

1. **Permission Denied**: Some files may be unreadable
   - Tool continues with other files
   - Warning message is displayed

2. **Binary Files**: Non-text files cause encoding errors
   - Automatically skipped
   - Warning message is displayed

3. **Invalid Path**: Project directory doesn't exist
   - Error message with path
   - Execution stops

## Tips

1. **Exclusions**: Always exclude version control and dependencies
2. **Output Location**: Save output outside project to avoid including it
3. **Review Output**: Large projects create large files - review before sharing
4. **Compression**: Consider compressing output for large projects

## Integration

### With Markdown Renderer

```bash
# Generate and view
pocket project to-file -o temp.md
pocket markdown render temp.md
```

### With Git

```bash
# Export specific branch
git checkout feature-branch
pocket project to-file -o feature-export.md
```

### In Scripts

```bash
#!/bin/bash
# Export all branches
for branch in $(git branch --list | tr -d ' *'); do
    git checkout $branch
    pocket project to-file -o "exports/${branch}.md"
done
```

## Related Commands

- [`markdown render`](markdown_tools.md): View generated Markdown file
- [`templates list`](agent_templates.md): Explore available templates
