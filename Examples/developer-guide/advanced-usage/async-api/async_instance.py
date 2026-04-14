import asyncio
from groupdocs.markdown import MarkdownConverter, ConvertOptions

async def async_instance():
    """Use the instance async API with a context manager."""

    # Step 1: Open the document with a context manager
    with MarkdownConverter("business-plan.docx") as converter:
        # Step 2: Configure conversion options
        options = ConvertOptions()
        options.heading_level_offset = 1

        # Step 3: Convert and save the Markdown output asynchronously
        await converter.convert_async("async-instance.md", options)

        # Step 4: Retrieve document metadata asynchronously
        info = await converter.get_document_info_async()
        # info.file_format, info.page_count

if __name__ == "__main__":
    asyncio.run(async_instance())