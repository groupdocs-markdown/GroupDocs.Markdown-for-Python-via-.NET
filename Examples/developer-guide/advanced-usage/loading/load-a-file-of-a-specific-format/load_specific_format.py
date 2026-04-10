from groupdocs.markdown import MarkdownConverter, LoadOptions, FileFormat

def load_specific_format():
    """Load a file with an explicitly specified format, skipping auto-detection."""

    # Step 1: Create load options with the explicit file format
    load_options = LoadOptions(FileFormat.XLSX)

    # Step 2: Open the file with load options using keyword argument
    with MarkdownConverter("cost-analysis.xlsx", load_options=load_options) as converter:
        # Step 3: Convert and save the Markdown output
        converter.convert("load-specific-format.md")

if __name__ == "__main__":
    load_specific_format()