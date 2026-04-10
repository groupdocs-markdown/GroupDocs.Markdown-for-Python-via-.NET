import os
from groupdocs.markdown import License, MarkdownConverter, ConvertOptions, ExportImagesToFileSystemStrategy

def export_pdf_with_options():
    """Convert a PDF to Markdown using the instance API with image export and heading offset."""

    # Step 1: Apply the license (optional for evaluation)
    if os.path.exists("GroupDocs.Markdown.lic"):
        License.set_("GroupDocs.Markdown.lic")

    # Step 2: Open the PDF document with a context manager
    with MarkdownConverter("business-plan.pdf") as converter:
        # Step 3: Configure the image export strategy to save images to disk
        strategy = ExportImagesToFileSystemStrategy("images")
        strategy.images_relative_path = "images"

        # Step 4: Set conversion options
        options = ConvertOptions()
        options.image_export_strategy = strategy
        options.heading_level_offset = 1  # shift all headings down one level

        # Step 

        # Step 5: Convert and save the Markdown output
        converter.convert("export-pdf-options.md", convert_options=options)

if __name__ == "__main__":
    export_pdf_with_options()