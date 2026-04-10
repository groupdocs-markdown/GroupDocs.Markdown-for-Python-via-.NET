from groupdocs.markdown import MarkdownConverter
from groupdocs.markdown import DocumentProtectedException, InvalidFormatException, GroupDocsMarkdownException

def error_handling_example():
    """Demonstrate error handling with specific exception types during conversion."""

    try:
        # Step 1: Attempt to convert the document
        MarkdownConverter.to_file("annual-report.docx", "error-handling.md")
    except DocumentProtectedException:
        # Step 2a: Handle password-protected documents
        print("Wrong or missing password.")
    except InvalidFormatException:
        # Step 2b: Handle corrupt or unsupported file formats
        print("File is corrupt or unsupported.")
    except GroupDocsMarkdownException as ex:
        # Step 2c: Handle any other conversion errors
        print(f"Conversion failed: {ex}")

if __name__ == "__main__":
    error_handling_example()