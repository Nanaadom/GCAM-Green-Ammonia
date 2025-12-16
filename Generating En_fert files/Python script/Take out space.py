import os
import glob

def process_xml_files(directory, file_pattern="*.xml"):
    """
    Process all XML files in the specified directory.
    Replaces " />" with "/>" in each file and saves the changes.
    """
    # Construct the full path pattern
    full_pattern = os.path.join(directory, file_pattern)

    # find all XML files in the directory
    xml_files = glob.glob(full_pattern)

    for file_path in xml_files:
        # Read the content of the XML file
        with open(file_path, 'r') as file:
            content = file.read()

        #  Find " />" and Replace with "/>"
        modified_content = content.replace(" />", "/>")

        # Save the modified content back to the same file
        with open(file_path, 'w') as file:
            file.write(modified_content)

# Specific directory
directory = r"D:\GCAM\XML_Files"

# Calling the function to process the XML files in the specified directory
process_xml_files(directory)
