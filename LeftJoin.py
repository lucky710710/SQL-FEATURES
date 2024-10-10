#Importing SQLite library
import sqlite3

# Connecting to database
connection = sqlite3.connect('Customer_Orders_Left_Join.db')
cursor = connection.cursor()

# Creating customers table
cursor.execute('''CREATE TABLE IF NOT EXISTS customers ( customer_id INTEGER PRIMARY KEY,customer_name TEXT NOT NULL);''')

# Creating the orders table
cursor.execute('''CREATE TABLE IF NOT EXISTS orders ( order_id INTEGER PRIMARY KEY,customer_id INTEGER,
               product_name TEXT NOT NULL,FOREIGN KEY (customer_id) REFERENCES customers(customer_id));''')

# Inserting records into customer table 
cursor.executemany('''INSERT INTO customers (customer_id, customer_name) VALUES (?, ?);''', [
    (1, 'Lalith Kumar'),
    (2, 'Yashwanth Kuntla'),
    (3, 'Kranti Jaddu'),
    (4, 'Swaraj Msani'),
    (5, 'Mahesh Babu')
])

# Selecting the Records from customers table
cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Inserting records into the orders table
cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, product_name) VALUES (?, ?, ?);''', [
    (101, 1, 'Refrigerator'),
    (102, 2, 'Microwave Oven'),
    (103, 1, 'Air Conditioner'),
    (104, 3, 'Washing Machine'),
    (105, 4, 'Dishwasher'),
    (106, 5, 'Vacuum Cleaner'),
    (107, 3, 'Water Purifier'),
    (108, 2, 'Blender')
])

# Selecting the records from orders table
cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Performing inner join between customer and order tables
cursor.execute('''SELECT customers.customer_name, orders.product_name FROM customers
                  LEFT JOIN orders ON customers.customer_id = orders.customer_id;''')
print("\n Left Join \n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Committing and closing the connection
connection.commit()
connection.close()