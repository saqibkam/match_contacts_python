import os
import pandas as pd
from collections import defaultdict

def merge_group_files(input_directory, output_directory):
    # Dictionary to hold files by group
    groups = defaultdict(list)

    # List all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            group_name = filename[0]  # Assuming group is identified by the first character
            groups[group_name].append(os.path.join(input_directory, filename))

    # Merge files within each group
    for group, files in groups.items():
        df_list = [pd.read_csv(file) for file in files]
        merged_df = pd.concat(df_list, ignore_index=True)
        merged_df.to_csv(os.path.join(output_directory, f"{group}.csv"), index=False)
        print(f"Merged {len(files)} files into {group}.csv")

def find_emails_in_at_least_five_groups(output_directory, final_output_directory):
    # Load group files into a dictionary
    group_files = {f"{i}.csv": pd.read_csv(os.path.join(output_directory, f"{i}.csv")) for i in range(1, 9)}

    # Dictionary to count occurrences of each email
    email_occurrences = defaultdict(int)
    email_name_map = {}

    # Count email occurrences across all groups and track names
    for group, df in group_files.items():
        emails = df['Email'].dropna()
        for email, name in zip(df['Email'], df['Contact Name']):
            email_occurrences[email] += 1
            if email not in email_name_map:
                email_name_map[email] = name

    # Filter emails found in at least 5 group files
    valid_emails = {email for email, count in email_occurrences.items() if count >= 5}

    # Function to generate tags based on frequency
    def generate_tags(frequency):
        base_tag = 'newsletter'
        if frequency == 5:
            return f"{base_tag}, five"
        elif frequency == 6:
            return f"{base_tag}, six"
        elif frequency == 7:
            return f"{base_tag}, seven"
        elif frequency == 8:
            return f"{base_tag}, eight"

    # Create a DataFrame for the valid emails with the tags column
    final_df = pd.DataFrame({
        'Email': list(valid_emails),
        'Contact Name': [email_name_map[email] for email in valid_emails],
        'Tags': [generate_tags(email_occurrences[email]) for email in valid_emails]  # Tags column
    })

    # Save the result to the output file
    final_df.to_csv(os.path.join(final_output_directory, "five_or_more_output.csv"), index=False)
    print(f"Saved emails found in at least 5 groups to 'five_or_more_output.csv' with tags")

if __name__ == "__main__":
    input_directory = "input_files"  # Directory containing your CSV files
    output_directory = "group_files"  # Directory to save merged group files
    final_output_directory = "final_output"  # Directory to save final output files

    # Ensure output directories exist
    os.makedirs(output_directory, exist_ok=True)
    os.makedirs(final_output_directory, exist_ok=True)

    # Step 1: Merge files within each group
    merge_group_files(input_directory, output_directory)

    # Step 2: Find emails in at least 5 group files and add tags column
    find_emails_in_at_least_five_groups(output_directory, final_output_directory)
