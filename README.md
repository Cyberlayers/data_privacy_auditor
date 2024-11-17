# Data Privacy Auditor

The **Data Privacy Auditor** is a Python-based tool designed to scan file permissions and locate sensitive data, ensuring compliance with privacy standards and enhancing data security. This tool helps organizations protect sensitive information and maintain strong data privacy practices.

---

## Features
- Scans a specified directory for files with sensitive extensions (e.g., `.txt`, `.csv`, `.docx`).
- Displays file paths and permissions for easy identification of potential vulnerabilities.
- Lightweight and user-friendly for quick privacy audits.

---

## Requirements
- **Python 3**: Ensure Python is installed on your system.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Cyberlayers/data_privacy_auditor.git

---

## Example Usage
1. Run the tool:
python3 data_privacy_auditor.py
2. Enter the directory path you wish to scan:
/home/kali/test
3. Sample output:
Scanning for sensitive files...
File: /home/kali/test/sensitive.txt, Permissions: 644
File: /home/kali/test/data.csv, Permissions: 600
File: /home/kali/test/report.docx, Permissions: 700

---

## How It Works
The tool scans a specified directory and its subdirectories for files with sensitive extensions such as:

.txt
.csv
.docx
.xlsx
For each detected file, the script:

Retrieves its file path.
Analyzes its permissions.
Outputs a report to help identify potential privacy risks.
Limitations
Designed for use in authorized environments only.
Requires user input for the directory path to scan.
Does not currently provide advanced reporting or automated remediation.

---

##Disclaimer
This tool is intended for educational purposes and authorized privacy audits only. Unauthorized use on networks or systems you do not own or have explicit permission to test is illegal and unethical. The authors are not responsible for misuse.

---

##Contributing
Contributions are welcome! If you’d like to improve the tool or add features, please fork the repository and submit a pull request.

##License
No license has been applied to this project. Usage, modification, or redistribution of the code requires explicit permission from the author.


