from groupdocs.markdown import MarkdownConverter

def load_from_disk_static():
    """Load and convert a local file to Markdown using the static API."""

    # Convert a local file directly to a Markdown file on disk
    MarkdownConverter.to_file("business-plan.docx", "load-disk-static.md")

if __name__ == "__main__":
    load_from_disk_static()