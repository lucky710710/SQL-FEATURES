#Importing SQLite librabry
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Users_Unique_Constraint.db')
cursor = conn.cursor()

# Create a table with unique constarint
cursor.execute('''CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);''')

# Insert users into the users table
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (1, 'Lalith Kumar', 'dlk@yahoo.com');''')
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (2, 'Yashwanth Kuntla', 'yk@outlook.com');''')

# Print all users from users table
cursor.execute('''SELECT * FROM users;''')
print(cursor.fetchall())

# Trying to insert a user with the same email as Lalith
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (3, 'Msani Swaraj', 'dlk@yahoo.com');''')  

# Commit and close the connection
conn.commit()
conn.close()