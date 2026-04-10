from groupdocs.markdown import MarkdownConverter

def get_info_static():
    """Retrieve document metadata using the static GetInfo method."""

    # Step 1: Get document info without performing a full conversion
    info = MarkdownConverter.get_info("business-plan.docx")

    # Step 2: Print the metadata fields
    print(f"Format:    {info.file_format}")     # Docx
    print(f"Pages:     {info.page_count}")      # 42
    print(f"Title:     {info.title}")            # "Q3 Report"
    print(f"Author:    {info.author}")           # "Jane Doe"
    print(f"Encrypted: {info.is_encrypted}")     # False

if __name__ == "__main__":
    get_info_static()