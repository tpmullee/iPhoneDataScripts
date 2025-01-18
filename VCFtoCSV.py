import csv
import re

# Define the function to parse vCard and export to CSV
def parse_vcard_to_csv(input_vcf, output_csv):
    """
    Parses a vCard (.vcf) file and exports the contacts to a CSV file.

    Parameters:
        input_vcf (str): Path to the input vCard file.
        output_csv (str): Path to the output CSV file.

    Output:
        A clean CSV file with the following fields:
        - First Name
        - Last Name
        - Email
        - Phone
        - Organization
        - Street Address
        - City
        - State
        - Postal Code
        - Country
    """
    with open(input_vcf, 'r') as vcf_file:
        contacts = []
        contact = {}

        for line in vcf_file:
            line = line.strip()
            
            if line.startswith('END:VCARD'):
                if 'Full Name' in contact:
                    # Split Full Name into First Name and Last Name
                    names = contact['Full Name'].split(' ', 1)
                    contact['First Name'] = names[0]
                    contact['Last Name'] = names[1] if len(names) > 1 else ''
                    del contact['Full Name']
                
                if 'item1.ADR' in contact:
                    # Split address into components (assuming standard format)
                    address_parts = contact['item1.ADR'].split(';')
                    contact['Street Address'] = address_parts[2].replace('\n', ', ') if len(address_parts) > 2 else ''
                    contact['City'] = address_parts[3] if len(address_parts) > 3 else ''
                    contact['State'] = address_parts[4] if len(address_parts) > 4 else ''
                    contact['Postal Code'] = address_parts[5] if len(address_parts) > 5 else ''
                    contact['Country'] = address_parts[6] if len(address_parts) > 6 else ''
                    del contact['item1.ADR']
                
                if 'Phone' in contact:
                    # Standardize phone number format
                    phone = re.sub(r'[^0-9]', '', contact['Phone'])  # Remove non-numeric characters
                    contact['Phone'] = f"+{phone}" if len(phone) > 10 else phone

                if 'Organization' in contact:
                    # Remove trailing semicolon from Organization
                    contact['Organization'] = contact['Organization'].rstrip(';')

                contacts.append(contact)
                contact = {}
            elif line.startswith('FN:'):
                contact['Full Name'] = line.split(':', 1)[1].strip()
            elif line.startswith('EMAIL;'):
                contact['Email'] = line.split(':', 1)[1].strip()
            elif line.startswith('TEL;'):
                contact['Phone'] = line.split(':', 1)[1].strip()
            elif line.startswith('ORG:'):
                contact['Organization'] = line.split(':', 1)[1].strip()

        # Write to CSV
        with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['First Name', 'Last Name', 'Email', 'Phone', 'Organization', 'Street Address', 'City', 'State', 'Postal Code', 'Country']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contacts)

        print(f"Converted {input_vcf} to {output_csv}")

# Example usage (for documentation purposes only):
if __name__ == "__main__":
    input_vcf_path = 'sample.vcf'  # Replace with the actual input file path
    output_csv_path = 'contacts.csv'  # Replace with the actual output file path

    parse_vcard_to_csv(input_vcf_path, output_csv_path)

# Instructions for Uploading to GitHub:
# 1. Initialize a GitHub repository on your local machine.
# 2. Add this script to the repository.
# 3. Commit the script using `git commit -m "Add vCard to CSV parser script"`.
# 4. Push the repository to GitHub using `git push origin main` (or the appropriate branch).