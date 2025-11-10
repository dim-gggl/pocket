"""
Tests for PDF converter module.
"""

import pytest
from pathlib import Path


def test_pdf_module_imports():
    """Test that PDF module can be imported."""
    from fancy_tools.pdf import convert_to_pdf, convert_txt_to_pdf, convert_md_to_pdf

    assert callable(convert_to_pdf)
    assert callable(convert_txt_to_pdf)
    assert callable(convert_md_to_pdf)


def test_pdf_converter_file_not_found(temp_dir):
    """Test that converter raises FileNotFoundError for non-existent files."""
    from fancy_tools.pdf.converter import convert_to_pdf

    input_file = temp_dir / "nonexistent.txt"
    output_file = temp_dir / "output.pdf"

    with pytest.raises(FileNotFoundError):
        convert_to_pdf(input_file, output_file)


def test_pdf_converter_unsupported_extension(temp_dir):
    """Test that converter raises ValueError for unsupported file types."""
    from fancy_tools.pdf.converter import convert_to_pdf

    # Create a file with unsupported extension
    input_file = temp_dir / "test.xyz"
    input_file.write_text("test content", encoding='utf-8')
    output_file = temp_dir / "output.pdf"

    with pytest.raises(ValueError, match="Unsupported file extension"):
        convert_to_pdf(input_file, output_file)


# Note: Full conversion tests require optional dependencies (fpdf2, markdown-pdf)
# These are skipped if dependencies are not installed
