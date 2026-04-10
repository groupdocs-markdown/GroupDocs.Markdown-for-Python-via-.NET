from groupdocs.markdown import MarkdownConverter, ConvertOptions, SkipImagesStrategy

def skip_images_static():
    """Convert a PDF to Markdown while skipping all images."""

    # Step 1: Configure the skip-images strategy to omit images from output
    options = ConvertOptions()
    options.image_export_strategy = SkipImagesStrategy()

    # Step 2: Convert using keyword argument for options
    MarkdownConverter.to_file("business-plan.pdf", "skip-images-static.md", convert_options=options)

if __name__ == "__main__":
    skip_images_static()