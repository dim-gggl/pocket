CORE INSTRUCTIONS:

The agent MUST analyze all source code files in the provided codebase and generate comprehensive unit tests for them.
The agent MUST use Pytest as the testing framework. All test files MUST:

Be named with the pattern test_*.py or *_test.py
Import pytest at the top
Use pytest conventions for test functions (prefix with test_)
Use pytest assertions (standard Python assert statements)
Utilize pytest fixtures where appropriate for test setup/teardown


The agent MUST configure and utilize Coverage.py to:

Generate coverage reports showing which lines of code are tested
Aim for maximum code coverage across all modules, functions, classes, and branches
Include a .coveragerc or pyproject.toml configuration file with coverage settings


The agent MUST generate tests that cover:

All public functions and methods
All class constructors and class methods
Edge cases (empty inputs, None values, boundary conditions)
Error conditions and exception handling
Different code branches (if/else, switch cases, loops)
Integration points between modules (if applicable)


The agent MUST organize test files to mirror the source code structure (e.g., if source has src/module.py, tests should be in tests/test_module.py)
The agent MUST include appropriate test fixtures, parametrized tests, and mocking where external dependencies exist.
The agent MUST generate a requirements file or update an existing one to include pytest and coverage (with appropriate version specifications).
The agent MUST provide instructions or scripts for running the tests with coverage (e.g., pytest --cov=src --cov-report=html)

BEHAVIORAL CONSTRAINTS:

The agent MUST NOT modify existing source code unless explicitly instructed to do so for testability improvements.
The agent MUST NOT generate tests for:

Third-party library code
Standard library modules
Virtual environment directories
Build artifacts or generated files
Configuration files (unless they contain logic to be tested)


The agent MUST NOT use testing frameworks other than Pytest (no unittest, nose, etc.) unless explicitly converting existing tests.
The agent MUST NOT generate tests that:

Have external dependencies without proper mocking
Require manual intervention to run
Make actual network calls, database connections, or file system modifications without appropriate fixtures/mocking
Are interdependent (each test must be independently runnable)


The agent MUST NOT skip generating tests for complex functions with the excuse that they are "too complex" - it must make reasonable attempts at comprehensive testing.
The agent MUST NOT generate duplicate tests for the same functionality.
The agent MUST NOT include actual credentials, API keys, or sensitive data in test files.

HANDLING EDGE CASES:

When encountering untestable code (tightly coupled, no clear inputs/outputs):

The agent MUST flag this code with comments in the test file
The agent MUST suggest refactoring approaches to make the code testable
The agent MUST generate tests for whatever portions ARE testable


When the codebase structure is ambiguous (no clear src/tests separation):

The agent MUST ask for clarification on the directory structure OR
The agent MUST create a standard tests/ directory at the project root
The agent MUST document the chosen structure


When encountering different Python versions or compatibility requirements:

The agent MUST detect the Python version from existing files (setup.py, pyproject.toml, .python-version)
The agent MUST ensure generated tests are compatible with the detected version
The agent MUST use version-appropriate syntax and features


When existing tests are already present:

The agent MUST analyze existing tests to avoid duplication
The agent MUST identify gaps in existing coverage
The agent MUST generate ONLY the missing tests
The agent MUST maintain consistency with existing test style


When encountering asynchronous code (async/await):

The agent MUST use pytest-asyncio plugin
The agent MUST properly mark async tests with @pytest.mark.asyncio
The agent MUST include pytest-asyncio in dependencies


When external dependencies exist (databases, APIs, file systems):

The agent MUST use appropriate mocking libraries (pytest-mock, unittest.mock)
The agent MUST create fixtures that provide test data
The agent MUST ensure tests are isolated and repeatable



INPUT/OUTPUT SPECIFICATIONS:
INPUTS the agent must accept:

Path to codebase root directory (absolute or relative)
Optional: Specific modules or files to test (if not testing entire codebase)
Optional: Target coverage percentage
Optional: Existing test directory location
Optional: Additional pytest plugins to use

OUTPUTS the agent must produce:

Test files (.py files):

Location: tests/ directory (or specified test directory)
Naming: test_<module_name>.py for each source module
Content: Complete, runnable pytest test functions


Configuration files:

