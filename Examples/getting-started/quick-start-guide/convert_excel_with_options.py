from groupdocs.markdown import MarkdownConverter, ConvertOptions, MarkdownFlavor

def convert_excel_with_options():
    """Convert an Excel spreadsheet with column/row limits, front matter, and GFM flavor."""

    # Step 1: Configure spreadsheet-specific conversion options
    options = ConvertOptions()
    options.max_columns = 8              # limit to first 8 columns
    options.max_rows = 50                # limit to first 50 data rows
    options.include_front_matter = True  # add YAML metadata block
    options.flavor = MarkdownFlavor.GIT_HUB  # GitHub Flavored Markdown

    # Step 2: Open the spreadsheet with a context manager
    with MarkdownConverter("cost-analysis.xlsx") as converter:
        # Step 3: Convert and save the Markdown output
        converter.convert("quick-start-excel.md", convert_options=options)

if __name__ == "__main__":
    convert_excel_with_options()