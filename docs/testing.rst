Testing Guide
=============

Comprehensive guide to testing Super Pocket and writing tests for contributions.

Testing Philosophy
------------------

Super Pocket follows these testing principles:

* **Comprehensive Coverage**: Aim for >80% code coverage
* **Fast Execution**: Tests should run quickly
* **Isolated**: Tests should not depend on each other
* **Readable**: Tests serve as documentation
* **Maintainable**: Easy to update as code changes

Test Structure
--------------

Test Organization
~~~~~~~~~~~~~~~~~

.. code-block:: text

   tests/
   ├── __init__.py
   ├── README_TESTS.md                    # Testing documentation
   ├── conftest.py                        # Pytest configuration & fixtures
   ├── unit_tests/                        # Unit tests
   │   ├── __init__.py
   │   ├── test_markdown/
   │   │   ├── __init__.py
   │   │   └── test_renderer.py
   │   ├── test_project/
   │   │   ├── __init__.py
   │   │   └── test_to_file.py
   │   ├── test_pdf/
   │   │   └── test_converter.py
   │   ├── test_web/
   │   │   └── test_favicon.py
   │   └── test_templates/
   │       ├── test_cli.py
   │       └── test_validator.py
   ├── integration_tests/                 # Integration tests
   │   └── test_cli_integration.py
   ├── fixtures/                          # Test data
   │   ├── sample.md
   │   ├── sample_project/
   │   └── test_images/
   └── helpers.py                         # Test utilities

Running Tests
-------------

Basic Usage
~~~~~~~~~~~

.. code-block:: bash

   # Run all tests
   pytest

   # Run with verbose output
   pytest -v

   # Run specific test file
   pytest tests/unit_tests/test_markdown/test_renderer.py

   # Run specific test
   pytest tests/unit_tests/test_markdown/test_renderer.py::test_render_basic

   # Run tests matching pattern
   pytest -k "markdown"

Coverage Reports
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run with coverage
   pytest --cov=pocket

   # Generate HTML coverage report
   pytest --cov=pocket --cov-report=html

   # View coverage report
   open htmlcov/index.html  # macOS
   xdg-open htmlcov/index.html  # Linux

   # Generate terminal report
   pytest --cov=pocket --cov-report=term-missing

Coverage Configuration
~~~~~~~~~~~~~~~~~~~~~~

Configuration in ``pyproject.toml``:

.. code-block:: toml

   [tool.pytest.ini_options]
   testpaths = ["tests"]
   python_files = "test_*.py"
   python_functions = "test_*"
   addopts = "-v --cov=pocket --cov-report=term-missing"

   [tool.coverage.run]
   source = ["pocket"]
   omit = [
       "*/tests/*",
       "*/__init__.py",
       "*/cli.py",
   ]

Writing Tests
-------------

Test File Structure
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   """Test module for markdown renderer.

   This module tests the markdown rendering functionality
   including basic rendering, syntax highlighting, and
   error handling.
   """

   import pytest
   from super_pocket.markdown.renderer import render_markdown


   class TestMarkdownRenderer:
       """Test cases for markdown rendering."""

       def test_render_basic_markdown(self):
           """Test rendering basic markdown content."""
           content = "# Hello World"
           result = render_markdown(content, from_string=True)
           assert "Hello World" in result

       def test_render_with_code_blocks(self):
           """Test rendering markdown with code blocks."""
           content = "```python\nprint('test')\n```"
           result = render_markdown(content, from_string=True)
           assert "print" in result

       def test_render_missing_file(self):
           """Test error handling for missing files."""
           with pytest.raises(FileNotFoundError):
               render_markdown("nonexistent.md")

Test Naming Conventions
~~~~~~~~~~~~~~~~~~~~~~~

* Test files: ``test_*.py``
* Test classes: ``Test*``
* Test functions: ``test_*``
* Be descriptive: ``test_export_excludes_patterns``

