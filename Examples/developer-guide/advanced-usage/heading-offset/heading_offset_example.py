from groupdocs.markdown import MarkdownConverter, ConvertOptions

def heading_offset_example():
    """Shift all heading levels by a fixed offset when converting to Markdown."""

    # Step 1: Set the heading level offset to 2
    options = ConvertOptions()
    options.heading_level_offset = 2  # shift all headings down two levels

    # Step 2: Convert the document and save it to a Markdown file
    MarkdownConverter.to_file("annual-report.docx", "heading-offset-example.md", convert_options=options)

    # Source: # Title     -> Output: ### Title
    # Source: ## Section  -> Output: #### Section
    # Heading levels are clamped to the range 1-6.

if __name__ == "__main__":
    heading_offset_example()