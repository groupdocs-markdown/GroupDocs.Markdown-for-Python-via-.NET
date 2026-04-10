from groupdocs.markdown import MarkdownConverter

def base64_static():
    """Convert a PDF to Markdown with images embedded as Base64 (default behavior)."""

    # Step 1: Convert the document -- images are embedded as Base64 by default
    markdown = MarkdownConverter.to_markdown("business-plan.pdf")

    # Step 2: Print the self-contained Markdown output
    print(markdown)

if __name__ == "__main__":
    base64_static()