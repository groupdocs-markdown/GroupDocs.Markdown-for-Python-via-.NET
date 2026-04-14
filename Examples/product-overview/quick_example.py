from groupdocs.markdown import MarkdownConverter, ConvertOptions, MarkdownFlavor

def quick_example():
    """Convert a Word document to Markdown with GitHub flavor and YAML front matter."""

    # One-liner
    md = MarkdownConverter.to_markdown("business-plan.docx")
    # # Quarterly Report
    #
    # ## Executive Summary
    #
    # This report covers the key initiatives...

    # With options
    options = ConvertOptions()
    options.flavor = MarkdownFlavor.GIT_HUB
    options.include_front_matter = True
    options.heading_level_offset = 1
    MarkdownConverter.to_file("business-plan.docx", "quick-example.md", convert_options=options)

if __name__ == "__main__":
    quick_example()