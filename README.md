# Bug Report Management Tool

A simple Python-based tool to read bug reports from a CSV file, display them neatly in the console, and generate a formatted Excel report. Designed to work both as a Python script and as a standalone Windows executable (.exe).

---

## 📌 Features

- Reads bug reports from a CSV file (`Bug_Report_Afzazul_Jaman(Bug_Report).csv`).
- Displays the first 20 rows of the bug report in the console using a neat tabular format.
- Handles long text and URLs gracefully to avoid truncation in console display.
- Generates a professional Excel (`.xlsx`) file with all bug report data.
- Fully compatible with standalone `.exe` builds using PyInstaller.
- Works seamlessly on Windows and can be executed from IDE or terminal.

---

## 🛠️ Installation

1. **Clone this repository:**

```bash
git clone https://github.com/afzazul-jaman/Bug_Report_Afzazul_Jaman.git
cd Bug_Report_Afzazul_Jaman
Set up a virtual environment (recommended):

bash
Copy code
python -m venv .venv
.venv\Scripts\activate   # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
⚡ Usage
Run as Python Script
bash
Copy code
python Bug_Report_Afzazul_Jaman.py
The first 20 rows will be displayed in the terminal.

A formatted Excel file Bug_Report_Afzazul_Jaman(Bug_Report).xlsx will be created in the same directory.

Open the Excel file to view full bug report data, including screenshots links.

Run as Executable (.exe)
Build the executable using PyInstaller:

bash
Copy code
pyinstaller --onefile --noconsole Bug_Report_Afzazul_Jaman.py
Run the executable:

Open dist\Bug_Report_Afzazul_Jaman.exe.

The first 20 rows will be displayed in the console.

The Excel file will be generated in the same folder as the .exe.

Note: Ensure that Bug_Report_Afzazul_Jaman(Bug_Report).csv is in the same folder as the executable or update the path accordingly.

📝 Example Output (Console)
sql

+-----------+-----------------------------------------------+----------------+----------------+----------+---------------------------------------------+------------+
| Bug ID    | Bug Title                                     | Steps to Repro | Expected Result | Actual   | Severity                                    | Screenshot|
+-----------+-----------------------------------------------+----------------+----------------+----------+---------------------------------------------+------------+
| BUG-001   | Page Takes Too Long to Load After Reload      | 1.Open the ... | Website should  | Website  | Medium                                      | https://drive.google.com/... |
| BUG-002   | Clicking on Search Bar Hides Adjacent Text...| 1.Open the ... | Clicking on ... | When the | Medium                                      | https://drive.google.com/... |
| ...       | ...                                           | ...            | ...            | ...      | ...                                         | ...        |
+-----------+-----------------------------------------------+----------------+----------------+----------+---------------------------------------------+------------+
For complete data including full text and screenshot links, open the generated Excel file.

📂 Project Structure
bash
Copy code
Bug_Report_Afzazul_Jaman/
│
├─ Bug_Report_Afzazul_Jaman.py         # Main Python script
├─ Bug_Report_Afzazul_Jaman(Bug_Report).csv  # Input CSV file
├─ Bug_Report_Afzazul_Jaman(Bug_Report).xlsx # Generated Excel file
├─ dist/                               # Folder containing compiled .exe
├─ build/                              # PyInstaller build files
├─ requirements.txt                    # Project dependencies
└─ README.md                           # Project documentation
🧰 Dependencies
Python 3.10+

pandas

tabulate

openpyxl

Install via:

pip install pandas tabulate openpyxl

⚠️ Notes
For large Excel files, opening in Excel is recommended to view full content.

The executable depends on the CSV being available in the same folder or a valid path.

The project is optimized for Windows environments.

