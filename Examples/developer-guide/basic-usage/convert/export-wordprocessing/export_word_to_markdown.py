import os
from groupdocs.markdown import License, MarkdownConverter

def export_word_to_markdown():
    """Convert a Word document to Markdown using the static one-liner API."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Convert the Word document directly to a Markdown file
    MarkdownConverter.to_file("business-plan.docx", "export-word-static.md")

if __name__ == "__main__":
    export_word_to_markdown()