# iPhone Data Extraction and Manpulation Scripts V1

This repository contains two helpful scripts designed for managing contacts and reminders efficiently. It will grow as my project continues for repeatable scripts available for public use. 

1. **ExportReminders.scpt**: An AppleScript for exporting reminders in full from macOS.
2. **VCFtoCSV.py**: A Python script to convert vCard files into clean and organized CSV files.

## Repository Contents

### 1. ExportReminders.scpt
- **Purpose**: Exports all reminders from macOS Reminders app into a comprehensive format.
- **Language**: AppleScript
- **Key Features**:
  - Exports reminders with full details, including title, due date, notes, and completion status.
  - Saves exported data in a readable and organized format.
- **Usage**:
  - Open the script in the Script Editor on macOS.
  - Run the script to generate a file containing your reminders.
- **Output**: The reminders will be exported into a file (e.g., `.txt` or `.csv`) based on the script's configuration.

---

### 2. VCFtoCSV.py - The Apple Contact Cards are stored individually and as groups in this file type. 
- **Purpose**: Converts vCard (`.vcf`) files into a structured CSV format for data organization.
- **Language**: Python
- **Key Features**:
  - Splits full names into first and last names.
  - Organizes addresses into separate fields: Street Address, City, State, Postal Code, and Country.
  - Standardizes phone numbers to a consistent format.
  - Removes trailing semicolons from organization names.
  - Creates a clean CSV with the following fields:
    - First Name, Last Name, Email, Phone, Organization, Street Address, City, State, Postal Code, Country.
- **Usage**:
  1. Ensure you have Python installed on your system.
  2. Run the script:
     ```bash
     python VCFtoCSV.py
     ```
  3. Provide the input vCard file path (`sample.vcf`) and the output CSV file path (`contacts.csv`) as needed.
- **Output**: A structured CSV file containing the contact information from the vCard file.
