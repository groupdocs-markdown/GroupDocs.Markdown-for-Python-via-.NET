from groupdocs.markdown import MarkdownConverter, ConvertOptions, ExportImagesToFileSystemStrategy

def image_file_basic():
    """Save images to a folder on disk during PDF to Markdown conversion."""

    # Step 1: Configure the file system image export strategy
    options = ConvertOptions()
    options.image_export_strategy = ExportImagesToFileSystemStrategy("output/images")

    # Step 2: Convert and save to file using keyword argument for options
    MarkdownConverter.to_file("business-plan.pdf", "output/document.md", convert_options=options)

if __name__ == "__main__":
    import os
    os.makedirs("output/images", exist_ok=True)
    image_file_basic()