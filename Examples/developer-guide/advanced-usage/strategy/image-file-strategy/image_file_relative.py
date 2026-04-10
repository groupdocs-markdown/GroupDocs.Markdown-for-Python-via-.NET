from groupdocs.markdown import MarkdownConverter, ConvertOptions, ExportImagesToFileSystemStrategy

def image_file_relative():
    """Save images to disk with portable, relative paths in the Markdown output."""

    # Step 1: Configure the image export strategy with a relative path
    strategy = ExportImagesToFileSystemStrategy("output/images")
    strategy.images_relative_path = "images"  # produces ![](images/img-001.png)

    # Step 2: Assign the strategy to conversion options
    options = ConvertOptions()
    options.image_export_strategy = strategy

    # Step 3: Convert and save using keyword argument for options
    MarkdownConverter.to_file("business-plan.pdf", "output/document.md", convert_options=options)

    # Markdown output contains: ![](images/img-001.png)
    # Image file saved to:     output/images/img-001.png

if __name__ == "__main__":
    import os
    os.makedirs("output/images", exist_ok=True)
    image_file_relative()