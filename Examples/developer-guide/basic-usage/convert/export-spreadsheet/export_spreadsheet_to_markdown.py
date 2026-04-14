import os
from groupdocs.markdown import License, MarkdownConverter

def export_spreadsheet_to_markdown():
    """Convert an Excel spreadsheet to Markdown using the static one-liner API."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Convert the spreadsheet directly to a Markdown file
    MarkdownConverter.to_file("cost-analysis.xlsx", "export-spreadsheet-static.md")

if __name__ == "__main__":
    export_spreadsheet_to_markdown()