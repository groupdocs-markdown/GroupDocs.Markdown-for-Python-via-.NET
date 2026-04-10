from groupdocs.markdown import MarkdownConverter, ConvertOptions, ExportImagesAsBase64Strategy

def base64_explicit():
    """Explicitly set the Base64 image strategy and convert using the instance API."""

    # Step 1: Explicitly configure the Base64 image export strategy
    options = ConvertOptions()
    options.image_export_strategy = ExportImagesAsBase64Strategy()

    # Step 2: Open the document with a context manager
    with MarkdownConverter("business-plan.pdf") as converter:
        # Step 3: Convert using keyword argument for options
        converter.convert("base64-explicit.md", convert_options=options)

if __name__ == "__main__":
    base64_explicit()