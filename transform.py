import csv

# Open the input CSV file
with open("input.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Create an output CSV file for writing cleaned data
    with open("output.csv", "w", newline="") as cleaned_csv_file:
        csv_writer = csv.writer(cleaned_csv_file)
        
        # Loop through rows in the input CSV
        for row in csv_reader:
            # Data cleaning: Remove empty values
            cleaned_row = [value for value in row if value.strip() != ""]
            
            # Write the cleaned row to the output CSV
            csv_writer.writerow(cleaned_row)
            
# Close both CSV files
csv_file.close()
cleaned_csv_file.close()
