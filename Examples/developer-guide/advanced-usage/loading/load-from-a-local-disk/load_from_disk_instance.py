from groupdocs.markdown import MarkdownConverter

def load_from_disk_instance():
    """Load a local file with the instance API, inspect metadata, then convert."""

    # Step 1: Open the document with a context manager
    with MarkdownConverter("business-plan.docx") as converter:
        # Step 2: Retrieve document metadata before converting
        info = converter.get_document_info()
        print(f"Format: {info.file_format}, Pages: {info.page_count}")

        # Step 3: Convert to Markdown and print the result
        converter.convert("load-from-disk-instance.md")

if __name__ == "__main__":
    load_from_disk_instance()