from groupdocs.markdown import MarkdownConverter, LoadOptions, FileFormat

def load_password_instance():
    """Open a password-protected spreadsheet and convert using the instance API."""

    # Step 1: Create load options with format and password
    load_options = LoadOptions(FileFormat.XLSX)
    load_options.password = "secret"

    # Step 2: Open the protected document using keyword argument for load options
    with MarkdownConverter("protected.xlsx", load_options=load_options) as converter:
        # Step 3: Convert and save the Markdown output
        converter.convert("load-password-instance.md")

if __name__ == "__main__":
    load_password_instance()