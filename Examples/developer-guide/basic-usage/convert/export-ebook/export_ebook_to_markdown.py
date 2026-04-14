import os
from groupdocs.markdown import License, MarkdownConverter

def export_ebook_to_markdown():
    """Convert an EPUB eBook to Markdown using the static one-liner API."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Convert the EPUB directly to a Markdown file
    MarkdownConverter.to_file("business-plan.epub", "export-ebook-static.md")

if __name__ == "__main__":
    export_ebook_to_markdown()