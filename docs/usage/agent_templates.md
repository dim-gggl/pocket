# Agent Templates & Cheatsheets

Documentation for managing agent configuration templates and development cheatsheets.

## Overview

Fancy Tools includes a comprehensive system for managing and distributing AI agent configuration templates and development cheatsheets. These resources are packaged with the tool and can be easily copied to your projects.

## Commands

### List Items

```bash
pocket templates list [OPTIONS]
```

#### Options

- `-t, --type [templates|cheatsheets|all]`: Type of items to list (default: all)

#### Examples

```bash
# List everything
pocket templates list

# List only templates
pocket templates list -t templates

# List only cheatsheets
pocket templates list -t cheatsheets
```

### View Item

```bash
pocket templates view <name> [OPTIONS]
```

#### Arguments

- `<name>`: Name of template or cheatsheet (without .md extension)

#### Options

- `-t, --type [template|cheatsheet]`: Type of item (auto-detected if not specified)

#### Examples

```bash
# View a template
pocket templates view unit_tests_agent

# View a cheatsheet
pocket templates view SQL

# Explicitly specify type
pocket templates view unit_tests_agent -t template
```

### Copy Item

```bash
pocket templates copy <name> [OPTIONS]
```

#### Arguments

- `<name>`: Name of template or cheatsheet to copy

#### Options

- `-o, --output PATH`: Output path (file or directory)
- `-t, --type [template|cheatsheet]`: Type of item
- `-f, --force`: Overwrite existing file

#### Examples

```bash
# Copy to current directory
pocket templates copy unit_tests_agent

# Copy to specific directory
pocket templates copy unit_tests_agent -o .agents/

# Copy with custom name
pocket templates copy SQL -o docs/sql-cheatsheet.md

# Force overwrite
pocket templates copy agent_maker -o .agents/ -f
```

### Initialize Templates

```bash
pocket templates init [OPTIONS]
```

#### Options

- `-o, --output PATH`: Directory for templates (default: `.AGENTS`)

#### Examples

```bash
# Initialize in default location (.AGENTS)
pocket templates init

# Initialize in custom directory
pocket templates init -o ./my-agents/
```

## Available Templates

### Agent Configuration Templates

#### 1. Unit Tests Agent

**File**: `unit_tests_agent.md`

Comprehensive configuration for an AI agent that generates unit tests using pytest and coverage.py.

**Features**:
- Pytest-based test generation
- Coverage analysis and reporting
- Fixture creation
- Mocking external dependencies
- Edge case testing
- Async code support

**Use when**: You need comprehensive unit tests for your Python project.

```bash
pocket templates copy unit_tests_agent -o .agents/
```

#### 2. Agent Maker

**File**: `agent_maker.md`

Template for creating new AI agent configurations.

**Features**:
- Structured agent definition format
- Best practices guidance
- Configuration validation
- Behavioral constraints documentation

**Use when**: Creating custom AI agents for specific tasks.

```bash
pocket templates copy agent_maker -o .agents/
```

#### 3. Agents Template Maker

**File**: `agents_template_maker.md`

Meta-template for generating AGENTS.md files for projects.

**Features**:
- Project-specific agent definitions
- Multi-agent workflows
- Integration guidelines
- Customization instructions

**Use when**: Setting up agent configurations for a new project.

```bash
pocket templates copy agents_template_maker -o .agents/
```

#### 4. Job Assistant Agent

**File**: `job_assistant_agent.md`

Configuration for an AI agent that helps with job search and applications.

**Features**:
- Resume optimization
- Cover letter generation
- Job description analysis
- Interview preparation

**Use when**: You need assistance with job applications and career development.

```bash
pocket templates copy job_assistant_agent -o ./career/
```

## Available Cheatsheets

### SQL Cheatsheet

**File**: `SQL.md`

Comprehensive SQL commands and queries reference.

**Includes**:
- Basic queries (SELECT, INSERT, UPDATE, DELETE)
- JOIN operations
- Aggregate functions
- Subqueries
- Window functions
- Common table expressions (CTEs)
- Performance tips

