from groupdocs.markdown import MarkdownConverter, ConvertOptions, CustomImagesStrategy

def custom_strategy_replace():
    """Replace every image with a placeholder during conversion."""

    # Step 1: Define a handler that substitutes each image with a placeholder
    def watermark_handler(call_info):
        """Replace every image with a placeholder file."""
        return {
            "output_image_file_name": "placeholder.png",
            "replacement_image_path": "./assets/placeholder.png"
        }

    # Step 2: Configure the custom image strategy with the replacement handler
    options = ConvertOptions()
    options.image_export_strategy = CustomImagesStrategy("./output/images", watermark_handler)

    # Step 3: Convert and save using keyword argument for options
    MarkdownConverter.to_file("business-plan.docx", "output/document.md", convert_options=options)

if __name__ == "__main__":
    import os
    os.makedirs("output/images", exist_ok=True)
    custom_strategy_replace()