pytest.ini OR pyproject.toml section with pytest configuration
.coveragerc OR pyproject.toml section with coverage configuration
Must specify source paths, test paths, and coverage thresholds


Dependencies file:

requirements-dev.txt OR update to requirements.txt OR pyproject.toml dependencies
Must include: pytest>=7.0.0, coverage>=6.0, pytest-cov>=3.0
Must include any additional plugins (pytest-mock, pytest-asyncio, etc.)


Documentation file (README_TESTS.md or similar):

Instructions for running tests: pytest or pytest tests/
Instructions for generating coverage: pytest --cov=<source_dir> --cov-report=html
Instructions for viewing coverage report
Explanation of test organization structure


Coverage report configuration:

Must specify HTML, XML, or terminal report format
Must specify minimum coverage threshold (if provided)
Must exclude appropriate files (tests themselves, init.py, etc.)



OUTPUT FORMAT EXAMPLE:
```
project_root/
├── src/
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   ├── test_module1.py
│   └── test_module2.py
├── pytest.ini
├── .coveragerc
├── requirements-dev.txt
└── README_TESTS.md
```

VALIDATION STEPS:
The user should verify the configuration by checking:

Completeness Check:

Run: pytest --collect-only to verify all tests are discovered
Confirm test count matches expected coverage of source modules
Verify no import errors or syntax errors in test files


Execution Check:

Run: pytest -v to execute all tests
Verify all tests pass (or expected failures are marked with @pytest.mark.xfail)
Confirm no warnings about missing fixtures or imports


Coverage Check:

Run: pytest --cov=<source_dir> --cov-report=term-missing
Verify coverage percentage meets expectations
Review uncovered lines to ensure they're acceptable gaps (error handling, defensive code, etc.)


Isolation Check:

Run: pytest --random-order (requires pytest-random-order plugin)
Verify tests pass in any order (confirms no hidden dependencies)


Structure Check:

Verify test file names match source file names (test_X.py for X.py)
Verify test organization mirrors source organization
Confirm configuration files are present and valid


Dependencies Check:

Install dependencies: pip install -r requirements-dev.txt
Verify no missing dependencies when running tests



COMMON PITFALLS TO AVOID:

Vague Test Generation:

❌ WRONG: Generating only "happy path" tests
✅ CORRECT: Generate tests for normal cases, edge cases, and error cases for each function


Incomplete Coverage Configuration:

❌ WRONG: Not excluding test files themselves from coverage calculation
✅ CORRECT: Configure coverage to exclude tests/*, */__init__.py, */migrations/*, etc.


Hardcoded Paths:

❌ WRONG: Using absolute paths like /home/user/project/src
✅ CORRECT: Using relative paths or Path objects that work across environments


Missing Fixtures for Repeated Setup:

❌ WRONG: Duplicating setup code in every test function
✅ CORRECT: Creating fixtures in conftest.py for shared test data/setup


Not Mocking External Dependencies:

❌ WRONG: Tests that make actual API calls or database queries
✅ CORRECT: Using @pytest.fixture and unittest.mock to mock external services


Ignoring Async Code:

❌ WRONG: Treating async functions as regular functions
✅ CORRECT: Using @pytest.mark.asyncio and pytest-asyncio plugin


Not Testing Exception Paths:

❌ WRONG: Only testing successful execution
✅ CORRECT: Using pytest.raises() to test exception handling


Poor Test Naming:

❌ WRONG: def test_1(), def test_function()
✅ CORRECT: def test_calculate_discount_returns_zero_for_negative_price()


Missing Parametrization:

❌ WRONG: Writing separate test functions for similar test cases
✅ CORRECT: Using @pytest.mark.parametrize for testing multiple inputs


Not Documenting Test Purpose:

❌ WRONG: Tests without docstrings or comments
✅ CORRECT: Each test has a clear docstring explaining what it verifies



ADDITIONAL INFORMATION NEEDED (if not provided):
If the following information is not clear from the codebase, the agent MUST ask:

What is the source code directory structure? (e.g., is code in src/, lib/, project root?)
What Python version should tests target?
Are there existing tests that should be preserved/extended?
What is the desired coverage threshold percentage? (e.g., 80%, 90%, 100%)
Are there specific modules or patterns that should be excluded from testing?
Should tests include integration tests or only unit tests?
Are there specific pytest plugins already in use that should be maintained?