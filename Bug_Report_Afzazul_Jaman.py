import pandas as pd
import os
import sys
from tabulate import tabulate
import re

# Path handling for EXE
if getattr(sys, 'frozen', False):
    exe_folder = os.path.dirname(sys.executable)
else:
    exe_folder = os.path.dirname(os.path.abspath(__file__))

# File paths (relative to script/exe directory) with raw strings
csv_file = os.path.join(exe_folder, r"C:\Users\ankon\PycharmProjects\Bug_Report_Afzazul_Jaman\Bug_Report_Afzazul_Jaman(Bug_Report).csv")
xlsx_file = os.path.join(exe_folder, r"C:\Users\ankon\PycharmProjects\Bug_Report_Afzazul_Jaman\Bug_Report_Afzazul_Jaman(Bug_Report).xlsx")

# Read CSV file
try:
    data = pd.read_csv(csv_file, encoding="latin1")
except FileNotFoundError:
    print(f"Error: The file {csv_file} was not found.")
    input("Press Enter to exit...")
    sys.exit(1)
except Exception as e:
    print(f"Error reading CSV file: {e}")
    input("Press Enter to exit...")
    sys.exit(1)

# Limit to first 20 rows
data = data.iloc[:20]

# Function to handle text without wrapping URLs
def wrap_text(text, width=30):
    if pd.isna(text):
        return ""
    # Check if the text is a URL (contains "http" or "https")
    if isinstance(text, str) and re.match(r'^https?://', text):
        return text  # Return URLs without wrapping
    # Return text as-is, no wrapping
    return str(text)

# Apply text handling to all string columns
for col in data.select_dtypes(include=['object']).columns:
    data[col] = data[col].apply(wrap_text)

# Determine the maximum length of URLs in the Screenshot column
max_link_length = 0
if 'Screenshot' in data.columns:
    max_link_length = data['Screenshot'].apply(lambda x: len(str(x)) if pd.notna(x) and re.match(r'^https?://', str(x)) else 0).max()
    if max_link_length == 0:
        max_link_length = 25  # Default to 30 if no URLs found

# Create a list of column widths based on DataFrame column order
col_widths = [max_link_length if col == 'Screenshot' else 25 for col in data.columns]

# Save to Excel
try:
    data.to_excel(xlsx_file, index=False)
except Exception as e:
    print(f"Error creating Excel file: {e}")
    input("Press Enter to exit...")
    sys.exit(1)

# Display data using tabulate with dynamic column widths
print("\nBug Report Data:")
print(tabulate(data, headers='keys', tablefmt='grid', showindex=False, maxcolwidths=col_widths))

# Instruction to view full data in Excel
print("\nNote: If text or links are cut off, please open the generated Excel file for full details.")
input(f"\n✅ XLSX created: {xlsx_file}\nPress Enter to exit...")