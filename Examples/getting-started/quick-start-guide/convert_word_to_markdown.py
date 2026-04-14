from groupdocs.markdown import MarkdownConverter

def convert_word_to_markdown():
    """Convert a Word document to Markdown in one line of code."""

    # Convert a DOCX file directly to a Markdown file on disk
    MarkdownConverter.to_file("business-plan.docx", "quick-start-word.md")

if __name__ == "__main__":
    convert_word_to_markdown()