from groupdocs.markdown import MarkdownConverter, ConvertOptions, CustomImagesStrategy

def custom_strategy_rename():
    """Rename images sequentially using a custom image saving handler."""

    # Step 1: Set up an image counter for sequential naming
    counter = [0]

    # Step 2: Define a handler that renames each image
    def rename_handler(call_info):
        """Called for each image during conversion.
        Receives context with ImageFileName, ShapeType, OutputDirectory.
        Returns dict with output actions."""
        ctx = call_info["context"]
        counter[0] += 1
        new_name = f"fig-{counter[0]}.png"
        print(f"  Renaming: {ctx['ImageFileName']} -> {new_name}")
        return {"output_image_file_name": new_name}

    # Step 3: Configure the custom image strategy with the handler
    options = ConvertOptions()
    options.image_export_strategy = CustomImagesStrategy("./output/images", rename_handler)

    # Step 4: Convert -- each image triggers the rename_handler callback
    MarkdownConverter.to_file("business-plan.docx", "output/document.md", convert_options=options)

if __name__ == "__main__":
    import os
    os.makedirs("output/images", exist_ok=True)
    custom_strategy_rename()