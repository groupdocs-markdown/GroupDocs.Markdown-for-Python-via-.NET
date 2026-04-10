from groupdocs.markdown import MarkdownConverter, ConvertOptions, MarkdownFlavor

def flavor_github():
    """Convert a document to GitHub Flavored Markdown with pipe tables and strikethrough."""

    # Step 1: Set the Markdown flavor to GitHub (GFM)
    options = ConvertOptions()
    options.flavor = MarkdownFlavor.GIT_HUB

    # Step 2: Convert the document using keyword argument for options
    md = MarkdownConverter.to_markdown("business-plan.docx", convert_options=options)

    # Tables are rendered as:
    # | Column A | Column B |
    # | --- | --- |
    # | value1 | value2 |

if __name__ == "__main__":
    flavor_github()