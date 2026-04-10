import re
from groupdocs.markdown import MarkdownConverter, ConvertOptions, SkipImagesStrategy, MarkdownFlavor

def convert_for_rag():
    """Convert a PDF to Markdown for RAG pipelines, then split into chunks by heading."""

    # Step 1: Configure conversion for text-only RAG (skip images)
    options = ConvertOptions()
    options.image_export_strategy = SkipImagesStrategy()
    options.flavor = MarkdownFlavor.COMMON_MARK

    # Step 2: Convert the document using keyword argument for options
    markdown = MarkdownConverter.to_markdown("business-plan.pdf", convert_options=options)

    # Step 3: Split the Markdown into chunks by heading markers
    chunks = re.split(r"\n#{1,2} ", markdown)

    # Step 4: Process each chunk (e.g., send to an embedding model)
    for chunk in chunks:
        if chunk.strip():
            print(f"Chunk ({len(chunk)} chars): {chunk[:80]}...")

if __name__ == "__main__":
    convert_for_rag()