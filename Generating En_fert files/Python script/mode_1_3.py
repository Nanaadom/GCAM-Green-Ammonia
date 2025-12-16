import pandas as pd
import xml.etree.ElementTree as ET
import os

# Define the path to the Excel file
excel_path = r'D:\GCAM\Scenario_Input_cost\input_cost.xlsx'

# Read the Excel file
df = pd.read_excel(excel_path)

# Check if 'Scenario' column exists
if 'Scenario' not in df.columns:
    raise ValueError("Column 'Scenario' not found in the Excel file.")

# Define the path to the template XML file
template_xml_path = r'D:\GCAM\Scenario_Input_cost\en_fert_template.xml'

# Output directory for new XML files
output_dir = r'D:\GCAM\XML_Files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each scenario
for scenario in range(1, 3):
    # Lookup input cost for the scenario number
    if scenario in df['Scenario'].values:
        input_cost = df.loc[df['Scenario'] == scenario, 'Inputcost'].iloc[0]
    else:
        print(f"Scenario number {scenario} not found in the Excel file.")
        continue

    # Define the path for the new XML file
    new_xml_file_path = os.path.join(output_dir, f'en_fert_{scenario}.xml')

    # Copy and modify the XML file
    tree = ET.parse(template_xml_path)
    root = tree.getroot()

    # Assuming 'FEWtures' is a text in an element
    for elem in root.iter():
        if elem.text == "FEWtures":
            elem.text = str(input_cost)

    # Save the modified XML file
    tree.write(new_xml_file_path)

    print(f'File en_fert_{scenario}.xml created with input cost: {input_cost}')