Good test names:

.. code-block:: python

   def test_render_markdown_with_headers()
   def test_export_project_creates_file()
   def test_copy_template_creates_directory()
   def test_invalid_input_raises_value_error()

Fixtures
--------

Common Fixtures
~~~~~~~~~~~~~~~

Define reusable fixtures in ``conftest.py``:

.. code-block:: python

   import pytest
   from pathlib import Path
   import tempfile
   import shutil


   @pytest.fixture
   def temp_dir():
       """Create temporary directory for tests."""
       temp = tempfile.mkdtemp()
       yield Path(temp)
       shutil.rmtree(temp)


   @pytest.fixture
   def sample_markdown():
       """Sample markdown content."""
       return """
       # Test Document

       ## Section 1

       - Item 1
       - Item 2

       ```python
       def hello():
           print("world")
       ```
       """


   @pytest.fixture
   def sample_project(temp_dir):
       """Create a sample project structure."""
       project = temp_dir / "sample_project"
       project.mkdir()

       # Create files
       (project / "README.md").write_text("# Project")
       (project / "main.py").write_text("print('hello')")

       src = project / "src"
       src.mkdir()
       (src / "__init__.py").write_text("")

       return project

Using Fixtures
~~~~~~~~~~~~~~

.. code-block:: python

   def test_export_project(sample_project, temp_dir):
       """Test exporting a project."""
       output = temp_dir / "export.md"

       export_project(
           project_path=sample_project,
           output_file=output
       )

       assert output.exists()
       content = output.read_text()
       assert "README.md" in content
       assert "main.py" in content

Parameterized Tests
-------------------

Testing Multiple Inputs
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   @pytest.mark.parametrize("input_text,expected", [
       ("# Heading", "Heading"),
       ("**bold**", "bold"),
       ("*italic*", "italic"),
       ("`code`", "code"),
   ])
   def test_markdown_elements(input_text, expected):
       """Test rendering various markdown elements."""
       result = render_markdown(input_text, from_string=True)
       assert expected in result


   @pytest.mark.parametrize("size", [16, 32, 64])
   def test_favicon_sizes(size):
       """Test generating favicons at different sizes."""
       result = generate_favicon("logo.png", size=size)
       assert result.size == (size, size)

Mocking and Patching
--------------------

Mocking External Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from unittest.mock import Mock, patch, mock_open


   def test_render_file_with_mock():
       """Test file rendering with mocked file system."""
       mock_content = "# Test"

       with patch("builtins.open", mock_open(read_data=mock_content)):
           result = render_markdown("test.md")
           assert "Test" in result


   def test_web_request_with_mock():
       """Test web functionality with mocked requests."""
       mock_response = Mock()
       mock_response.status_code = 200
       mock_response.text = "Success"

       with patch("requests.get", return_value=mock_response):
           result = fetch_data("http://example.com")
           assert result == "Success"

Mocking Click Commands
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from click.testing import CliRunner
   from super_pocket.cli import cli


   def test_cli_markdown_render():
       """Test markdown render command."""
       runner = CliRunner()

       with runner.isolated_filesystem():
           # Create test file
           with open("test.md", "w") as f:
               f.write("# Test")

           result = runner.invoke(cli, ["markdown", "render", "test.md"])

           assert result.exit_code == 0
           assert "Test" in result.output

Testing Patterns
----------------

Testing CLI Commands
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def test_project_export_command(temp_dir):
       """Test project export CLI command."""
       runner = CliRunner()

       with runner.isolated_filesystem():
           # Setup
           Path("test.py").write_text("print('hello')")

           # Execute
           result = runner.invoke(cli, [
               "project", "to-file",
               "-o", "output.md"
           ])

           # Assert
           assert result.exit_code == 0
           assert Path("output.md").exists()

