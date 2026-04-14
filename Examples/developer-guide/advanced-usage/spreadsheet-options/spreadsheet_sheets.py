from groupdocs.markdown import MarkdownConverter, ConvertOptions

def spreadsheet_sheets():
    """Convert a workbook with custom sheet separators and hidden sheet filtering."""

    # Step 1: Configure sheet separator and hidden sheet behavior
    options = ConvertOptions()
    options.sheet_separator = "\n---\n"      # horizontal rule between worksheets
    options.include_hidden_sheets = False    # skip hidden worksheets (default)

    # Step 2: Open the workbook with a context manager
    with MarkdownConverter("cost-analysis.xlsx") as converter:
        # Step 3: Convert and save the Markdown output
        converter.convert("spreadsheet-sheets.md", convert_options=options)

if __name__ == "__main__":
    spreadsheet_sheets()