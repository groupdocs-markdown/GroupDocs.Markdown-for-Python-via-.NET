import os
from groupdocs.markdown import MarkdownConverter, ConvertOptions, SkipImagesStrategy

def batch_convert_for_hugo():
    """Batch-convert all documents in a folder to Markdown with YAML front matter for Hugo/Jekyll."""

    # Step 1: Define source and output directories
    input_dir = "documents"
    output_dir = "content/posts"
    os.makedirs(output_dir, exist_ok=True)

    # Step 2: Configure conversion for static site generators
    options = ConvertOptions()
    options.include_front_matter = True          # add YAML metadata block
    options.heading_level_offset = 1             # reserve H1 for Hugo page title
    options.image_export_strategy = SkipImagesStrategy()  # text-only content

    # Step 3: Iterate over all files in the source folder
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        # Skip directories
        if not os.path.isfile(file_path):
            continue

        # Build output path with .md extension
        output_path = os.path.join(
            output_dir,
            os.path.splitext(filename)[0] + ".md")

        try:
            # Step 4: Convert each file with front matter and heading offset
            MarkdownConverter.to_file(file_path, output_path, convert_options=options)
            print(f"  OK: {filename} -> {output_path}")
        except Exception as ex:
            print(f"  SKIP: {filename} - {ex}")

if __name__ == "__main__":
    batch_convert_for_hugo()