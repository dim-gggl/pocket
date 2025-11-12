Quick Start Guide
=================

This guide will help you get started with Super Pocket's main features.

Your First Command
------------------

After :doc:`installation`, let's verify everything works:

.. code-block:: bash

   pocket --help

You should see the main help menu with all available commands.

Markdown Rendering
------------------

Super Pocket can beautifully render Markdown files directly in your terminal with syntax highlighting
and rich formatting.

Basic Usage
~~~~~~~~~~~

.. code-block:: bash

   # Render a markdown file
   pocket markdown render README.md

   # Or use the standalone command
   markd README.md

The rendered output will display in your terminal with:

* Proper heading hierarchy
* Syntax-highlighted code blocks
* Formatted lists and tables
* Links and emphasis

Example Output
~~~~~~~~~~~~~~

Given this markdown file:

.. code-block:: markdown

   # My Project

   ## Features

   - Fast performance
   - Easy to use
   - Well documented

   ## Code Example

   ```python
   def hello():
       print("Hello, World!")
   ```

Super Pocket will render it with beautiful formatting and colors in your terminal.

Project Export
--------------

Export entire projects to a single Markdown file for easy sharing, documentation,
or AI context.

Basic Export
~~~~~~~~~~~~

.. code-block:: bash

   # Export current directory
   pocket project to-file

   # Export specific directory
   pocket project to-file -p /path/to/project

   # Specify output file
   pocket project to-file -o my-project-export.md

Excluding Files
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Exclude specific files/directories
   pocket project to-file -e "node_modules,dist,*.pyc"

   # Multiple exclusions
   pocket project to-file -e "venv,.git,__pycache__"

The exported file will contain:

* Project structure tree
* File contents with syntax highlighting
* Proper formatting for sharing

Agent Templates & Cheatsheets
------------------------------

Super Pocket includes a collection of AI agent templates and development cheatsheets.

Listing Available Items
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # List all templates and cheatsheets
   pocket templates list

   # List only templates
   pocket templates list -t templates

   # List only cheatsheets
   pocket templates list -t cheatsheets

Viewing Templates
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # View a template
   pocket templates view unit_tests_agent

   # View a cheatsheet
   pocket templates view SQL -t cheatsheet

Copying Templates
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Copy template to your project
   pocket templates copy unit_tests_agent -o .agents/

   # Copy to current directory
   pocket templates copy agent_maker -o .

Initializing Agent Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Create .agents directory with all templates
   pocket templates init

   # Create in custom location
   pocket templates init -o ./my-agents/

Available Templates
~~~~~~~~~~~~~~~~~~~

* **agent_maker**: Agent creation assistant configuration
* **unit_tests_agent**: Comprehensive unit test generator
* **agents_template_maker**: Template for AGENTS.md files
* **job_assistant_agent**: Job search and application assistant

Available Cheatsheets
~~~~~~~~~~~~~~~~~~~~~

* **SQL**: SQL commands and queries reference
* More coming soon!

PDF Conversion
--------------

Convert text and Markdown files to PDF documents.

.. note::
   PDF features require the ``pdf`` optional dependencies:

   .. code-block:: bash

      pip install pocket[pdf]

Basic Conversion
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Convert markdown to PDF
   pocket pdf convert document.md -o output.pdf

   # Convert text file to PDF
   pocket pdf convert notes.txt -o notes.pdf

   # Using standalone command
   conv-to-pdf document.md output.pdf

The PDF will be generated with:

* Proper formatting
* Syntax highlighting for code blocks (from Markdown)
* Readable fonts and layout

Web Utilities
-------------

Generate favicons and other web assets.

.. note::
   Web features require the ``web`` optional dependencies:

   .. code-block:: bash

      pip install pocket[web]

Favicon Generation
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate favicon from image
   pocket web favicon logo.png -o favicon.ico

   # Specify custom size
   pocket web favicon logo.png -o favicon.ico --size 32

   # Using standalone command
   flavicon logo.png -o favicon.ico

Supported input formats:

* PNG
* JPG/JPEG
* GIF
* BMP

Common Workflows
----------------

Development Documentation Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # 1. Export project for documentation
   pocket project to-file -o project-snapshot.md

   # 2. Render README in terminal
   pocket markdown render README.md

   # 3. Convert docs to PDF for offline reading
   pocket pdf convert DOCS.md -o docs.pdf

AI-Assisted Development Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # 1. Initialize agent templates
   pocket templates init

   # 2. Export project context for AI
   pocket project to-file -o context.md -e "venv,node_modules"

   # 3. View relevant cheatsheet
   pocket templates view SQL -t cheatsheet

Project Sharing Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # 1. Export entire project
   pocket project to-file -p . -o shared-project.md -e ".git,venv"

   # 2. Convert to PDF for formal sharing
   pocket pdf convert shared-project.md -o project-overview.pdf

   # 3. Create project favicon
   pocket web favicon logo.png -o favicon.ico

Tips and Tricks
---------------

Combining Commands
~~~~~~~~~~~~~~~~~~

Use shell pipes and redirection with Super Pocket commands:

.. code-block:: bash

   # Export and view in pager
   pocket project to-file -o - | less

   # Search in rendered markdown
   pocket markdown render README.md | grep "TODO"

Creating Aliases
~~~~~~~~~~~~~~~~

Add these to your shell configuration (``~/.bashrc`` or ``~/.zshrc``):

.. code-block:: bash

   # Quick markdown rendering
   alias md='pocket markdown render'

   # Quick project export
   alias export='pocket project to-file'

   # View templates quickly
   alias tpl='pocket templates view'

Using with Watch Commands
~~~~~~~~~~~~~~~~~~~~~~~~~

Auto-render on file changes:

.. code-block:: bash

   # Linux/macOS with inotifywait or fswatch
   while true; do
       inotifywait -e modify README.md && pocket markdown render README.md
   done

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

Customize Super Pocket behavior (if supported in future versions):

.. code-block:: bash

   export POCKET_DEFAULT_OUTPUT_DIR=~/exports
   export POCKET_THEME=dark

Next Steps
----------

* :doc:`commands` - Detailed command reference
* :doc:`templates` - Learn more about templates and cheatsheets
* :doc:`api` - API documentation for programmatic use
* :doc:`contributing` - Contribute to Super Pocket

Getting Help
------------

For each command, you can get detailed help:

.. code-block:: bash

   # Main help
   pocket --help

   # Subcommand help
   pocket markdown --help
   pocket project --help
   pocket templates --help

   # Specific command help
   pocket markdown render --help
   pocket project to-file --help

See Also
--------

* :doc:`commands` - Complete command reference
* :doc:`templates` - Templates and cheatsheets guide
* :doc:`contributing` - How to contribute
