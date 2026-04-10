from groupdocs.markdown import MarkdownConverter, DocumentProtectedException

def load_password_exception():
    """Handle incorrect or missing passwords when opening protected documents."""

    try:
        # Step 1: Attempt to convert without providing a password
        markdown = MarkdownConverter.to_markdown("protected.docx")
    except DocumentProtectedException as ex:
        # Step 2: Catch the exception and display a user-friendly message
        print(f"Cannot open document: {ex}")

if __name__ == "__main__":
    load_password_exception()