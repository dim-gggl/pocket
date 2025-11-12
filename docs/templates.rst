Templates & Cheatsheets
=======================

Super Pocket includes a curated collection of AI agent templates and development cheatsheets
to boost your productivity.

Overview
--------

The templates system provides:

* **Agent Templates**: Pre-configured AI agent setups for common development tasks
* **Cheatsheets**: Quick reference guides for various technologies and tools
* **Easy Management**: Simple CLI for viewing, copying, and managing templates

Agent Templates
---------------

Agent templates are Markdown files containing configuration and instructions for AI coding assistants.
They help maintain consistency across projects and streamline AI-assisted development workflows.

Available Templates
~~~~~~~~~~~~~~~~~~~

agent_maker.md
^^^^^^^^^^^^^^

An agent configuration designed to help you create new AI agent templates.

**Use cases:**

* Creating custom agent configurations
* Designing project-specific AI assistants
* Templating agent behaviors

**Usage:**

.. code-block:: bash

   pocket templates view agent_maker
   pocket templates copy agent_maker -o .agents/

unit_tests_agent.md
^^^^^^^^^^^^^^^^^^^

Comprehensive configuration for generating unit tests with proper coverage and best practices.

**Use cases:**

* Automated test generation
* Test coverage improvement
* TDD workflow assistance

**Features:**

* Generates comprehensive test suites
* Follows testing best practices
* Includes edge cases and error handling
* Supports multiple testing frameworks

**Usage:**

.. code-block:: bash

   pocket templates view unit_tests_agent
   pocket templates copy unit_tests_agent -o .agents/

agents_template_maker.md
^^^^^^^^^^^^^^^^^^^^^^^^^

Template for creating AGENTS.md files that document your project's AI agent configurations.

**Use cases:**

* Documenting agent setups
* Project onboarding
* Team collaboration on AI workflows

**Usage:**

.. code-block:: bash

   pocket templates view agents_template_maker
   pocket templates copy agents_template_maker -o ./docs/

job_assistant_agent.md
^^^^^^^^^^^^^^^^^^^^^^

AI assistant configuration for job search and application processes.

**Use cases:**

* Resume optimization
* Cover letter generation
* Interview preparation
* Job application tracking

**Usage:**

.. code-block:: bash

   pocket templates view job_assistant_agent
   pocket templates copy job_assistant_agent -o .

Development Cheatsheets
-----------------------

Quick reference guides for common development tasks and technologies.

Available Cheatsheets
~~~~~~~~~~~~~~~~~~~~~

SQL.md
^^^^^^

Comprehensive SQL reference covering:

* Basic queries (SELECT, INSERT, UPDATE, DELETE)
* Joins (INNER, LEFT, RIGHT, FULL)
* Aggregate functions
* Subqueries and CTEs
* Window functions
* Database design patterns

**Usage:**

.. code-block:: bash

   pocket templates view SQL -t cheatsheet
   pocket templates copy SQL -t cheatsheet -o ./docs/

Managing Templates
------------------

Listing Templates
~~~~~~~~~~~~~~~~~

View all available templates and cheatsheets:

.. code-block:: bash

   # List everything
   pocket templates list

   # List only templates
   pocket templates list -t templates

   # List only cheatsheets
   pocket templates list -t cheatsheets

The output shows:

* Template/cheatsheet names
* Descriptions
* Categories

Viewing Content
~~~~~~~~~~~~~~~

Preview template content before copying:

.. code-block:: bash

   # View any template
   pocket templates view unit_tests_agent

   # View with type specified
   pocket templates view SQL -t cheatsheet

This displays the full content in your terminal with formatting.

Copying to Your Project
~~~~~~~~~~~~~~~~~~~~~~~

Copy templates to use them in your projects:

.. code-block:: bash

   # Copy to current directory
   pocket templates copy unit_tests_agent

   # Copy to specific location
   pocket templates copy unit_tests_agent -o .agents/

   # Copy with full path
   pocket templates copy agent_maker -o /path/to/project/.agents/

The copied files maintain their original formatting and can be edited as needed.

Initializing Agent Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set up a complete agent templates directory:

.. code-block:: bash

   # Create .agents/ with all templates
   pocket templates init

   # Custom location
   pocket templates init -o ./config/agents/

This creates:

* A dedicated directory for agent templates
* Copies of all available templates
* Organized structure for team sharing

Using Templates in Projects
----------------------------

Agent Configuration Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Initialize Templates:**

   .. code-block:: bash

      pocket templates init

