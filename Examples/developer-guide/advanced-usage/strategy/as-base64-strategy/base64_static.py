from groupdocs.markdown import MarkdownConverter

def base64_static():
    """Convert a PDF to Markdown with images embedded as Base64 (default behavior)."""

    # Convert the document and save it to a file --
    # images are embedded as Base64 data URIs by default,
    # so the output is a single self-contained Markdown file.
    MarkdownConverter.to_file("business-plan.pdf", "base64-static.md")

if __name__ == "__main__":
    base64_static()