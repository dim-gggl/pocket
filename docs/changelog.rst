Changelog
=========

All notable changes to Super Pocket will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[Unreleased]
------------

Features planned for future releases:

* Additional cheatsheets (Git, Docker, Python, Bash, Regex)
* Template validation in CLI
* Interactive template creation wizard
* Web-based template browser
* More PDF output formats and options
* Image optimization tools
* Configuration file support
* Plugin system for extensions

[1.0.1] - 2025-11-11
--------------------

Current release.

Added
~~~~~

* Comprehensive Sphinx documentation
* Read the Docs integration
* Complete API documentation
* User guides and tutorials
* Testing documentation
* Contribution guidelines

Changed
~~~~~~~

* Improved README with better examples
* Enhanced project structure documentation

[1.0.0] - 2025-01-15
--------------------

Initial stable release.

Added
~~~~~

**Core Features:**

* Unified CLI interface for all tools
* Backward-compatible standalone commands
* Rich terminal output with colors and formatting
* Comprehensive error handling

**Markdown Tools:**

* Terminal markdown rendering with syntax highlighting
* Support for all standard markdown elements
* Code block syntax highlighting
* Rich text formatting (bold, italic, links)
* Table rendering

**Project Export:**

* Export entire projects to single Markdown files
* Directory tree visualization
* File content extraction with syntax highlighting
* Pattern-based file exclusion
* Configurable output formatting

**Agent Templates:**

* ``agent_maker.md`` - Agent creation assistant
* ``unit_tests_agent.md`` - Unit test generator
* ``agents_template_maker.md`` - AGENTS.md template
* ``job_assistant_agent.md`` - Job search assistant

**Cheatsheets:**

* ``SQL.md`` - SQL reference guide

**PDF Tools:**

* Markdown to PDF conversion
* Text to PDF conversion
* Syntax highlighting preservation
* Custom formatting options

**Web Utilities:**

* Favicon generation from images
* Multiple size support
* Format conversion (PNG, JPG, GIF to ICO)

**Development:**

* Comprehensive test suite (20+ tests)
* 80%+ code coverage
* Type hints throughout codebase
* Black and Ruff for code quality

**Documentation:**

* Detailed README
* Usage examples
* Command reference
* API documentation

[0.2.0] - 2024-12-20
--------------------

Beta release with major feature additions.

Added
~~~~~

* PDF conversion tools
* Web utilities (favicon generation)
* Job search utilities
* Additional agent templates
* More comprehensive tests
* CI/CD pipeline

Changed
~~~~~~~

* Improved CLI organization
* Better error messages
* Enhanced output formatting

Fixed
~~~~~

* Unicode handling in markdown renderer
* Path handling on Windows
* Template discovery issues

[0.1.0] - 2024-11-15
--------------------

Initial alpha release.

Added
~~~~~

* Basic markdown rendering
* Project export functionality
* Initial template system
* Basic CLI interface
* Core test suite

Migration Guides
----------------

Migrating to 1.0.0 from 0.x
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Breaking Changes:**

None - version 1.0.0 maintains backward compatibility with 0.x releases.

**Recommended Updates:**

1. Update to new unified CLI (optional):

   .. code-block:: bash

      # Old
      markd README.md

      # New (both work)
      pocket markdown render README.md
      markd README.md  # Still supported

2. Use new template management:

   .. code-block:: bash

      # Initialize templates
      pocket templates init

3. Install optional dependencies as needed:

   .. code-block:: bash

      pip install pocket[all]

Deprecation Notices
-------------------

None currently. All features in 1.0.1 are supported and maintained.

Version Support
---------------

+----------+----------------+------------------+
| Version  | Status         | Support Until    |
+==========+================+==================+
| 1.0.x    | Stable         | Active           |
+----------+----------------+------------------+
| 0.2.x    | Maintenance    | 2025-06-01       |
+----------+----------------+------------------+
| 0.1.x    | Unsupported    | 2024-12-31       |
+----------+----------------+------------------+

Changelog Categories
--------------------

* **Added** - New features
* **Changed** - Changes in existing functionality
* **Deprecated** - Soon-to-be removed features
* **Removed** - Removed features
* **Fixed** - Bug fixes
* **Security** - Security improvements

Contributing to Changelog
--------------------------

When submitting changes:

1. Add entry to ``[Unreleased]`` section
2. Use appropriate category (Added, Changed, etc.)
3. Write clear, concise descriptions
4. Include issue/PR references
5. Follow existing format

Example entry:

.. code-block:: text

   [Unreleased]
   ------------

   Added
   ~~~~~

   * JSON export format for projects (#123)
   * Docker cheatsheet (#124)

   Fixed
   ~~~~~

   * Unicode handling in Windows (#125)

See Also
--------

* `Keep a Changelog <https://keepachangelog.com/>`_ - Changelog format
* `Semantic Versioning <https://semver.org/>`_ - Versioning scheme
* :doc:`contributing` - How to contribute
