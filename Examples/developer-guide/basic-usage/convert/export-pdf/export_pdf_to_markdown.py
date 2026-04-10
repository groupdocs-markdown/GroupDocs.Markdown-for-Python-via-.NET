import os
from groupdocs.markdown import License, MarkdownConverter

def export_pdf_to_markdown():
    """Convert a PDF document to Markdown using the static one-liner API."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Convert PDF to a Markdown string in one call
    markdown = MarkdownConverter.to_markdown("business-plan.pdf")

    # Step 3: Or save the conversion result directly to a file
    MarkdownConverter.to_file("business-plan.pdf", "export-pdf.md")

if __name__ == "__main__":
    export_pdf_to_markdown()