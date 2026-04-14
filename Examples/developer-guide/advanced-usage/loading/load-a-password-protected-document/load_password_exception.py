from groupdocs.markdown import MarkdownConverter, DocumentProtectedException

def load_password_exception():
    """Handle incorrect or missing passwords when opening protected documents."""

    try:
        # Step 1: Attempt to convert without providing a password
        MarkdownConverter.to_file("protected.docx", "load-password-exception.md")
    except DocumentProtectedException as ex:
        # Step 2: Catch the exception and write a user-friendly message to a file
        with open("load-password-exception.txt", "w", encoding="utf-8") as f:
            f.write(f"Cannot open document: {ex}\n")

if __name__ == "__main__":
    load_password_exception()