import sqlite3

connection = sqlite3.connect("speechie.db")
cursor = connection.cursor()

# Create the table (only if it doesn't exist)
command = """"CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT)"""""
cursor.execute(command)

# Insert data into the table
cursor.execute("INSERT INTO users VALUES ('paroafzal1345@gmail.com', '1234567890')")
cursor.execute("INSERT INTO users VALUES ('Joshua@gmail.com', 'password-josh')")
cursor.execute("INSERT INTO users VALUES ('James@gmail.com', 'easypass')")

# Commit the changes to the database
connection.commit()

print("Data inserted successfully!")

connection.close()
