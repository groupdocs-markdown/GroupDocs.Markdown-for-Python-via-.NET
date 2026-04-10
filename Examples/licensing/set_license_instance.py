import os
from groupdocs.markdown import License

def set_license_instance():
    """Apply a license from a file using the instance method."""

    # Step 1: Define the path to the license file
    license_path = "GroupDocs.Markdown.lic"

    # Step 2: Create a License instance and apply the license
    if os.path.exists(license_path):
        license = License()
        license.set_license(license_path)

if __name__ == "__main__":
    set_license_instance()