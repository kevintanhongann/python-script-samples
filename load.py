import psycopg2
import csv

# Database connection
conn = psycopg2.connect(
    database="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
)

# Cursor creation
cursor = conn.cursor()

# CSV file reading
with open("input.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Insert data into the database
    for row in csv_reader:
        # Construct an INSERT statement
        sql_insert = "INSERT INTO your_table (column1, column2, column3) VALUES (%s, %s, %s);"

        # Execute the INSERT statement with the data from the CSV row
        cursor.execute(sql_insert, (row[0], row[1], row[2]))  # Adjust column indexes as needed

# Commit changes and close resources
conn.commit()
cursor.close()
conn.close()
