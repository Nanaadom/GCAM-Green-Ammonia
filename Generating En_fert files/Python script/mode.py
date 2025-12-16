import pandas as pd
import xml.etree.ElementTree as ET
import os

# Define the scenario number
scenario = 1

# Define the path to the Excel file
excel_path = r'D:\GCAM\Scenario_Input_cost\input_cost.xlsx'

# Read the Excel file
df = pd.read_excel(excel_path)

# Print available column names
print("Available columns in the Excel file:", df.columns)

# Check if 'Scenario' column exists
if 'Scenario' not in df.columns:
    raise ValueError("Column 'Scenario' not found in the Excel file.")

input_cost = df.loc[df['Scenario'] == scenario, 'Inputcost'].iloc[0]

# Define the path to the template XML file and the path for the new XML file
template_xml_path = r'D:\GCAM\Scenario_Input_cost\en_fert_template.xml'
new_xml_file_path = r'D:\GCAM\XML\en_fert_{}.xml'.format(scenario)
#                     D:\GCAM\Scenario_Input cost

# Read and modify the XML file
tree = ET.parse(template_xml_path)
root = tree.getroot()

# Assuming 'FEWtures' is a text in an element, find and replace it
# This part may need adjustment depending on the XML structure
for elem in root.iter():
    if elem.text == "FEWtures":
        elem.text = str(input_cost)

# Save the modified XML file
tree.write(new_xml_file_path)

print(f'File saved as: {new_xml_file_path}')
