from groupdocs.markdown import MarkdownConverter, ConvertOptions

def convert_specific_pages_instance():
    """Convert only specific pages from a document using the instance API."""

    # Step 1: Open the document with a context manager
    with MarkdownConverter("business-plan.docx") as converter:
        # Step 2: Specify which pages to convert (1-based numbering)
        options = ConvertOptions()
        options.page_numbers = [1, 3]  # convert only pages 1 and 3

        # Step 3: Convert and save the result
        converter.convert("convert-pages-instance.md", convert_options=options)

if __name__ == "__main__":
    convert_specific_pages_instance()