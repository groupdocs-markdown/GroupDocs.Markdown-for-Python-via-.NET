from groupdocs.markdown import MarkdownConverter, ConvertOptions

def front_matter_combined():
    """Convert a document with both YAML front matter and heading level offset."""

    # Step 1: Configure options with front matter and heading offset
    options = ConvertOptions()
    options.include_front_matter = True       # add YAML metadata block
    options.heading_level_offset = 1          # shift headings down one level

    # Step 2: Convert and save to a file using keyword argument for options
    MarkdownConverter.to_file("annual-report.docx", "front-matter-combined.md", convert_options=options)

if __name__ == "__main__":
    front_matter_combined()