import os
import glob
from groupdocs.markdown import MarkdownConverter, ConvertOptions, SkipImagesStrategy, GroupDocsMarkdownException

def batch_convert_for_rag():
    """Batch-convert all PDFs in a folder to Markdown for RAG ingestion."""

    # Step 1: Configure conversion to skip images (text-only RAG)
    options = ConvertOptions()
    options.image_export_strategy = SkipImagesStrategy()

    # Step 2: Find all PDF files in the documents folder
    files = glob.glob("documents/*.pdf")

    # Step 3: Convert each file, handling errors gracefully
    for file in files:
        try:
            markdown = MarkdownConverter.to_markdown(file, convert_options=options)
            output_path = os.path.splitext(file)[0] + ".md"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"Converted: {file}")
        except GroupDocsMarkdownException as ex:
            print(f"Skipped {file}: {ex}")

if __name__ == "__main__":
    batch_convert_for_rag()