2. **Choose Appropriate Agents:**

   Review available templates and select ones that match your needs.

3. **Customize for Your Project:**

   Edit the copied templates to include project-specific instructions.

4. **Use with AI Assistants:**

   Reference these templates when working with AI coding assistants.

Cheatsheet Workflow
~~~~~~~~~~~~~~~~~~~

1. **View Cheatsheet:**

   .. code-block:: bash

      pocket templates view SQL -t cheatsheet

2. **Copy for Reference:**

   .. code-block:: bash

      pocket templates copy SQL -t cheatsheet -o ./docs/

3. **Keep in Documentation:**

   Include cheatsheets in your project documentation for team reference.

Best Practices
--------------

Template Organization
~~~~~~~~~~~~~~~~~~~~~

* Keep agent templates in a dedicated directory (`.agents/` or `.ai/`)
* Version control your customized templates
* Document your template customizations
* Share templates across team repositories

Customization Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~

When customizing templates:

* Preserve the core structure
* Add project-specific context
* Include relevant examples from your codebase
* Document any modifications

Template Naming
~~~~~~~~~~~~~~~

For custom templates:

* Use descriptive names: ``backend_tdd_agent.md``
* Include scope: ``frontend_component_agent.md``
* Version if needed: ``api_agent_v2.md``

Creating Custom Templates
--------------------------

You can create your own templates following these guidelines:

Template Structure
~~~~~~~~~~~~~~~~~~

.. code-block:: markdown

   # Agent Name

   ## Purpose
   Brief description of what this agent does.

   ## Context
   Background information the agent needs.

   ## Instructions
   Detailed step-by-step instructions.

   ## Examples
   Code examples and usage patterns.

   ## Best Practices
   Guidelines and recommendations.

Adding to Super Pocket
~~~~~~~~~~~~~~~~~~~~~~

To add templates to Super Pocket's collection:

1. Create your template following the structure above
2. Test it thoroughly in real projects
3. Submit a pull request to the Super Pocket repository
4. Include documentation and examples

See :doc:`contributing` for details on contributing templates.

Template File Format
--------------------

Templates are standard Markdown files (`.md`) with:

* Front matter (optional)
* Structured content sections
* Code examples with syntax highlighting
* Links and references

Example Template
~~~~~~~~~~~~~~~~

.. code-block:: markdown

   # Unit Tests Agent

   ## Purpose
   Generate comprehensive unit tests for Python code with pytest.

   ## Instructions

   1. Analyze the code structure
   2. Identify functions and classes to test
   3. Generate tests covering:
      - Happy path scenarios
      - Edge cases
      - Error conditions

   ## Example

   ```python
   def test_addition():
       assert add(2, 3) == 5
       assert add(-1, 1) == 0
   ```

Troubleshooting
---------------

Template Not Found
~~~~~~~~~~~~~~~~~~

If you get a "template not found" error:

.. code-block:: bash

   # List available templates to verify name
   pocket templates list

   # Check spelling and try again
   pocket templates view correct_name

Cannot Copy Template
~~~~~~~~~~~~~~~~~~~~

If copying fails:

.. code-block:: bash

   # Ensure output directory exists
   mkdir -p .agents

   # Try with absolute path
   pocket templates copy unit_tests_agent -o "$(pwd)/.agents/"

Template Display Issues
~~~~~~~~~~~~~~~~~~~~~~~

If templates don't display correctly:

* Ensure your terminal supports Unicode
* Check terminal color settings
* Try a different terminal emulator

Future Additions
----------------

Planned templates and cheatsheets:

Templates
~~~~~~~~~

* ``code_review_agent.md`` - Automated code review
* ``documentation_agent.md`` - Documentation generation
* ``refactoring_agent.md`` - Code refactoring assistance
* ``debugging_agent.md`` - Debugging assistance

Cheatsheets
~~~~~~~~~~~

* ``git.md`` - Git commands and workflows
* ``docker.md`` - Docker and containerization
* ``python.md`` - Python language reference
* ``bash.md`` - Shell scripting
* ``regex.md`` - Regular expressions

Contributing Templates
~~~~~~~~~~~~~~~~~~~~~~

We welcome contributions! See :doc:`contributing` for:

* Template submission guidelines
* Quality standards
* Review process

See Also
--------

* :doc:`commands` - Commands reference
* :doc:`quickstart` - Quick start guide
* :doc:`contributing` - How to contribute templates
* :doc:`api` - API for programmatic access
