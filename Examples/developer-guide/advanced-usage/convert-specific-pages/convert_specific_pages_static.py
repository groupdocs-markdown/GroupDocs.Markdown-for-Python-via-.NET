from groupdocs.markdown import MarkdownConverter, ConvertOptions

def convert_specific_pages_static():
    """Convert only specific pages from a document using the static API."""

    # Step 1: Specify which pages to convert (1-based numbering)
    options = ConvertOptions()
    options.page_numbers = [1, 3]  # convert only pages 1 and 3

    # Step 2: Convert selected pages using keyword argument for options
    MarkdownConverter.to_file("business-plan.docx", "convert-pages-static.md", convert_options=options)

if __name__ == "__main__":
    convert_specific_pages_static()