from groupdocs.markdown import MarkdownConverter

def get_supported_formats():
    """List all file formats supported by GroupDocs.Markdown."""

    # Step 1: Retrieve the list of supported formats
    formats = MarkdownConverter.get_supported_formats()

    # Step 2: Print each supported format
    for fmt in formats:
        print(fmt)

if __name__ == "__main__":
    get_supported_formats()