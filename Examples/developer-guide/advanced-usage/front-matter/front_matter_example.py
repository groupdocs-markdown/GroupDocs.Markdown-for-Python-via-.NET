from groupdocs.markdown import MarkdownConverter, ConvertOptions

def front_matter_example():
    """Convert a document to Markdown with YAML front matter extracted from metadata."""

    # Step 1: Enable front matter generation in conversion options
    options = ConvertOptions()
    options.include_front_matter = True

    # Step 2: Convert the document and save it to a Markdown file
    MarkdownConverter.to_file("business-plan.docx", "front-matter-example.md", convert_options=options)
    # Output:
    # ---
    # title: "Q3 Report"
    # author: "Jane Doe"
    # format: Docx
    # pages: 12
    # ---
    #
    # # Q3 Report
    # ...

if __name__ == "__main__":
    front_matter_example()