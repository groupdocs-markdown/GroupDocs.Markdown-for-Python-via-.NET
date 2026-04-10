import os
from groupdocs.markdown import License

def set_license_stream_instance():
    """Apply a license from a stream using the instance method."""

    # Step 1: Open the license file as a binary stream
    license_path = "GroupDocs.Markdown.lic"
    if os.path.exists(license_path):
        with open(license_path, "rb") as stream:
            # Step 2: Create a License instance and apply from the stream
            license = License()
            license.set_license(stream)

if __name__ == "__main__":
    set_license_stream_instance()