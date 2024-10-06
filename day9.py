# Day 9 Notes

#! 1. What is Database?
# A database is an organized collection of large amounts of data for easy storage and retrieval.

#! 2. Types of Database?
# There are many types of database, but the mainly focues, & famous are:
#* 2.1 MySQL: It's an Relational Databases (RDBMS) type of database which organizes data into tables with rows and columns.
#* 2.1 MongoDB: It's an Non-Relational Databases stores data in a flexible, document-like structure (like aJSON ile).Store data permanently.


#! 3. What is MySQL?
# MySQL is a popular RDBMS that organizes data into tables with predefined schemas.
# Tables: Data is organized in a structured format using rows and columns. Each table stores data related to a specific entity.
# Rows (Records): Each row in a table represents a single record. For example, in a table of employees, each row represents a unique employee's data.
# Columns (Fields): Each column represents a specific attribute of the data, like name, age, or address in an employee table. 

#! 4. How to Connect Python to MySQL?
# Step 1:- Install the MySQL Connector: pip install mysql-connector-python.
# Step 2:-
import mysql.connector

# Establish a connection to the MySQL database using the specified credentials
connection = mysql.connector.connect(
    host="localhost",            # The hostname of the MySQL server (use "localhost" for local server)
    user="priyalrajtest",        # MySQL username (the user created in the MySQL server)
    password="priyalrajtest",    # Password for the specified MySQL user
    database="priyalrajtestdb"   # The name of the database to connect to
)

# Check if the connection to the MySQL database was successful
if connection.is_connected():
    print("Connected to MySQL database")

# Create a cursor object, which is used to execute SQL queries and fetch data from the database
cursor = connection.cursor()

# Close the cursor and the connection to free up resources
cursor.close()  # Always close the cursor after you're done executing queries
connection.close()  # Close the connection to the MySQL database


#! 5. Create Operation in MySQL:
# Execute an INSERT query
cursor.execute("INSERT INTO testtable (name, age, city) VALUES ('Amit', 17, 'Patna')")

# Commit the transaction to save the changes
connection.commit()  # Commit the transaction

#! 6. Read Operation in MySQL:
# Example query to fetch data from a table
# Uncomment and replace 'testtable' with the actual table name in your database
cursor.execute("SELECT * FROM testtable")  # Replace 'your_table' with the table name present in 'priyalrajtestdb'

# Fetch all rows from the result of the executed query and print each row
for row in cursor.fetchall():  # Iterate through each row in the fetched result
    print(row)  # Print each row (tuple) from the query result

#! 7. Update Operation in MYSQL:
cursor.execute("UPDATE testtable SET age = 50 WHERE Name = 'Priyal'")
connection.commit()

#! 8. Delete Operation in MYSQL:
cursor.execute("DELETE FROM testtable WHERE age = '50'")
connection.commit()  # Commit the delete transaction

#! 9. What is MongoDB?
# MongoDB stores data in a flexible, document-oriented format.
# Key-Value Pairs: Similar to Python dictionaries.
# Flexible Schema: No predefined structure required.
# Nested Documents: Can contain sub-documents and arrays.
# Complex Data: Supports storing complex data types.

#! 10. Connect to MongoDB using Python:
from pymongo import MongoClient  # Import the MongoClient class from pymongo

# Establish a connection to the MongoDB server
try:
    client = MongoClient("mongodb://localhost:27017/")  # Connect to the local MongoDB server
    # Access a specific database (replace 'your_database' with your database name)
    db = client["your_database"]

    # Check if the server is accessible by listing databases
    server_info = client.server_info()  # If this command executes without error, connection is successful
    print("Connected to MongoDB server successfully!")  # Print connection success message
except Exception as e:
    print(f"Failed to connect to MongoDB server: {e}")  # Print error message if connection fails


#! 11. Create Operation in MongoDB:
# Insert a new document into the collection
db.testtable.insert_one({"name": "Amit", "age": 17, "city": "Patna"})

#! 12. Read Operation in MongoDB:
# Retrieve all documents from the collection
for doc in db.testtable.find():
    print(doc)

#! 13. Update Operation in MongoDB:
# Update the age of the document where the name is 'Priyal'
db.testtable.update_one({"name": "Priyal"}, {"$set": {"age": 50}})

#! 14. Delete Operation in MongoDB:
# Delete the document where the age is 50
db.testtable.delete_one({"age": 50})