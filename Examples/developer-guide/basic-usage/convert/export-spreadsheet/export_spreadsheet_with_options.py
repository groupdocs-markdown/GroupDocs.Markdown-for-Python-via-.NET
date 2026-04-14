import os
from groupdocs.markdown import License, MarkdownConverter, ConvertOptions

def export_spreadsheet_with_options():
    """Convert an Excel spreadsheet to Markdown with column/row limits and heading offset."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Open the spreadsheet with a context manager
    with MarkdownConverter("cost-analysis.xlsx") as converter:
        # Step 3: Configure spreadsheet-specific conversion options
        options = ConvertOptions()
        options.max_columns = 10   # limit to first 10 columns
        options.max_rows = 100     # limit to first 100 data rows per sheet
        options.heading_level_offset = 1  # shift headings down one level

        # Step 4: Convert and save the Markdown output
        converter.convert("export-spreadsheet-instance.md", convert_options=options)

if __name__ == "__main__":
    export_spreadsheet_with_options()