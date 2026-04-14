import asyncio
from groupdocs.markdown import MarkdownConverter, ConvertOptions

async def async_static():
    """Use the static async API to convert a document and inspect its metadata."""

    # Step 1: Convert to a Markdown string
    md = await MarkdownConverter.to_markdown_async("business-plan.docx")

    # Step 2: Convert and save directly to a file
    await MarkdownConverter.to_file_async("business-plan.docx", "async-static.md", None)

    # Step 3: Convert with options
    options = ConvertOptions()
    options.include_front_matter = True
    await MarkdownConverter.to_file_async("business-plan.docx", "async-static.md", options)

    # Step 4: Retrieve document info without a full conversion
    info = await MarkdownConverter.get_info_async("business-plan.docx", None)
    # info.file_format, info.page_count

if __name__ == "__main__":
    asyncio.run(async_static())