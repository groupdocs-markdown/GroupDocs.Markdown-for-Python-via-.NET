from groupdocs.markdown import MarkdownConverter, ConvertOptions

def convert_instance():
    """Convert a document using the instance API with conversion options."""
    with MarkdownConverter("business-plan.docx") as converter:
        options = ConvertOptions()
        options.heading_level_offset = 1

        converter.convert("convert-instance-api.md", convert_options=options)

if __name__ == "__main__":
    convert_instance()