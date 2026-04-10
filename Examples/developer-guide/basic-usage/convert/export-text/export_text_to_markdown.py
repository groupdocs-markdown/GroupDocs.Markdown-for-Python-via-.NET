import os
from groupdocs.markdown import License, MarkdownConverter

def export_text_to_markdown():
    """Convert an XML/text file to Markdown using the static one-liner API."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Convert XML to a Markdown string in one call
    markdown = MarkdownConverter.to_markdown("llms-tech.xml")

    # Step 3: Or save the conversion result directly to a file
    MarkdownConverter.to_file("llms-tech.xml", "export-text.md")

if __name__ == "__main__":
    export_text_to_markdown()