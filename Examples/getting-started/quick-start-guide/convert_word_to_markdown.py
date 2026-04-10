from groupdocs.markdown import MarkdownConverter

def convert_word_to_markdown():
    """Convert a Word document to Markdown in one line of code."""

    # Step 1: Convert a DOCX file to a Markdown string
    markdown = MarkdownConverter.to_markdown("business-plan.docx")

    # Step 2: Or save the result directly to a .md file
    MarkdownConverter.to_file("business-plan.docx", "convert-word.md")

if __name__ == "__main__":
    convert_word_to_markdown()