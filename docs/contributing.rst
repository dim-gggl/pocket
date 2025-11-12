Contributing to Super Pocket
============================

Thank you for your interest in contributing to Super Pocket! This guide will help you get started.

Code of Conduct
---------------

By participating in this project, you agree to:

* Be respectful and inclusive
* Welcome newcomers and help them learn
* Focus on what is best for the community
* Show empathy towards other community members

Getting Started
---------------

Setting Up Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Fork and Clone:**

   .. code-block:: bash

      # Fork the repository on GitHub first
      git clone https://github.com/YOUR-USERNAME/super-pocket.git
      cd super-pocket

2. **Create Virtual Environment:**

   .. code-block:: bash

      # Using venv
      python -m venv .venv
      source .venv/bin/activate  # On Windows: .venv\Scripts\activate

      # Or using uv (recommended)
      uv sync

3. **Install Development Dependencies:**

   .. code-block:: bash

      # Install with all dependencies
      pip install -e ".[all,dev]"

      # Or using uv
      uv pip install -e ".[all,dev]"

4. **Verify Installation:**

   .. code-block:: bash

      # Run tests
      pytest

      # Check version
      pocket --version

Creating a Branch
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Create a feature branch
   git checkout -b feature/your-feature-name

   # Or for bug fixes
   git checkout -b fix/bug-description

How to Contribute
-----------------

Reporting Bugs
~~~~~~~~~~~~~~

Before creating a bug report:

* Check existing issues
* Verify you're using the latest version
* Test with minimal reproduction case

When creating a bug report, include:

* Clear, descriptive title
* Steps to reproduce
* Expected vs actual behavior
* Environment details (OS, Python version)
* Error messages and tracebacks

Example bug report:

.. code-block:: markdown

   **Bug Description**
   `pocket markdown render` crashes on files with emoji

   **To Reproduce**
   1. Create file with emoji: `echo "# 🚀 Test" > test.md`
   2. Run: `pocket markdown render test.md`
   3. See error

   **Expected Behavior**
   File renders correctly with emoji displayed

   **Environment**
   - OS: macOS 13.4
   - Python: 3.11.4
   - Super Pocket: 1.0.1

   **Error Message**
   ```
   UnicodeDecodeError: 'ascii' codec can't decode byte...
   ```

Suggesting Features
~~~~~~~~~~~~~~~~~~~

Feature requests should include:

* Clear use case description
* Why this feature would be useful
* Proposed implementation (optional)
* Examples of similar features elsewhere

Example feature request:

.. code-block:: markdown

   **Feature Request**
   Add JSON export format for projects

   **Use Case**
   I need to export project structure as JSON for processing
   with other tools and automation scripts.

   **Proposed Solution**
   Add `-f json` option to `pocket project to-file`:
   ```bash
   pocket project to-file -f json -o project.json
   ```

   **Alternatives**
   Could pipe markdown output through converter, but native
   support would be more efficient.

Contributing Code
-----------------

Code Style
~~~~~~~~~~

Super Pocket follows PEP 8 with these tools:

* **black** - Code formatting
* **ruff** - Linting
* **mypy** - Type checking (optional)

Before committing:

.. code-block:: bash

   # Format code
   black pocket tests

   # Check linting
   ruff check pocket tests

   # Type check (optional)
   mypy pocket

Project automatically formats on commit with pre-commit hooks.

Type Hints
~~~~~~~~~~

All new code should include type hints:

.. code-block:: python

   from typing import Optional, List
   from pathlib import Path

   def export_project(
       project_path: str | Path,
       output_file: str | Path,
       exclude: Optional[List[str]] = None
   ) -> None:
       """Export project to file.

       Args:
           project_path: Path to project directory
           output_file: Output file path
           exclude: Optional list of patterns to exclude
       """
       pass

Documentation
~~~~~~~~~~~~~

All public functions and classes need docstrings:

.. code-block:: python

   def function(param: str) -> bool:
       """Brief one-line description.

       Longer description explaining the function's purpose
       and behavior in more detail.

       Args:
           param: Description of the parameter

       Returns:
           Description of return value

       Raises:
           ValueError: When input is invalid

       Examples:
           >>> function("test")
           True
       """
       pass

Testing
~~~~~~~

All new features and bug fixes need tests:

.. code-block:: python

   import pytest
   from pocket.markdown.renderer import render_markdown

   def test_render_basic_markdown():
       """Test basic markdown rendering."""
       content = "# Hello World"
       result = render_markdown(content, from_string=True)
       assert "Hello World" in result

   def test_render_missing_file():
       """Test handling of missing files."""
       with pytest.raises(FileNotFoundError):
           render_markdown("nonexistent.md")

Run tests:

.. code-block:: bash

   # Run all tests
   pytest

   # Run with coverage
   pytest --cov=pocket --cov-report=html

   # Run specific test
   pytest tests/unit_tests/test_markdown/test_renderer.py

See :doc:`testing` for detailed testing guidelines.

Commit Messages
~~~~~~~~~~~~~~~

Write clear, descriptive commit messages:

