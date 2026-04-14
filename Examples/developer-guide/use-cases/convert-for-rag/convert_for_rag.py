import re
from groupdocs.markdown import MarkdownConverter, ConvertOptions, SkipImagesStrategy, MarkdownFlavor

def convert_for_rag():
    """Convert a PDF to Markdown for RAG pipelines, then split into chunks by heading."""

    # Step 1: Configure conversion for text-only RAG (skip images)
    options = ConvertOptions()
    options.image_export_strategy = SkipImagesStrategy()
    options.flavor = MarkdownFlavor.COMMON_MARK

    # Step 2: Convert the document and save it to a Markdown file
    MarkdownConverter.to_file("business-plan.pdf", "convert-for-rag-basic.md", convert_options=options)

    # Step 3: Read the result back and split it into chunks by heading markers
    with open("convert-for-rag-basic.md", "r", encoding="utf-8") as f:
        markdown = f.read()
    chunks = [c for c in re.split(r"\n#{1,2} ", markdown) if c.strip()]

    # Step 4: Write a chunk summary to a text file (ready to feed an embedding model)
    with open("convert-for-rag-basic.txt", "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks, 1):
            f.write(f"Chunk {i} ({len(chunk)} chars): {chunk[:80]}...\n")

if __name__ == "__main__":
    convert_for_rag()