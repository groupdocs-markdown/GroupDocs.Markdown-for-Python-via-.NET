from groupdocs.markdown import MarkdownConverter, ConvertOptions

def warnings_example():
    """Show how to inspect non-fatal conversion warnings after converting."""

    # Step 1: Open the spreadsheet with a context manager
    with MarkdownConverter("cost-analysis.xlsx") as converter:
        # Step 2: Configure row truncation
        options = ConvertOptions()
        options.max_rows = 10  # limit to first 10 data rows per sheet

        # Step 3: Convert using keyword argument for options
        result = converter.convert("warnings.md", convert_options=options)

        # Step 4: Inspect non-fatal warnings (e.g., truncation notices)
        for warning in result.warnings:
            print(f"Warning: {warning}")

if __name__ == "__main__":
    warnings_example()