from groupdocs.markdown import MarkdownConverter

def convert():
    """Convert a document to Markdown using the instance API."""
    with MarkdownConverter("business-plan.docx") as converter:
        converter.convert("run-example-basic.md")

if __name__ == "__main__":
    convert()