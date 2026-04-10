from groupdocs.markdown import MarkdownConverter

def get_info_instance():
    """Retrieve document metadata using the instance API."""

    # Step 1: Open the spreadsheet with a context manager
    with MarkdownConverter("cost-analysis.xlsx") as converter:
        # Step 2: Retrieve document metadata
        info = converter.get_document_info()

        print(f"Format:     {info.file_format}")
        print(f"Pages:      {info.page_count}")
        print(f"Title:      {info.title}")
        print(f"Author:     {info.author}")
        print(f"Encrypted:  {info.is_encrypted}")

if __name__ == "__main__":
    get_info_instance()