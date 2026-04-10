import os
from groupdocs.markdown import License, MarkdownConverter

def export_spreadsheet_to_markdown():
    """Convert an Excel spreadsheet to Markdown using the static one-liner API."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Convert XLSX to a Markdown string in one call
    markdown = MarkdownConverter.to_markdown("cost-analysis.xlsx")

    # Step 3: Or save the conversion result directly to a file
    MarkdownConverter.to_file("cost-analysis.xlsx", "export-spreadsheet.md")

if __name__ == "__main__":
    export_spreadsheet_to_markdown()