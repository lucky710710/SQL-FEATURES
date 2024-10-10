# Importing SQLite library
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Customer_Violating_Foreign_Key_Constraint.db')
cursor = conn.cursor()

# Enabling foreign key constraints
cursor.execute('PRAGMA foreign_keys = ON;')

# Create the customers table
cursor.execute('''CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY, 
    customer_name TEXT NOT NULL
);''')

# Create the orders table
cursor.execute('''CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY, 
    customer_id INTEGER, 
    order_date TEXT, 
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);''')

# Insert customers into the customers table
cursor.execute('''INSERT INTO customers (customer_id, customer_name) VALUES (1, 'Lalith Kumar');''')
cursor.execute('''INSERT INTO customers (customer_id, customer_name) VALUES (2, 'Yashwanth Kuntla');''')

# Print all records from the customers table
cursor.execute('''SELECT * FROM customers;''')
print(cursor.fetchall())

# Attempting to insert an order with a non-existing customer ID (5) violates the foreign key constraint because customer_id 5 does not exist in the customers table.
cursor.execute('''INSERT INTO orders (order_id, customer_id, order_date) VALUES (1, 5, '2024-09-20');''')  

# Print all records from the orders table
cursor.execute('''SELECT * FROM orders;''')
print(cursor.fetchall())

# Commit the changes and close the database connection
conn.commit()
conn.close()