.. code-block:: text

   Add JSON export format for projects

   - Implement JSONExporter class
   - Add -f/--format option to CLI
   - Include tests and documentation
   - Update CHANGELOG.md

   Closes #123

Format:

* First line: Brief summary (50 chars max)
* Blank line
* Detailed description (72 chars per line)
* Reference issues/PRs

Pull Request Process
--------------------

1. **Create Feature Branch:**

   .. code-block:: bash

      git checkout -b feature/your-feature

2. **Make Changes:**

   * Write code following style guide
   * Add tests
   * Update documentation
   * Run linters and tests

3. **Commit Changes:**

   .. code-block:: bash

      git add .
      git commit -m "Your descriptive message"

4. **Push to Fork:**

   .. code-block:: bash

      git push origin feature/your-feature

5. **Create Pull Request:**

   * Go to GitHub and create PR
   * Fill out PR template
   * Link related issues
   * Wait for review

Pull Request Checklist
~~~~~~~~~~~~~~~~~~~~~~

Before submitting, ensure:

* [ ] Code follows style guide (black, ruff)
* [ ] All tests pass
* [ ] New tests added for new features
* [ ] Documentation updated
* [ ] CHANGELOG.md updated
* [ ] No merge conflicts
* [ ] PR description is clear
* [ ] Linked to related issues

Review Process
~~~~~~~~~~~~~~

Your PR will be reviewed for:

* Code quality and style
* Test coverage
* Documentation completeness
* Backward compatibility
* Performance implications

Be prepared to:

* Answer questions
* Make requested changes
* Iterate on design

Contributing Documentation
--------------------------

Documentation improvements are highly valued!

Building Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Install sphinx dependencies
   pip install -r docs/requirements.txt

   # Build HTML documentation
   cd docs
   make html

   # View in browser
   open _build/html/index.html  # macOS
   xdg-open _build/html/index.html  # Linux

Documentation Structure
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   docs/
   ├── conf.py              # Sphinx configuration
   ├── index.rst            # Homepage
   ├── installation.rst     # Installation guide
   ├── quickstart.rst       # Quick start guide
   ├── commands.rst         # Commands reference
   ├── api.rst              # API documentation
   ├── contributing.rst     # This file
   ├── _static/             # Static files (CSS, images)
   └── _templates/          # Custom templates

Documentation Style
~~~~~~~~~~~~~~~~~~~

* Use clear, concise language
* Include code examples
* Add screenshots where helpful
* Cross-reference related sections
* Follow reStructuredText format

Contributing Templates
----------------------

Adding New Templates
~~~~~~~~~~~~~~~~~~~~

1. **Create Template File:**

   .. code-block:: bash

      # Create in templates directory
      touch pocket/templates_and_cheatsheets/templates/your_agent.md

2. **Write Template Content:**

   Follow this structure:

   .. code-block:: markdown

      # Agent Name

      ## Purpose
      Brief description

      ## Instructions
      Detailed steps

      ## Examples
      Code examples

3. **Test Template:**

   .. code-block:: bash

      # Verify it appears in list
      pocket templates list

      # Test viewing
      pocket templates view your_agent

      # Test copying
      pocket templates copy your_agent -o /tmp/

4. **Update Documentation:**

   Add your template to ``docs/templates.rst``

Template Guidelines
~~~~~~~~~~~~~~~~~~~

* Use clear, descriptive names
* Include comprehensive instructions
* Provide examples
* Test thoroughly
* Document use cases

Contributing Cheatsheets
~~~~~~~~~~~~~~~~~~~~~~~~

Similar process to templates:

1. Create file in ``pocket/templates_and_cheatsheets/cheatsheets/``
2. Follow markdown format
3. Include comprehensive reference
4. Test with ``pocket templates view NAME -t cheatsheet``

Release Process
---------------

For maintainers releasing new versions:

1. **Update Version:**

   Update in ``pyproject.toml``

2. **Update Changelog:**

   Document all changes in ``CHANGELOG.md``

3. **Create Release:**

   .. code-block:: bash

      git tag -a v1.0.2 -m "Release v1.0.2"
      git push origin v1.0.2

4. **Build and Publish:**

   .. code-block:: bash

      # Build package
      python -m build

      # Upload to PyPI
      python -m twine upload dist/*

Community
---------

Ways to Get Involved
~~~~~~~~~~~~~~~~~~~~

* Report bugs
* Suggest features
* Improve documentation
* Write tutorials
* Help other users
* Review pull requests
* Contribute code

Getting Help
~~~~~~~~~~~~

* GitHub Issues - Bug reports and features
* Discussions - Questions and ideas
* Documentation - Guides and references

Recognition
~~~~~~~~~~~

Contributors are recognized in:

* CONTRIBUTORS.md file
* Release notes
* GitHub contributors page

Thank You!
----------

Every contribution, no matter how small, is valuable and appreciated.
Thank you for helping make Super Pocket better!

See Also
--------

* :doc:`testing` - Testing guidelines
* :doc:`api` - API documentation
* :doc:`quickstart` - Getting started
