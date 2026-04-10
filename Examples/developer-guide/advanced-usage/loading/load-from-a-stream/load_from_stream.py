from groupdocs.markdown import MarkdownConverter

def load_from_stream():
    """Load a document from a binary stream and convert to Markdown."""

    # Step 1: Open the document file as a binary stream
    with open("business-plan.docx", "rb") as stream:
        # Step 2: Create a converter from the stream
        with MarkdownConverter(stream) as converter:
            # Step 3: Convert and save the Markdown output
            converter.convert("load-from-stream.md")

if __name__ == "__main__":
    load_from_stream()