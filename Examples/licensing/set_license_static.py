import os
from groupdocs.markdown import License

def set_license_static():
    """Apply a license from a file using the static convenience method."""

    # Step 1: Set the license using the static method (call once per app)
    license_path = "GroupDocs.Markdown.lic"
    if os.path.exists(license_path):
        License.set_(license_path)

if __name__ == "__main__":
    set_license_static()