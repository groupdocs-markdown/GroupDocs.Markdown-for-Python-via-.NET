from groupdocs.markdown import MarkdownConverter

def load_from_disk_instance():
    """Load a local file with the instance API, then convert it."""

    # Step 1: Open the document with a context manager
    with MarkdownConverter("business-plan.docx") as converter:
        # Step 2: Convert to Markdown and save the result
        converter.convert("load-disk-instance.md")

if __name__ == "__main__":
    load_from_disk_instance()