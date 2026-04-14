import os
from groupdocs.markdown import License, MarkdownConverter

def export_pdf_to_markdown():
    """Convert a PDF document to Markdown using the static one-liner API."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Convert the PDF directly to a Markdown file
    MarkdownConverter.to_file("business-plan.pdf", "export-pdf-static.md")

if __name__ == "__main__":
    export_pdf_to_markdown()