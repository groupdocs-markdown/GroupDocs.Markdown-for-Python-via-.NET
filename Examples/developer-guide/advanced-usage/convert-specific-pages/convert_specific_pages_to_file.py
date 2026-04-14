from groupdocs.markdown import MarkdownConverter, ConvertOptions

def convert_specific_pages_to_file():
    """Convert specific pages from a PDF and save the result to a file."""

    # Step 1: Specify which pages to convert (1-based numbering)
    options = ConvertOptions()
    options.page_numbers = [2, 4, 5]  # convert pages 2, 4, and 5

    # Step 2: Convert and save to file using keyword argument for options
    MarkdownConverter.to_file("business-plan.pdf", "convert-pages-to-file.md", convert_options=options)

if __name__ == "__main__":
    convert_specific_pages_to_file()