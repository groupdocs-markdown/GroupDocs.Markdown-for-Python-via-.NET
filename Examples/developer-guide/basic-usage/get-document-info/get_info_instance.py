from groupdocs.markdown import MarkdownConverter

def get_info_instance():
    """Retrieve document metadata using the instance API."""

    # Step 1: Open the spreadsheet with a context manager
    with MarkdownConverter("cost-analysis.xlsx") as converter:
        # Step 2: Retrieve document metadata
        info = converter.get_document_info()

        # Step 3: Write the metadata fields to a text file
        with open("get-info-instance.txt", "w", encoding="utf-8") as f:
            f.write(f"Format:    {info.file_format}\n")
            f.write(f"Pages:     {info.page_count}\n")
            f.write(f"Title:     {info.title}\n")
            f.write(f"Author:    {info.author}\n")
            f.write(f"Encrypted: {info.is_encrypted}\n")

if __name__ == "__main__":
    get_info_instance()