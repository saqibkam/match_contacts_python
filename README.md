Overview
This repository contains a Python-based solution designed to automate the process of merging and enriching contact data from multiple CSV files. The scripts provided can efficiently combine multiple CSV files into groups, match records against a source database, and enrich those records with additional data, such as phone numbers, before producing a comprehensive output file.

Key Features
CSV File Grouping and Merging: The script processes multiple CSV files by grouping them based on a specified identifier (e.g., the first character of the filename). It then merges the files within each group into a single dataset, ensuring that all relevant data is consolidated.

Identification of Frequent Emails Across Groups: The script identifies email addresses that appear in at least five different groups. These frequent emails are tagged according to their occurrence frequency (e.g., "newsletter, five", "newsletter, six"), allowing for easy categorization.

Record Enrichment with Contact Data: After identifying frequent emails, the records are enriched by matching them against a source database of contacts using email addresses as the key identifier. This step adds crucial information, such as phone numbers and other relevant contact details, to each record.

Batch Processing and Optimized Matching: The script handles large datasets efficiently by processing records in batches, preventing memory overload and ensuring smooth operation even with extensive data.

Comprehensive Output: The final output is a complete CSV file that consolidates all processed records, enriched with additional data fetched from the source database. This file is ready for further analysis or import into other systems.

How to Run
Clone the Repository: Clone this repository to your local machine.

Install Dependencies: Install the required Python packages using pip:

pip install -r requirements.txt
Prepare CSV Files: Place your input CSV files in the designated input_files directory.

Run the Scripts: Execute the scripts to start the merging, matching, and enrichment process:

python merge_and_enrich.py
python batch_match_and_export.py
Output: The processed and enriched records will be saved to new CSV files in the specified output directories.

Scripts and Their Functions
merge_group_files(input_directory, output_directory):

Merges CSV files within specified groups based on an identifier (e.g., the first character of the filename).
Saves the merged files in the output_directory.
find_emails_in_at_least_five_groups(output_directory, final_output_directory):

Identifies email addresses that appear in at least five groups.
Adds tags based on the frequency of appearance.
Saves the final output with tagged emails in the final_output_directory.
add_phone_numbers_and_filter(merged_df, contacts_file):

Enriches the merged dataset by matching it with a contacts database using email addresses.
Filters and adds phone numbers to the dataset.

Example Usage

python merge_and_enrich.py
python batch_match_and_export.py

Dependencies
Python 3.x
Required libraries: pandas, csv, and any database-specific connector (e.g., sqlite3).

Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
