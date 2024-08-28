import csv
import os

def load_csv(filename):
    """Load a CSV file and return its content as a list of dictionaries."""
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_csv(filename, fieldnames, rows, mode='w'):
    """Write data to a CSV file."""
    with open(filename, mode=mode, newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if mode == 'w':
            writer.writeheader()
        writer.writerows(rows)

def merge_tags(mla_tag, additional_tags):
    """Merge MLA tag and additional tags into a single string."""
    if additional_tags:
        return f"{mla_tag}, {additional_tags}"
    return mla_tag

def match_contacts(contacts, emails, output_file, fieldnames):
    """Match emails from emails.csv with contacts in contacts.csv and return relevant data."""
    matched_contacts = []
    processed = 0
    matched_count = 0
    
    for email_record in emails:
        email = email_record.get('Email')
        additional_tag = email_record.get('Tags')

        for contact in contacts:
            if contact.get('Email') == email:
                phone = contact.get('Mobile Phone Number') or contact.get('Phone Number')
                if phone:
                    matched_contact = {
                        'First Name': contact.get('First Name'),
                        'Last Name': contact.get('Last Name'),
                        'Email': contact.get('Email'),
                        'Phone': phone,
                        'Contact Source': contact.get('Original Source'),
                        'Job Title': contact.get('Job Title'),
                        'Company Name': contact.get('Company Name'),
                        'Street Address': contact.get('Street Address'),
                        'City': contact.get('City'),
                        'Country': contact.get('Country/Region'),
                        'State': contact.get('State/Region'),
                        'Postal Code': contact.get('Postal Code'),
                        'Website': contact.get('Website URL'),
                        'UTM Term': contact.get('UTM:Term'),
                        'UTM Content': contact.get('UTM:Content'),
                        'UTM Source': contact.get('Original Source'),  # Adjusted mapping
                        'UTM Campaign': contact.get('UTM:Campaign'),
                        'UTM Medium': contact.get('UTM:Medium'),
                        'Tags': merge_tags(contact.get('MLA Tag'), additional_tag),  # Adjusted mapping
                        'Practice Type': contact.get('What type of law do you practice? NEW'),
                        'Contact Owner': contact.get('Contact owner'),
                    }

                    matched_contacts.append(matched_contact)
                    matched_count += 1

        processed += 1

        # Write the matched contacts in batches of 500
        if processed % 500 == 0:
            write_csv(output_file, fieldnames, matched_contacts, mode='a')
            print(f"{processed} records processed. {matched_count} contacts found with phone number and stored.")
            matched_contacts.clear()  # Clear the batch list

    # Write any remaining contacts that didn't make it into a full batch
    if matched_contacts:
        write_csv(output_file, fieldnames, matched_contacts, mode='a')
        print(f"Final batch processed. {matched_count} contacts found with phone number and stored.")

def main():
    contacts_file = 'contacts.csv'
    emails_file = 'emails.csv'
    output_file = 'matched_contacts.csv'
    
    contacts = load_csv(contacts_file)
    emails = load_csv(emails_file)
    
    # Prepare the output file and write the header
    fieldnames = [
        'First Name', 'Last Name', 'Email', 'Phone', 'Contact Source', 'Job Title',
        'Company Name', 'Street Address', 'City', 'Country', 'State', 'Postal Code',
        'Website', 'UTM Term', 'UTM Content', 'UTM Source', 'UTM Campaign', 'UTM Medium',
        'Tags', 'Practice Type', 'Contact Owner'
    ]
    
    # Create the output file with the header
    write_csv(output_file, fieldnames, [], mode='w')
    
    match_contacts(contacts, emails, output_file, fieldnames)
    
    print("Processing complete.")

if __name__ == '__main__':
    main()
