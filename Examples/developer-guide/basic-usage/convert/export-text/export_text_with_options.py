import os
from groupdocs.markdown import License, MarkdownConverter, ConvertOptions

def export_text_with_options():
    """Convert an XML/text file to Markdown using the instance API with heading offset."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Open the text file with a context manager
    with MarkdownConverter("llms-tech.xml") as converter:
        # Step 3: Configure conversion options
        options = ConvertOptions()
        options.heading_level_offset = 1  # shift all headings down one level

        # Step 

        # Step 4: Convert and save the Markdown output
        converter.convert("export-text-options.md", convert_options=options)

if __name__ == "__main__":
    export_text_with_options()