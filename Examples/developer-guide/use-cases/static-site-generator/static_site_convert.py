from groupdocs.markdown import MarkdownConverter, ConvertOptions, ExportImagesToFileSystemStrategy

def static_site_convert():
    """Convert a DOCX to Markdown with front matter and relative images for static sites."""

    # Step 1: Configure image export with relative paths
    strategy = ExportImagesToFileSystemStrategy("content/posts/images")
    strategy.images_relative_path = "images"

    # Step 2: Set conversion options for static site generators
    options = ConvertOptions()
    options.include_front_matter = True       # add YAML metadata block
    options.heading_level_offset = 1          # reserve H1 for the page title
    options.image_export_strategy = strategy

    # Step 3: Convert and save using keyword argument for options
    MarkdownConverter.to_file(
        "annual-report.docx", "content/posts/annual-report.md",
        convert_options=options)

    # Output file starts with:
    # ---
    # title: "Annual Report 2025"
    # author: "Finance Team"
    # format: Docx
    # pages: 24
    # ---
    #
    # ## Executive Summary
    # ...

if __name__ == "__main__":
    import os
    os.makedirs("content/posts/images", exist_ok=True)
    static_site_convert()