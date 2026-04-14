import os
import sys
import traceback

# Use UTF-8 for stdout on Windows to avoid encoding errors when printing
# converted Markdown that contains special Unicode characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Set license path (update this path to your license file location)
# os.environ["GROUPDOCS_LIC_PATH"] = "./GroupDocs.Markdown.lic"

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Markdown for Python via .NET Examples!
=================================================================

This script will run a series of examples showcasing how to export documents to Markdown.
Each example demonstrates different use cases and functionalities such as:

- Converting PDF, Word, Excel, eBook, and text files to Markdown.
- Controlling image export strategies.
- Using conversion options (headings, pages, front matter).
- Inspecting document metadata.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API!

=======================================================
"""
    print(intro_text)

def set_license():
    """Set the GroupDocs license from environment variable or license file."""
    from groupdocs.markdown import License

    # First, check for license path in environment variable
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")

    # Set license if found
    if license_path and os.path.exists(license_path):
        license = License()
        license.set_license(license_path)
        print(f"{GREEN}License set from: {license_path}{RESET}\n")
    else:
        print(f"{YELLOW}No license file found. Running in evaluation mode.{RESET}\n")

def run_example(base_dir, example_path):
    """Run a single example by executing its script in-process."""
    full_path = os.path.join(base_dir, example_path)
    example_dir = os.path.dirname(full_path)

    # Change to the example directory so relative paths work
    saved_cwd = os.getcwd()
    os.chdir(example_dir)
    try:
        code = open(full_path, "r", encoding="utf-8").read()
        exec(compile(code, full_path, "exec"), {"__name__": "__main__", "__file__": full_path})
    finally:
        os.chdir(saved_cwd)

examples = [
    "getting-started/quick-start-guide/import-module.py",
    "getting-started/quick-start-guide/convert_word_to_markdown.py",
    "getting-started/quick-start-guide/convert_pdf_with_images.py",
    "getting-started/quick-start-guide/convert_excel_with_options.py",
    "licensing/set_license_static.py",
    "licensing/set_license_instance.py",
    "licensing/set_license_stream_static.py",
    "licensing/set_license_stream_instance.py",
    "licensing/set_metered_license.py",
    "getting-started/how-to-run-examples/convert.py",
    "developer-guide/basic-usage/convert/_index/convert_static.py",
    "developer-guide/basic-usage/convert/_index/convert_instance.py",
    "developer-guide/basic-usage/convert/export-pdf/export_pdf_to_markdown.py",
    "developer-guide/basic-usage/convert/export-pdf/export_pdf_with_options.py",
    "developer-guide/basic-usage/convert/export-wordprocessing/export_word_to_markdown.py",
    "developer-guide/basic-usage/convert/export-wordprocessing/export_word_with_options.py",
    "developer-guide/basic-usage/get-document-info/get_info_static.py",
    "developer-guide/basic-usage/get-document-info/get_info_instance.py",
    "developer-guide/basic-usage/convert/export-spreadsheet/export_spreadsheet_to_markdown.py",
    "developer-guide/basic-usage/convert/export-spreadsheet/export_spreadsheet_with_options.py",
    "developer-guide/basic-usage/convert/export-ebook/export_ebook_to_markdown.py",
    "developer-guide/basic-usage/convert/export-ebook/export_ebook_with_options.py",
    "developer-guide/basic-usage/convert/export-text/export_text_to_markdown.py",
    "developer-guide/basic-usage/convert/export-text/export_text_with_options.py",
    "developer-guide/advanced-usage/loading/load-from-a-local-disk/load_from_disk_static.py",
    "developer-guide/advanced-usage/loading/load-from-a-local-disk/load_from_disk_instance.py",
    "developer-guide/advanced-usage/strategy/as-base64-strategy/base64_static.py",
    "developer-guide/advanced-usage/strategy/as-base64-strategy/base64_explicit.py",
    "developer-guide/advanced-usage/loading/load-from-a-stream/load_from_stream.py",
    "developer-guide/advanced-usage/loading/load-from-a-stream/load_from_stream_with_options.py",
    "developer-guide/advanced-usage/strategy/image-file-strategy/image_file_basic.py",
    "developer-guide/advanced-usage/strategy/image-file-strategy/image_file_relative.py",
    "developer-guide/advanced-usage/loading/load-a-file-of-a-specific-format/load_specific_format.py",
    "developer-guide/advanced-usage/loading/load-a-file-of-a-specific-format/get_supported_formats.py",
    "developer-guide/advanced-usage/markdown-flavor/flavor_github.py",
    "developer-guide/advanced-usage/markdown-flavor/flavor_commonmark.py",
    "developer-guide/advanced-usage/strategy/image-skip-strategy/skip_images_static.py",
    "developer-guide/advanced-usage/strategy/image-skip-strategy/skip_images_instance.py",
    "developer-guide/advanced-usage/convert-specific-pages/convert_specific_pages_static.py",
    "developer-guide/advanced-usage/convert-specific-pages/convert_specific_pages_instance.py",
    "developer-guide/advanced-usage/convert-specific-pages/convert_specific_pages_to_file.py",
    "developer-guide/advanced-usage/front-matter/front_matter_example.py",
    "developer-guide/advanced-usage/front-matter/front_matter_combined.py",
    "developer-guide/advanced-usage/loading/load-a-password-protected-document/load_password_static.py",
    "developer-guide/advanced-usage/loading/load-a-password-protected-document/load_password_instance.py",
    "developer-guide/advanced-usage/loading/load-a-password-protected-document/load_password_exception.py",
    "developer-guide/advanced-usage/strategy/custom-strategy/custom_strategy_rename.py",
    "developer-guide/advanced-usage/strategy/custom-strategy/custom_strategy_replace.py",
    "developer-guide/advanced-usage/heading-offset/heading_offset_example.py",
    "developer-guide/advanced-usage/spreadsheet-options/spreadsheet_truncation.py",
    "developer-guide/advanced-usage/spreadsheet-options/spreadsheet_sheets.py",
    "developer-guide/advanced-usage/error-handling/error_handling_example.py",
    "developer-guide/advanced-usage/error-handling/warnings_example.py",
    "developer-guide/advanced-usage/async-api/async_static.py",
    "developer-guide/advanced-usage/async-api/async_instance.py",
    "developer-guide/advanced-usage/async-api/async_concurrent.py",
    "developer-guide/advanced-usage/async-api/async_fastapi.py",
    "developer-guide/advanced-usage/uri-rewriting/uri_rewriting_cdn.py",
    "developer-guide/use-cases/convert-for-rag/convert_for_rag.py",
    "developer-guide/use-cases/convert-for-rag/batch_convert_for_rag.py",
    "developer-guide/use-cases/static-site-generator/static_site_convert.py",
    "developer-guide/use-cases/static-site-generator/batch_convert_for_hugo.py",
    "developer-guide/use-cases/batch-convert/batch_convert.py",
    "product-overview/quick_example.py",
]

print_intro()
set_license()

base_dir = os.path.dirname(__file__)
passed = 0
failed = 0

for example in examples:
    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        run_example(base_dir, example)
        print(f"{GREEN}Completed {example}{RESET}\n")
        passed += 1
    except Exception as e:
        print(f"{RED}Error in {example}: {type(e).__name__}: {e}{RESET}\n")
        failed += 1

print(f"\n{GREEN}Passed: {passed}{RESET}  {RED}Failed: {failed}{RESET}  Total: {passed + failed}")
