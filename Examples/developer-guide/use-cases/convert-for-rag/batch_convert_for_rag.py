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

    # Step 3: Convert each file, handling errors gracefully, and write a log
    with open("batch-convert-for-rag.txt", "w", encoding="utf-8") as log:
        for file in files:
            output_path = os.path.splitext(file)[0] + ".md"
            try:
                MarkdownConverter.to_file(file, output_path, convert_options=options)
                log.write(f"Converted: {file}\n")
            except GroupDocsMarkdownException as ex:
                log.write(f"Skipped {file}: {ex}\n")

if __name__ == "__main__":
    batch_convert_for_rag()