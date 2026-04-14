from groupdocs.markdown import MarkdownConverter, ConvertOptions, MarkdownFlavor

def flavor_commonmark():
    """Convert a document to strict CommonMark format (no table extensions)."""

    # Step 1: Set the Markdown flavor to CommonMark
    options = ConvertOptions()
    options.flavor = MarkdownFlavor.COMMON_MARK

    # Step 2: Convert the document and save it to a Markdown file
    MarkdownConverter.to_file("business-plan.docx", "flavor-commonmark.md", convert_options=options)

    # Tables are rendered as fenced code blocks since CommonMark
    # has no native table syntax:
    # ```
    # Column A  |  Column B
    # value1    |  value2
    # ```

if __name__ == "__main__":
    flavor_commonmark()