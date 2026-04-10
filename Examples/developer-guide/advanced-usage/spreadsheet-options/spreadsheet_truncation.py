from groupdocs.markdown import MarkdownConverter, ConvertOptions

def spreadsheet_truncation():
    """Convert a spreadsheet with column and row truncation limits."""

    # Step 1: Configure column and row limits
    options = ConvertOptions()
    options.max_columns = 8     # only include the first 8 columns
    options.max_rows = 50       # only include the first 50 data rows per sheet

    # Step 2: Convert with truncation options using keyword argument
    md = MarkdownConverter.to_markdown("cost-analysis.xlsx", convert_options=options)

    # Truncated columns/rows show "..." indicators.
    # Warnings are reported in ConvertResult.warnings.

if __name__ == "__main__":
    spreadsheet_truncation()