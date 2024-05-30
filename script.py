import pandas as pd

# Read the JSON file
json_file_path = 'data.json'
with open(json_file_path, 'r') as file:
    data = pd.read_json(file)

# Write the data to an Excel file
excel_file_path = 'output.xlsx'
data.to_excel(excel_file_path, index=False)

print(f"Data has been successfully written to {excel_file_path}")
