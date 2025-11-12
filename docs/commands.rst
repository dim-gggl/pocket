Commands Reference
==================

Complete reference for all Super Pocket CLI commands.

Global Options
--------------

These options are available for all commands:

.. code-block:: bash

   pocket [OPTIONS] COMMAND [ARGS]...

Options:

* ``--version`` - Show version and exit
* ``--help`` - Show help message and exit

Markdown Commands
-----------------

Tools for rendering and working with Markdown files.

pocket markdown render
~~~~~~~~~~~~~~~~~~~~~~

Render a Markdown file in the terminal with beautiful formatting.

**Usage:**

.. code-block:: bash

   pocket markdown render [OPTIONS] FILE

**Arguments:**

* ``FILE`` - Path to the Markdown file to render (required)

**Options:**

* ``--help`` - Show help message

**Examples:**

.. code-block:: bash

   # Render README file
   pocket markdown render README.md

   # Render any markdown file
   pocket markdown render docs/guide.md

**Standalone Command:**

.. code-block:: bash

   markd README.md

Project Commands
----------------

Tools for exporting and managing project files.

pocket project to-file
~~~~~~~~~~~~~~~~~~~~~~

Export an entire project directory to a single Markdown file.

**Usage:**

.. code-block:: bash

   pocket project to-file [OPTIONS]

**Options:**

* ``-p, --path TEXT`` - Project directory path (default: current directory)
* ``-o, --output TEXT`` - Output file name (default: <project_name>-1-file.md)
* ``-e, --exclude TEXT`` - Comma-separated list of files/directories to exclude
* ``--help`` - Show help message

**Examples:**

.. code-block:: bash

   # Export current directory
   pocket project to-file

   # Export specific project
   pocket project to-file -p /path/to/project

   # Custom output file
   pocket project to-file -o my-export.md

   # Exclude directories
   pocket project to-file -e "node_modules,dist,venv"

   # Exclude multiple patterns
   pocket project to-file -e ".git,*.pyc,__pycache__"

**Output Format:**

The generated file includes:

* Project name and metadata
* Directory structure tree
* File contents with syntax highlighting
* Proper section headers

**Standalone Command:**

.. code-block:: bash

   project to-file -p . -o output.md

Templates Commands
------------------

Manage AI agent templates and development cheatsheets.

pocket templates list
~~~~~~~~~~~~~~~~~~~~~

List all available templates and cheatsheets.

**Usage:**

.. code-block:: bash

   pocket templates list [OPTIONS]

**Options:**

* ``-t, --type TEXT`` - Filter by type: "templates", "cheatsheets", or "all" (default: all)
* ``--help`` - Show help message

**Examples:**

.. code-block:: bash

   # List everything
   pocket templates list

   # List only templates
   pocket templates list -t templates

   # List only cheatsheets
   pocket templates list -t cheatsheets

pocket templates view
~~~~~~~~~~~~~~~~~~~~~

View the contents of a specific template or cheatsheet.

**Usage:**

.. code-block:: bash

   pocket templates view [OPTIONS] NAME

**Arguments:**

* ``NAME`` - Name of the template or cheatsheet (required)

**Options:**

* ``-t, --type TEXT`` - Type: "template" or "cheatsheet" (default: auto-detect)
* ``--help`` - Show help message

**Examples:**

.. code-block:: bash

   # View template (auto-detected)
   pocket templates view unit_tests_agent

   # View cheatsheet explicitly
   pocket templates view SQL -t cheatsheet

   # View any template
   pocket templates view agent_maker

pocket templates copy
~~~~~~~~~~~~~~~~~~~~~

Copy a template or cheatsheet to your project.

**Usage:**

.. code-block:: bash

   pocket templates copy [OPTIONS] NAME

**Arguments:**

* ``NAME`` - Name of the template or cheatsheet to copy (required)

**Options:**

* ``-o, --output TEXT`` - Output directory path (default: current directory)
* ``-t, --type TEXT`` - Type: "template" or "cheatsheet" (default: auto-detect)
* ``--help`` - Show help message

**Examples:**

.. code-block:: bash

   # Copy to current directory
   pocket templates copy unit_tests_agent

   # Copy to specific directory
   pocket templates copy unit_tests_agent -o .agents/

   # Copy cheatsheet
   pocket templates copy SQL -t cheatsheet -o ./docs/

pocket templates init
~~~~~~~~~~~~~~~~~~~~~

Initialize an agent templates directory with all available templates.

**Usage:**

.. code-block:: bash

   pocket templates init [OPTIONS]

