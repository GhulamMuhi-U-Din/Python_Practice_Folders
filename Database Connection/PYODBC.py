import pyodbc

connection = pyodbc.connect(
    "DRIVER={MySQL ODBC 9.6 Unicode Driver};"
    "SERVER=localhost;"
    "DATABASE=northwind;"
    "UID=root;"
    "PWD=your_password;"
)

print("Connected Successfully!")
# Create a cursor
cursor = connection.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM newcustomers")

# Read all rows
rows = cursor.fetchall()

# Print each row
for row in rows:

    print(row)

# Close connection
connection.close()