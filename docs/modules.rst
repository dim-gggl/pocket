Module Index
============

Complete index of all Super Pocket modules.

This page provides an overview of Super Pocket's module structure and links to detailed
API documentation for each module.

Package Structure
-----------------

.. code-block:: text

   pocket/
   ├── __init__.py
   ├── cli.py                          # Main CLI interface
   ├── markdown/                       # Markdown tools
   │   ├── __init__.py
   │   └── renderer.py
   ├── project/                        # Project export tools
   │   ├── __init__.py
   │   └── to_file.py
   ├── pdf/                            # PDF conversion tools
   │   ├── __init__.py
   │   └── converter.py
   ├── web/                            # Web utilities
   │   ├── __init__.py
   │   ├── favicon.py
   │   └── job_search.py
   └── templates_and_cheatsheets/      # Templates management
       ├── __init__.py
       ├── cli.py
       ├── validator.py
       ├── templates/                  # Agent templates
       │   └── __init__.py
       └── cheatsheets/                # Development cheatsheets
           └── __init__.py

Module Descriptions
-------------------

Core Modules
~~~~~~~~~~~~

pocket
^^^^^^

Main package initialization and public API.

.. autosummary::
   :toctree: _autosummary

   pocket

pocket.cli
^^^^^^^^^^

Command-line interface implementation using Click framework.

**Key Components:**

* Main CLI group
* Subcommand groups for each tool category
* Option parsing and validation
* Error handling and user feedback

.. autosummary::
   :toctree: _autosummary

   pocket.cli

Markdown Modules
~~~~~~~~~~~~~~~~

pocket.markdown
^^^^^^^^^^^^^^^

Markdown rendering and processing functionality.

.. autosummary::
   :toctree: _autosummary

   pocket.markdown
   pocket.markdown.renderer

**Features:**

* Terminal markdown rendering
* Syntax highlighting
* Rich text formatting
* Link handling

Project Modules
~~~~~~~~~~~~~~~

pocket.project
^^^^^^^^^^^^^^

Project export and analysis tools.

.. autosummary::
   :toctree: _autosummary

   pocket.project
   pocket.project.to_file

**Features:**

* Directory tree generation
* File content extraction
* Pattern-based exclusion
* Markdown formatting

PDF Modules
~~~~~~~~~~~

pocket.pdf
^^^^^^^^^^

PDF conversion utilities.

.. note::
   Requires ``pocket[pdf]`` optional dependencies.

.. autosummary::
   :toctree: _autosummary

   pocket.pdf
   pocket.pdf.converter

**Features:**

* Markdown to PDF conversion
* Text to PDF conversion
* Formatting preservation
* Font and style management

Web Modules
~~~~~~~~~~~

pocket.web
^^^^^^^^^^

Web utilities and asset generation.

.. note::
   Requires ``pocket[web]`` optional dependencies.

.. autosummary::
   :toctree: _autosummary

   pocket.web
   pocket.web.favicon
   pocket.web.job_search

**Features:**

* Favicon generation from images
* Image processing and resizing
* Format conversion
* Job search utilities

Templates Modules
~~~~~~~~~~~~~~~~~

pocket.templates_and_cheatsheets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Agent templates and cheatsheets management.

.. autosummary::
   :toctree: _autosummary

   pocket.templates_and_cheatsheets
   pocket.templates_and_cheatsheets.cli
   pocket.templates_and_cheatsheets.validator
   pocket.templates_and_cheatsheets.templates
   pocket.templates_and_cheatsheets.cheatsheets

**Features:**

* Template discovery and listing
* Content viewing and rendering
* Template copying and initialization
* Validation and verification

Module Dependencies
-------------------

Core Dependencies
~~~~~~~~~~~~~~~~~

Required for all functionality:

* ``click>=8.3.0`` - CLI framework
* ``rich>=14.1.0`` - Terminal formatting
* ``python-dotenv>=1.2.1`` - Environment configuration
* ``requests>=2.32.5`` - HTTP requests

Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~

**PDF Module:**

* ``fpdf2>=2.7.0``
* ``markdown-pdf>=1.0.0``

**Web Module:**

* ``Pillow>=10.0.0``

**Development:**

* ``pytest>=7.0.0``
* ``pytest-cov>=3.0.0``
* ``black>=23.0.0``
* ``ruff>=0.1.0``

Module Import Examples
----------------------

Importing Modules
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Import main package
   import pocket

   # Import specific modules
   from super_pocket.markdown import renderer
   from super_pocket.project import to_file
   from super_pocket.templates_and_cheatsheets import cli as templates_cli

   # Import specific functions
   from super_pocket.markdown.renderer import render_markdown
   from super_pocket.project.to_file import export_project

Using Submodules
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Access markdown functionality
   from super_pocket import markdown
   markdown.renderer.render_markdown('README.md')

   # Access project tools
   from super_pocket import project
   project.to_file.export_project('.')

   # Access templates
   from super_pocket import templates_and_cheatsheets
   templates_and_cheatsheets.cli.list_templates()

Module Guidelines
-----------------

Public vs Private
~~~~~~~~~~~~~~~~~

* **Public API**: Functions and classes without underscore prefix
* **Private API**: Functions and classes with underscore prefix (``_function``)
* **Internal**: Modules in ``_internal`` directories

Only use the public API in your code, as private APIs may change without notice.

Import Recommendations
~~~~~~~~~~~~~~~~~~~~~~

Preferred import styles:

.. code-block:: python

   # Good: Specific imports
   from super_pocket.markdown.renderer import render_markdown

   # Good: Module import
   from super_pocket import markdown

   # Avoid: Star imports
   from super_pocket.markdown import *  # Don't do this

Type Hints
~~~~~~~~~~

All modules use type hints:

.. code-block:: python

   from typing import Optional, List
   from pathlib import Path

   def function(
       path: str | Path,
       options: Optional[List[str]] = None
   ) -> bool:
       """Function with type hints."""
       pass

Module Documentation Standards
-------------------------------

All modules follow these documentation standards:

Docstring Format
~~~~~~~~~~~~~~~~

Google-style docstrings:

.. code-block:: python

   def function(param1: str, param2: int) -> bool:
       """Brief description.

       Longer description explaining the function's purpose
       and behavior in more detail.

       Args:
           param1: Description of param1
           param2: Description of param2

       Returns:
           Description of return value

       Raises:
           ValueError: When input is invalid
           FileNotFoundError: When file doesn't exist

       Examples:
           >>> function("test", 42)
           True
       """
       pass

Module Docstrings
~~~~~~~~~~~~~~~~~

.. code-block:: python

   """Module name and brief description.

   Longer description of module purpose, functionality,
   and usage patterns.

   Example:
       Basic usage example::

           from super_pocket.module import function
           result = function()

   Attributes:
       CONSTANT: Description of module constant

   Note:
       Any important notes or warnings
   """

See Also
--------

* :doc:`api` - Complete API reference
* :doc:`contributing` - Contribution guidelines
* :doc:`testing` - Testing documentation

Full Module Index
-----------------

.. autosummary::
   :toctree: _autosummary
   :recursive:

   pocket
