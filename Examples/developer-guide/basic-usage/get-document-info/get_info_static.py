from groupdocs.markdown import MarkdownConverter

def get_info_static():
    """Retrieve document metadata using the static GetInfo method."""

    # Step 1: Get document info without performing a full conversion
    info = MarkdownConverter.get_info("business-plan.docx")

    # Step 2: Write the metadata fields to a text file
    with open("get-info-static.txt", "w", encoding="utf-8") as f:
        f.write(f"Format:    {info.file_format}\n")     # Docx
        f.write(f"Pages:     {info.page_count}\n")      # 42
        f.write(f"Title:     {info.title}\n")           # "Q3 Report"
        f.write(f"Author:    {info.author}\n")          # "Jane Doe"
        f.write(f"Encrypted: {info.is_encrypted}\n")    # False

if __name__ == "__main__":
    get_info_static()