# Importing the SQLite library
import sqlite3

# Connecting to database
conn = sqlite3.connect('Products_Cross_Join.db')
cursor = conn.cursor()

# Creating the products table
cursor.execute(''' 
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    );''')

# Creating the customers table 
cursor.execute(''' 
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );''')

# Inserting records into products table
cursor.executemany(''' 
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Mobile'),
    (2, 'Watch'),
    (3, 'Smart TV'),
    (4, 'Laptop')
])

# Selecting all records from products table
cursor.execute("SELECT * FROM products")
print("\n Products Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Inserting records into the customers table
cursor.executemany(''' 
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'Lalith Kumar'),
    (2, 'Yashwanth Kuntla'),
    (3, 'Maniram'),
    (4, 'Mahasvin')
])

# Selecting all records from the customers table
cursor.execute("SELECT * FROM customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)  

# Performing a cross join
cursor.execute(''' 
    SELECT products.product_name, customers.customer_name
    FROM products
    CROSS JOIN customers;
''')

# Results of the cross join
print("Cross Join \n")
rows = cursor.fetchall()
print("Product Name  | Customer Name") 
print("-----------------------------")

# Printing cross join product
for row in rows:
    product_name = row[0]  
    customer_name = row[1] 
    print(f"{product_name:<12} | {customer_name}")

# Committing and closing the connection
conn.commit()
conn.close()