Testing File Operations
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def test_file_operations(temp_dir):
       """Test file creation and modification."""
       test_file = temp_dir / "test.txt"

       # Test file creation
       test_file.write_text("content")
       assert test_file.exists()

       # Test file reading
       content = test_file.read_text()
       assert content == "content"

       # Test file deletion
       test_file.unlink()
       assert not test_file.exists()

Testing Error Handling
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def test_error_handling():
       """Test various error conditions."""
       # Test ValueError
       with pytest.raises(ValueError, match="Invalid input"):
           process_invalid_input()

       # Test FileNotFoundError
       with pytest.raises(FileNotFoundError):
           open_nonexistent_file()

       # Test custom exceptions
       with pytest.raises(TemplateNotFoundError):
           get_template("nonexistent")

Test Markers
------------

Using Markers
~~~~~~~~~~~~~

.. code-block:: python

   import pytest


   @pytest.mark.slow
   def test_slow_operation():
       """Test that takes a long time."""
       pass


   @pytest.mark.integration
   def test_integration():
       """Integration test."""
       pass


   @pytest.mark.skipif(sys.platform == "win32", reason="Unix only")
   def test_unix_specific():
       """Test for Unix systems only."""
       pass


   @pytest.mark.xfail(reason="Known issue #123")
   def test_known_issue():
       """Test for known bug."""
       pass

Running Marked Tests
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run only integration tests
   pytest -m integration

   # Skip slow tests
   pytest -m "not slow"

   # Run multiple markers
   pytest -m "unit or integration"

Continuous Integration
----------------------

GitHub Actions
~~~~~~~~~~~~~~

Example ``.github/workflows/tests.yml``:

.. code-block:: yaml

   name: Tests

   on: [push, pull_request]

   jobs:
     test:
       runs-on: ubuntu-latest
       strategy:
         matrix:
           python-version: [3.11, 3.12, 3.13]

       steps:
       - uses: actions/checkout@v2

       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: ${{ matrix.python-version }}

       - name: Install dependencies
         run: |
           pip install -e ".[all,dev]"

       - name: Run tests
         run: |
           pytest --cov=pocket --cov-report=xml

       - name: Upload coverage
         uses: codecov/codecov-action@v2

Test Coverage Goals
-------------------

Coverage Targets
~~~~~~~~~~~~~~~~

* **Overall**: >80% coverage
* **Core modules**: >90% coverage
* **CLI**: >70% coverage
* **New code**: 100% coverage

Checking Coverage
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate coverage report
   pytest --cov=pocket --cov-report=term-missing

   # Check coverage threshold
   pytest --cov=pocket --cov-fail-under=80

Debugging Tests
---------------

Using pdb
~~~~~~~~~

.. code-block:: python

   def test_with_debugging():
       """Test with debugging."""
       result = complex_operation()

       # Add breakpoint
       import pdb; pdb.set_trace()

       assert result == expected

Verbose Output
~~~~~~~~~~~~~~

.. code-block:: bash

   # Maximum verbosity
   pytest -vv

   # Show print statements
   pytest -s

   # Show local variables on failure
   pytest -l

Best Practices
--------------

Test Guidelines
~~~~~~~~~~~~~~~

1. **One Assertion Per Test** (when possible)
2. **Test One Thing** - Keep tests focused
3. **Use Descriptive Names** - Self-documenting
4. **Arrange-Act-Assert** - Clear test structure
5. **Independent Tests** - No shared state
6. **Fast Tests** - Mock slow operations

Example
~~~~~~~

.. code-block:: python

   def test_export_creates_output_file(temp_dir):
       """Test that export creates the output file."""
       # Arrange
       project = create_sample_project(temp_dir)
       output = temp_dir / "export.md"

       # Act
       export_project(project, output)

       # Assert
       assert output.exists()

See Also
--------

* :doc:`contributing` - Contributing guide
* :doc:`api` - API documentation
* `pytest documentation <https://docs.pytest.org/>`_
