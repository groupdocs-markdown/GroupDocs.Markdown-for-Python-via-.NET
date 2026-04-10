from groupdocs.markdown import (
    MarkdownConverter, ConvertOptions,
    ExportImagesToFileSystemStrategy, CustomUriExportStrategy
)

def uri_rewriting_cdn():
    """Rewrite image URIs to point to a CDN base URL in the Markdown output."""

    # Step 1: Define the CDN base URL
    CDN_BASE = "https://cdn.example.com/assets/"

    # Step 2: Create a handler that prepends the CDN URL to each resource
    def cdn_handler(call_info):
        """Called for each resource URI during conversion.
        Receives context with ResourceFileName, ResourceFileUri.
        Returns dict with resource_file_uri to override the URI."""
        ctx = call_info["context"]
        original = ctx["ResourceFileName"]
        return {"resource_file_uri": CDN_BASE + original}

    # Step 3: Configure image and URI export strategies
    options = ConvertOptions()
    options.image_export_strategy = ExportImagesToFileSystemStrategy("./output/images")
    options.uri_export_strategy = CustomUriExportStrategy(cdn_handler)

    # Step 4: Convert and save using keyword argument for options
    MarkdownConverter.to_file("business-plan.docx", "output/report.md", convert_options=options)
    # Images saved locally to output/images/
    # Markdown references: ![](https://cdn.example.com/assets/img-001.png)

if __name__ == "__main__":
    import os
    os.makedirs("output/images", exist_ok=True)
    uri_rewriting_cdn()