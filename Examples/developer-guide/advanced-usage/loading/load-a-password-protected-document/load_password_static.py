from groupdocs.markdown import MarkdownConverter, LoadOptions, FileFormat

def load_password_static():
    """Open a password-protected document and convert using the static API."""

    # Step 1: Create load options with format and password
    load_options = LoadOptions(FileFormat.DOCX)
    load_options.password = "secret"

    # Step 2: Convert the protected document using keyword argument
    MarkdownConverter.to_file("protected.docx", "load-password-static.md", load_options=load_options)

if __name__ == "__main__":
    load_password_static()