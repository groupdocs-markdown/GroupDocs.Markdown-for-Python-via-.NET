import os
from groupdocs.markdown import MarkdownConverter

def batch_convert():
    """Convert all supported documents in a folder to Markdown."""

    # Step 1: Define input and output directories
    input_dir = "documents"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    converted = 0
    skipped = 0

    # Step 2: Iterate over all files in the input folder
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
            # Step 3: Convert each document to Markdown
            MarkdownConverter.to_file(file_path, output_path)
            converted += 1
            print(f"  OK: {filename}")
        except Exception as ex:
            skipped += 1
            print(f"  SKIP: {filename} - {ex}")

    # Step 4: Print summary
    print(f"Done: {converted} converted, {skipped} skipped")

if __name__ == "__main__":
    batch_convert()