# Tests Documentation

This directory contains comprehensive unit tests for the Pocket project.

## Test Structure

The tests are organized to mirror the source code structure:

```
tests/
├── conftest.py                    # Shared fixtures and configuration
├── unit_tests/
│   ├── test_cli.py                # Tests for main CLI
│   ├── test_markdown/
│   │   └── test_renderer.py      # Tests for markdown renderer
│   ├── test_pdf/
│   │   └── test_converter.py     # Tests for PDF converter
│   ├── test_project/
│   │   └── test_to_file.py       # Tests for project-to-file converter
│   ├── test_templates/
│   │   ├── test_cli.py           # Tests for templates CLI
│   │   └── test_validator.py    # Tests for template validator
│   └── test_web/
│       └── test_favicon.py       # Tests for favicon generator
```

## Running Tests

### Basic Test Execution

```bash
# Activate virtual environment first
source .venv/bin/activate

# Run all tests
pytest tests/

# Run tests with verbose output
pytest tests/ -v

# Run a specific test file
pytest tests/unit_tests/test_markdown/test_renderer.py

# Run a specific test function
pytest tests/unit_tests/test_markdown/test_renderer.py::test_read_markdown_file_success
```

### Running Tests with Coverage

```bash
# Run tests with coverage report (terminal)
pytest tests/ --cov=pocket --cov-report=term-missing

# Run tests with coverage report (HTML)
pytest tests/ --cov=pocket --cov-report=html

# Run tests with both terminal and HTML reports
pytest tests/ --cov=pocket --cov-report=term-missing --cov-report=html
```

The HTML coverage report will be generated in the `htmlcov/` directory. Open `htmlcov/index.html` in a browser to view the detailed coverage report.

### Using uv

```bash
# Run tests with uv
uv run pytest tests/

# Run tests with coverage
uv run pytest tests/ --cov=pocket --cov-report=html
```

## Current Test Coverage

As of the latest test run:

- **Overall Coverage**: 72%
- **markdown/renderer.py**: 71% coverage
- **pdf/converter.py**: 54% coverage (requires optional dependencies for full testing)
- **project/to_file.py**: 77% coverage
- **templates_and_cheatsheets/validator.py**: 90% coverage
- **web/favicon.py**: 71% coverage (requires optional dependencies for full testing)

## Test Organization

### Test Naming Convention

- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`
- Test classes: `Test*`

### Test Structure

Each test file follows this structure:

1. **Imports**: Import necessary modules and fixtures
2. **Test Functions**: Individual test cases with descriptive names
3. **Fixtures**: Shared test data and setup (in `conftest.py`)

### Shared Fixtures

The `conftest.py` file provides shared fixtures:

- `temp_dir`: Temporary directory for test files
- `sample_markdown_content`: Sample markdown content for testing
- `sample_markdown_file`: Temporary markdown file
- `sample_project_structure`: Sample project directory structure
- `runner`: CliRunner instance for testing CLI commands

## Writing New Tests

### Guidelines

1. **Test Coverage**: Aim to test all public functions and methods
2. **Edge Cases**: Include tests for edge cases (empty inputs, None values, boundary conditions)
3. **Error Handling**: Test error conditions and exception handling
4. **Isolation**: Each test should be independent and runnable in any order
5. **Mocking**: Use mocking for external dependencies (file I/O, network calls, etc.)

### Example Test

```python
"""
Tests for example module.
"""

import pytest
from pathlib import Path
from super_pocket.example import example_function


def test_example_function_success():
    """Test example function with valid input."""
    result = example_function("input")
    assert result == "expected_output"


def test_example_function_invalid_input():
    """Test example function with invalid input raises error."""
    with pytest.raises(ValueError):
        example_function(None)
```

## Test Execution Validation

### Completeness Check

```bash
# Verify all tests are discovered
pytest --collect-only
```

### Execution Check

```bash
# Run all tests with verbose output
pytest -v
```

### Coverage Check

```bash
# Generate coverage report
pytest --cov=pocket --cov-report=term-missing

# Review uncovered lines
# Ensure gaps are acceptable (error handling, defensive code, etc.)
```

### Isolation Check

```bash
# Run tests in random order (requires pytest-random-order)
pytest --random-order
```

## Dependencies

Test dependencies are specified in `pyproject.toml` under `[project.optional-dependencies.dev]`:

- `pytest>=7.0.0`: Testing framework
- `pytest-cov>=3.0.0`: Coverage plugin

Install test dependencies:

```bash
uv sync --dev
# or
pip install -e ".[dev]"
```

## Continuous Integration

Tests should be run automatically in CI/CD pipelines. The test suite is designed to:

- Run quickly (< 1 second for full suite)
- Be deterministic (no random failures)
- Not require external services
- Work on all supported Python versions (3.11+)

## Troubleshooting

### Tests Failing

1. Ensure virtual environment is activated
2. Install all dependencies: `uv sync`
3. Check Python version: `python --version` (should be 3.11+)
4. Run tests with verbose output: `pytest -v`

### Coverage Issues

1. Ensure `pytest-cov` is installed
2. Check that source paths are correct in `pyproject.toml`
3. Verify coverage exclusions are appropriate

### Import Errors

1. Ensure package is installed in development mode: `uv sync`
2. Check that `pocket` is in Python path
3. Verify `__init__.py` files exist in all package directories

## Notes

- Tests for PDF and favicon conversion may require optional dependencies (`fpdf2`, `markdown-pdf`, `Pillow`)
- Some tests are skipped if optional dependencies are not installed
- Binary file handling tests may behave differently on different operating systems
- Permission-related tests may be skipped on systems that don't support permission changes