**Options:**

* ``-o, --output TEXT`` - Output directory path (default: .agents/)
* ``--help`` - Show help message

**Examples:**

.. code-block:: bash

   # Initialize in default location (.agents/)
   pocket templates init

   # Initialize in custom location
   pocket templates init -o ./my-agents/

   # Initialize in project subdirectory
   pocket templates init -o ./config/agents/

PDF Commands
------------

Convert text and Markdown files to PDF format.

.. note::
   Requires ``pocket[pdf]`` optional dependencies.

pocket pdf convert
~~~~~~~~~~~~~~~~~~

Convert a text or Markdown file to PDF.

**Usage:**

.. code-block:: bash

   pocket pdf convert [OPTIONS] INPUT

**Arguments:**

* ``INPUT`` - Path to input file (required)

**Options:**

* ``-o, --output TEXT`` - Output PDF file path (required)
* ``--help`` - Show help message

**Examples:**

.. code-block:: bash

   # Convert markdown to PDF
   pocket pdf convert document.md -o document.pdf

   # Convert text file
   pocket pdf convert notes.txt -o notes.pdf

   # Convert with custom output path
   pocket pdf convert README.md -o ~/Documents/readme.pdf

**Supported Input Formats:**

* Markdown (.md, .markdown)
* Plain text (.txt)

**Standalone Command:**

.. code-block:: bash

   conv-to-pdf document.md output.pdf

Web Commands
------------

Web utilities for generating favicons and other web assets.

.. note::
   Requires ``pocket[web]`` optional dependencies.

pocket web favicon
~~~~~~~~~~~~~~~~~~

Generate a favicon from an image file.

**Usage:**

.. code-block:: bash

   pocket web favicon [OPTIONS] INPUT

**Arguments:**

* ``INPUT`` - Path to input image file (required)

**Options:**

* ``-o, --output TEXT`` - Output .ico file path (default: favicon.ico)
* ``--size INTEGER`` - Favicon size in pixels (default: 16)
* ``--help`` - Show help message

**Examples:**

.. code-block:: bash

   # Generate favicon with defaults
   pocket web favicon logo.png

   # Specify output path
   pocket web favicon logo.png -o static/favicon.ico

   # Custom size
   pocket web favicon logo.png -o favicon.ico --size 32

**Supported Input Formats:**

* PNG
* JPG/JPEG
* GIF
* BMP

**Standalone Command:**

.. code-block:: bash

   flavicon logo.png -o favicon.ico

Command Cheat Sheet
-------------------

Quick reference table:

.. list-table::
   :widths: 30 40 30
   :header-rows: 1

   * - Command
     - Description
     - Standalone
   * - ``pocket markdown render``
     - Render markdown in terminal
     - ``markd``
   * - ``pocket project to-file``
     - Export project to file
     - ``project to-file``
   * - ``pocket templates list``
     - List templates/cheatsheets
     - N/A
   * - ``pocket templates view``
     - View template/cheatsheet
     - N/A
   * - ``pocket templates copy``
     - Copy template to project
     - N/A
   * - ``pocket templates init``
     - Initialize templates directory
     - N/A
   * - ``pocket pdf convert``
     - Convert to PDF
     - ``conv-to-pdf``
   * - ``pocket web favicon``
     - Generate favicon
     - ``flavicon``

Common Patterns
---------------

Working with Multiple Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Process multiple markdown files
   for file in *.md; do
       pocket markdown render "$file"
   done

   # Export multiple projects
   for dir in projects/*/; do
       pocket project to-file -p "$dir" -o "${dir%/}-export.md"
   done

Using Output Redirection
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Save rendered output
   pocket markdown render README.md > rendered.txt

   # Export to stdout
   pocket project to-file -o - > project.md

Combining with Other Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Export and search
   pocket project to-file -o - | grep "TODO"

   # Convert and view PDF
   pocket pdf convert docs.md -o docs.pdf && open docs.pdf

   # Generate favicon and verify
   pocket web favicon logo.png && file favicon.ico

Exit Codes
----------

Super Pocket commands use standard Unix exit codes:

* ``0`` - Success
* ``1`` - General error
* ``2`` - Command line usage error
* Other codes may indicate specific errors

Environment Variables
---------------------

Currently, Super Pocket does not use environment variables for configuration. This may be added in future versions.

See Also
--------

* :doc:`quickstart` - Getting started guide
* :doc:`templates` - Templates and cheatsheets details
* :doc:`api` - API documentation
* :doc:`contributing` - Contributing to Super Pocket