```bash
pocket templates view SQL
pocket templates copy SQL -o docs/cheatsheets/
```

## Workflow Examples

### Setting Up New Project

```bash
# 1. Initialize agent templates
cd my-new-project
pocket templates init

# 2. Review available templates
pocket templates list -t templates

# 3. Copy specific templates you need
pocket templates copy unit_tests_agent -o .agents/

# 4. View and customize
pocket templates view unit_tests_agent
```

### Adding Cheatsheets to Documentation

```bash
# Create docs directory
mkdir -p docs/cheatsheets

# Copy cheatsheets
pocket templates copy SQL -o docs/cheatsheets/

# Add more as needed
# pocket templates copy Git -o docs/cheatsheets/
# pocket templates copy Docker -o docs/cheatsheets/
```

### Quick Reference Access

```bash
# View cheatsheet without copying
pocket templates view SQL

# Or render with markdown tool
pocket templates copy SQL -o /tmp/sql.md
pocket markdown render /tmp/sql.md
```

## Python API

### Programmatic Access

```python
from pocket.templates_and_cheatsheets import TEMPLATES_DIR, CHEATSHEETS_DIR

# List templates
templates = list(TEMPLATES_DIR.glob("*.md"))
print(f"Found {len(templates)} templates")

# Read template content
template_path = TEMPLATES_DIR / "unit_tests_agent.md"
content = template_path.read_text(encoding='utf-8')
```

### Custom Template Management

```python
from pathlib import Path
from pocket.templates_and_cheatsheets.validator import validate_template_file

# Validate a template
template_path = Path(".agents/custom_agent.md")
is_valid = validate_template_file(template_path, verbose=True)
```

## Creating Custom Templates

While Fancy Tools provides built-in templates, you can create your own:

### Template Structure

```markdown
# Agent Name

## Purpose
Brief description of what this agent does

## Configuration
Detailed configuration instructions

## Usage
How to use this agent

## Examples
Practical examples
```

### Best Practices

1. **Clear Documentation**: Explain purpose and usage
2. **Examples**: Include practical examples
3. **Constraints**: Document limitations and requirements
4. **Validation**: Test templates before distributing

### Validation

```python
from pocket.templates_and_cheatsheets.validator import validate_template_file

validate_template_file(Path("my-template.md"))
```

## Template Locations

### Built-in Templates

Located in the package:
```
pocket/templates_and_cheatsheets/
├── templates/
│   ├── agent_maker.md
│   ├── unit_tests_agent.md
│   ├── agents_template_maker.md
│   └── job_assistant_agent.md
└── cheatsheets/
    └── SQL.md
```

### Project Templates

Your project templates (copied from built-in):
```
.AGENTS/
├── AGENTS.md
├── unit_tests_agent.md
└── custom_agent.md
```

## Tips

1. **Version Control**: Commit copied templates to track customizations
2. **Customization**: Templates are meant to be customized per project
3. **Organization**: Keep templates in `.AGENTS/` or similar directory
4. **Backup**: Templates are valuable - back them up
5. **Sharing**: Share customized templates across your projects

## Common Workflows

### Starting New Python Project

```bash
pocket templates init
pocket templates copy unit_tests_agent -o .agents/
# Customize unit_tests_agent.md for your project
```

### Code Review Preparation

```bash
pocket project to-file -o review.md
pocket templates copy unit_tests_agent -o .agents/
# Review code with testing guidelines in mind
```

### Learning New Technology

```bash
# View relevant cheatsheet
pocket templates view SQL

# Copy for reference
pocket templates copy SQL -o ~/cheatsheets/
```

## Related Commands

- [`markdown render`](markdown_tools.md): View templates in formatted output
- [`project to-file`](project_tools.md): Export project with agent configs

## Future Enhancements

Coming soon:
- More cheatsheets (Git, Docker, Kubernetes)
- Template validation command
- Interactive template creation wizard
- Template versioning
- Community template repository
