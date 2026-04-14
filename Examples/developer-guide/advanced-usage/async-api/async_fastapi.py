import os
import tempfile
from fastapi import FastAPI, UploadFile
from fastapi.responses import PlainTextResponse
from groupdocs.markdown import MarkdownConverter, ConvertOptions, MarkdownFlavor

app = FastAPI()

@app.post("/convert", response_class=PlainTextResponse)
async def async_fastapi(file: UploadFile):
    """Accept an uploaded document and return Markdown without blocking the event loop."""
    # Stream the upload to a temp file so GroupDocs.Markdown can open it
    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    options = ConvertOptions()
    options.flavor = MarkdownFlavor.GIT_HUB

    try:
        return await MarkdownConverter.to_markdown_async(tmp_path, convert_options=options)
    finally:
        os.unlink(tmp_path)