import os
from groupdocs.markdown import License, MarkdownConverter

def export_ebook_to_markdown():
    """Convert an EPUB eBook to Markdown using the static one-liner API."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Convert EPUB to a Markdown string in one call
    markdown = MarkdownConverter.to_markdown("business-plan.epub")

    # Step 3: Or save the conversion result directly to a file
    MarkdownConverter.to_file("business-plan.epub", "export-ebook.md")

if __name__ == "__main__":
    export_ebook_to_markdown()