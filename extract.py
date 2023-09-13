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

# SQL query
sql_query = "SELECT * FROM your_table;"
cursor.execute(sql_query)

# Fetch data
data = cursor.fetchall()

# Create and open CSV file
with open("output.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write data to CSV
    for row in data:
        csv_writer.writerow(row)

# Close resources
cursor.close()
conn.close()
