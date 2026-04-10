from groupdocs.markdown import MarkdownConverter, ConvertOptions, ExportImagesToFileSystemStrategy

def convert_pdf_with_images():
    """Convert a PDF to Markdown with images exported to a folder on disk."""

    # Step 1: Configure image export with relative paths
    strategy = ExportImagesToFileSystemStrategy("output/images")
    strategy.images_relative_path = "images"

    # Step 2: Assign the strategy to conversion options
    options = ConvertOptions()
    options.image_export_strategy = strategy

    # Step 3: Convert and save using keyword argument for options
    MarkdownConverter.to_file("business-plan.pdf", "output/report.md", convert_options=options)
    # Images saved to output/images/
    # Markdown references: ![](images/img-001.png)

if __name__ == "__main__":
    import os
    os.makedirs("output/images", exist_ok=True)
    convert_pdf_with_images()