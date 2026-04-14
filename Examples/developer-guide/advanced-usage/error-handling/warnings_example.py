from groupdocs.markdown import MarkdownConverter, ConvertOptions

def warnings_example():
    """Show how to inspect non-fatal conversion warnings after converting."""

    # Step 1: Open the spreadsheet with a context manager
    with MarkdownConverter("cost-analysis.xlsx") as converter:
        # Step 2: Configure row truncation
        options = ConvertOptions()
        options.max_rows = 10  # limit to first 10 data rows per sheet

        # Step 3: Convert and capture the result for inspection
        result = converter.convert("warnings-example.md", convert_options=options)

        # Step 4: Write any non-fatal warnings to a separate text file
        with open("warnings-example.txt", "w", encoding="utf-8") as f:
            for warning in result.warnings:
                f.write(f"Warning: {warning}\n")

if __name__ == "__main__":
    warnings_example()