# Importing SQLite library
import sqlite3

# Connecting to the SQLite database
conn = sqlite3.connect('Customers_Natural_Join.db')
cursor = conn.cursor()

# Creating the customers table
cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );
''')

# Creating the orders table
cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
''')

# Inserting records into customers table
cursor.executemany(''' 
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'Lalith Kumar'),
    (2, 'Yashwanth Kuntla'),
    (3, 'Deepak Hooda')
])

# Displaying all records from customers table
cursor.execute("SELECT * FROM customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

# Inserting records into orders table
cursor.executemany(''' 
    INSERT INTO orders (order_id, customer_id, order_date) 
    VALUES (?, ?, ?);
''', [
    (101, 1, '2024-09-02'),  
    (102, 2, '2024-09-15'),  
    (103, 1, '2024-09-22'),  
    (104, 3, '2024-09-04')   
])

# Displaying all records from the orders table
cursor.execute("SELECT * FROM orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

# Performing natural join between customers and orders
cursor.execute(''' 
    SELECT * 
    FROM customers
    NATURAL JOIN orders;
''')

# Results of the natural join
print("\n Natural Join \n")
rows = cursor.fetchall()
print("Customer Name | Order ID | Order Date")
print("-------------------------------------")
for row in rows:
    customer_name = row[1] 
    order_id = row[2]      
    order_date = row[3]    
    print(f"{customer_name:<14} | {order_id:<8} | {order_date}")

# Committing and closing the connection
conn.commit()
conn.close()