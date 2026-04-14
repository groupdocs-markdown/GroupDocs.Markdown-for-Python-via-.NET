import asyncio
from groupdocs.markdown import MarkdownConverter

async def async_concurrent():
    """Convert several documents concurrently with asyncio.gather()."""

    # Step 1: Define the source files and their output targets
    jobs = [
        ("business-plan.docx", "async-concurrent-docx.md"),
        ("business-plan.pdf",  "async-concurrent-pdf.md"),
        ("cost-analysis.xlsx", "async-concurrent-xlsx.md"),
    ]

    # Step 2: Launch every conversion concurrently
    await asyncio.gather(*(
        MarkdownConverter.to_file_async(src, dst, None) for src, dst in jobs
    ))

if __name__ == "__main__":
    asyncio.run(async_concurrent())