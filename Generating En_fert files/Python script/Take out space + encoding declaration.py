import os
import glob

def process_xml_files(directory, file_pattern="*.xml"):
    """
    Process all XML files in the specified directory.
    Ensures "<?xml version='1.0' encoding='UTF-8'?>" is at the beginning of each file.
    Replaces " />" with "/>" in each file and saves the changes.
    """
    xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
    
    # Construct the full path pattern
    full_pattern = os.path.join(directory, file_pattern)

    # Find all XML files in the directory
    xml_files = glob.glob(full_pattern)

    for file_path in xml_files:
        # Read the content of the XML file
        with open(file_path, 'r') as file:
            content = file.read()

        # Ensure the XML declaration is at the beginning
        if not content.startswith('<?xml'):
            content = xml_declaration + content
        else:
            # Update existing declaration
            content = xml_declaration + content.split('\n', 1)[1]

        #  Find " />" and Replace with "/>"
        modified_content = content.replace(" />", "/>")

        # Save the modified content back to the same file
        with open(file_path, 'w') as file:
            file.write(modified_content)

# Specific directory
directory = r"D:\GCAM\XML_Files"

# Calling the function to process the XML files in the specified directory
process_xml_files(directory)
