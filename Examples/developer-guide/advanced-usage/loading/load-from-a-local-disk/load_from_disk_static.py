from groupdocs.markdown import MarkdownConverter

def load_from_disk_static():
    """Load and convert a local file to Markdown using the static API."""

    # Step 1: Convert a local file to a Markdown string in one call
    markdown = MarkdownConverter.to_markdown("business-plan.docx")

    # Step 2: Or save the result directly to a file on disk
    MarkdownConverter.to_file("business-plan.docx", "load-from-disk-static.md")

if __name__ == "__main__":
    load_from_disk_static()