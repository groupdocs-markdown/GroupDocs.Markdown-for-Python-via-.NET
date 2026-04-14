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

    # Step 2: Iterate over all files and write a conversion log
    with open("batch-convert-basic.txt", "w", encoding="utf-8") as log:
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
                log.write(f"  OK: {filename}\n")
            except Exception as ex:
                skipped += 1
                log.write(f"  SKIP: {filename} - {ex}\n")

        # Step 4: Append a summary line
        log.write(f"Done: {converted} converted, {skipped} skipped\n")

if __name__ == "__main__":
    batch_convert()