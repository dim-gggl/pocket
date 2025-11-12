API Reference
=============

Complete API documentation for Super Pocket modules.

This page provides detailed API documentation for all public modules, classes, and functions
in Super Pocket. Use this as a reference when using Super Pocket programmatically or extending its functionality.

Core Module
-----------

.. automodule:: pocket
   :members:
   :undoc-members:
   :show-inheritance:

CLI Module
----------

Command-line interface implementation.

.. automodule:: pocket.cli
   :members:
   :undoc-members:
   :show-inheritance:

Markdown Module
---------------

Markdown rendering and processing tools.

.. automodule:: pocket.markdown
   :members:
   :undoc-members:
   :show-inheritance:

markdown.renderer
~~~~~~~~~~~~~~~~~

.. automodule:: pocket.markdown.renderer
   :members:
   :undoc-members:
   :show-inheritance:

Project Module
--------------

Project export and management tools.

.. automodule:: pocket.project
   :members:
   :undoc-members:
   :show-inheritance:

project.to_file
~~~~~~~~~~~~~~~

.. automodule:: pocket.project.to_file
   :members:
   :undoc-members:
   :show-inheritance:

PDF Module
----------

PDF conversion tools.

.. note::
   Requires ``pocket[pdf]`` optional dependencies.

.. automodule:: pocket.pdf
   :members:
   :undoc-members:
   :show-inheritance:

pdf.converter
~~~~~~~~~~~~~

.. automodule:: pocket.pdf.converter
   :members:
   :undoc-members:
   :show-inheritance:

Web Module
----------

Web utilities including favicon generation.

.. note::
   Requires ``pocket[web]`` optional dependencies.

.. automodule:: pocket.web
   :members:
   :undoc-members:
   :show-inheritance:

web.favicon
~~~~~~~~~~~

.. automodule:: pocket.web.favicon
   :members:
   :undoc-members:
   :show-inheritance:

web.job_search
~~~~~~~~~~~~~~

.. automodule:: pocket.web.job_search
   :members:
   :undoc-members:
   :show-inheritance:

Templates Module
----------------

Agent templates and cheatsheets management.

.. automodule:: pocket.templates_and_cheatsheets
   :members:
   :undoc-members:
   :show-inheritance:

templates_and_cheatsheets.cli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: pocket.templates_and_cheatsheets.cli
   :members:
   :undoc-members:
   :show-inheritance:

templates_and_cheatsheets.validator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: pocket.templates_and_cheatsheets.validator
   :members:
   :undoc-members:
   :show-inheritance:

Using the API
-------------

Programmatic Usage
~~~~~~~~~~~~~~~~~~

You can use Super Pocket's modules (imported via the ``pocket`` package) programmatically in your Python code:

Markdown Rendering Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from pocket.markdown.renderer import render_markdown

   # Render a markdown file
   render_markdown('README.md')

   # Process markdown content
   content = "# Hello World\n\nThis is **bold** text."
   render_markdown(content, from_string=True)

Project Export Example
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from pocket.project.to_file import export_project

   # Export a project
   export_project(
       project_path='/path/to/project',
       output_file='export.md',
       exclude=['node_modules', '.git']
   )

Templates Management Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from pocket.templates_and_cheatsheets.cli import (
       list_templates,
       view_template,
       copy_template
   )

   # List available templates
   templates = list_templates(type='templates')

   # View template content
   content = view_template('unit_tests_agent')

   # Copy template to location
   copy_template('unit_tests_agent', output_path='.agents/')

PDF Conversion Example
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from pocket.pdf.converter import convert_to_pdf

   # Convert markdown to PDF
   convert_to_pdf(
       input_file='document.md',
       output_file='document.pdf'
   )

Favicon Generation Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from pocket.web.favicon import generate_favicon

   # Generate favicon from image
   generate_favicon(
       input_image='logo.png',
       output_path='favicon.ico',
       size=16
   )

Error Handling
~~~~~~~~~~~~~~

All Super Pocket functions raise appropriate exceptions on errors:

.. code-block:: python

   from pocket.markdown.renderer import render_markdown

   try:
       render_markdown('nonexistent.md')
   except FileNotFoundError as e:
       print(f"File not found: {e}")
   except ValueError as e:
       print(f"Invalid input: {e}")

Common Exceptions
^^^^^^^^^^^^^^^^^

* ``FileNotFoundError`` - File or directory not found
* ``ValueError`` - Invalid parameter value
* ``IOError`` - I/O operation failed
* ``PermissionError`` - Insufficient permissions

Type Hints
~~~~~~~~~~

Super Pocket uses type hints throughout the codebase for better IDE support:

.. code-block:: python

   from typing import Optional, List
   from pathlib import Path

   def export_project(
       project_path: str | Path,
       output_file: str | Path,
       exclude: Optional[List[str]] = None
   ) -> None:
       """Export project to file."""
       pass

Configuration
~~~~~~~~~~~~~

Some modules accept configuration options:

.. code-block:: python

   from pocket.markdown.renderer import MarkdownRenderer

   # Create custom renderer
   renderer = MarkdownRenderer(
       theme='dark',
       width=100,
       show_links=True
   )

   renderer.render('document.md')

Extending Super Pocket
----------------------

Custom Renderers
~~~~~~~~~~~~~~~~

Extend the markdown renderer:

.. code-block:: python

   from pocket.markdown.renderer import MarkdownRenderer

   class CustomRenderer(MarkdownRenderer):
       def render_heading(self, text: str, level: int) -> str:
           # Custom heading rendering
           return f"{'#' * level} {text.upper()}\n"

Custom Exporters
~~~~~~~~~~~~~~~~

Create custom project exporters:

.. code-block:: python

   from pocket.project.to_file import ProjectExporter

   class JSONExporter(ProjectExporter):
       def export(self, project_path: str) -> dict:
           # Export to JSON format
           return {
               'files': self.collect_files(project_path),
               'structure': self.build_tree(project_path)
           }

Plugin System
~~~~~~~~~~~~~

Future versions will support a plugin system for extending functionality.

API Stability
-------------

Version Compatibility
~~~~~~~~~~~~~~~~~~~~~

* **Stable API**: Public functions and classes in this documentation
* **Unstable API**: Private functions (prefixed with ``_``) may change
* **Deprecated**: Marked with deprecation warnings

Semantic Versioning
~~~~~~~~~~~~~~~~~~~

Super Pocket follows semantic versioning:

* **Major** (X.0.0): Breaking API changes
* **Minor** (1.X.0): New features, backward compatible
* **Patch** (1.0.X): Bug fixes, backward compatible

Migration Guides
~~~~~~~~~~~~~~~~

For major version changes, see migration guides in the changelog.

See Also
--------

* :doc:`modules` - Module index
* :doc:`quickstart` - Getting started
* :doc:`contributing` - Contributing code
* :doc:`testing` - Testing guidelines
