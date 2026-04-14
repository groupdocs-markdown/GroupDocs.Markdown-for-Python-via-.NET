from groupdocs.markdown import MarkdownConverter, LoadOptions, FileFormat

def load_from_stream_with_options():
    """Load a document from a stream with explicit format specification."""

    # Step 1: Open the file as a binary stream
    with open("document", "rb") as stream:
        # Step 2: Specify the file format explicitly (no auto-detection)
        load_options = LoadOptions(FileFormat.DOCX)

        # Step 3: Create a converter from the stream with load options
        with MarkdownConverter(stream, load_options=load_options) as converter:
            # Step 4: Convert and save the Markdown output
            converter.convert("load-stream-with-options.md")

if __name__ == "__main__":
    import shutil
    shutil.copy("business-plan.docx", "document")  # create file without extension
    load_from_stream_with_options()