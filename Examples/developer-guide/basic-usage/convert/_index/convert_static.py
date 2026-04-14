from groupdocs.markdown import MarkdownConverter

def convert_static():
    """Convert a document to Markdown using the static one-liner API."""
    MarkdownConverter.to_file("business-plan.docx", "convert-static-methods.md")

if __name__ == "__main__":
    convert_static()