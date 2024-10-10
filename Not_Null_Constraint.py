# Import SQLite library
import sqlite3

# Connect to database
conn = sqlite3.connect('Users_Not_Null.db')
cursor = conn.cursor() 

# Create the users table 
cursor.execute('''CREATE TABLE users (
    user_id INTEGER PRIMARY KEY, 
    username TEXT NOT NULL, 
    email TEXT NOT NULL   
);''')

# Insert data into users table
cursor.execute('INSERT INTO users (user_id, username, email) VALUES (1, "Lalith Kumar", "dlk@yahoo.com");')
cursor.execute('INSERT INTO users (user_id, username, email) VALUES (2, "Yashwanth Kuntla", "yk@outlook.com");')

# Attempt to insert a user with a NULL username
try:
    cursor.execute('INSERT INTO users (user_id, username, email) VALUES (3, NULL, "msani@gmail.com");')
except sqlite3.IntegrityError as e:
    print("Error:", e)

# Attempt to insert user with a NULL email
try:
    cursor.execute('INSERT INTO users (user_id, username, email) VALUES (4, "Lucky", NULL);')
except sqlite3.IntegrityError as e:
    print("Error:", e) 

# Display the data in the users table
print("\n Current data in the users table:")
cursor.execute('SELECT * FROM users')
for row in cursor.fetchall():
    print(row) 

# Commit and close the connection
conn.commit()
conn.close()