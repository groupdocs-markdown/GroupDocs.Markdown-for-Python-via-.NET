from groupdocs.markdown import MarkdownConverter, ConvertOptions, SkipImagesStrategy

def skip_images_instance():
    """Skip all images during conversion using the instance API."""

    # Step 1: Configure the skip-images strategy
    options = ConvertOptions()
    options.image_export_strategy = SkipImagesStrategy()

    # Step 2: Open the document with a context manager
    with MarkdownConverter("business-plan.pdf") as converter:
        # Step 3: Convert using keyword argument for options
        converter.convert("skip-images-instance.md", convert_options=options)

if __name__ == "__main__":
    skip_images_instance()