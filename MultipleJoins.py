#Importing SQLite library
import sqlite3

# Connecting to the SQLite database
conn = sqlite3.connect('Customers_Multiple_Join.db')
cursor = conn.cursor()

# Creating the customers table
cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,  
        customer_name TEXT NOT NULL       
    );
''')

# Creating the products table
cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,  
        product_name TEXT NOT NULL     
    );
''')

# Creating the orders table
cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,      
        customer_id INTEGER,                
        product_id INTEGER,                
        order_date TEXT NOT NULL,          
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),  
        FOREIGN KEY (product_id) REFERENCES products(product_id)      
    );
''')

# Inserting records into the customers table
cursor.executemany(''' 
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?); 
''', [
    (1, 'Lalith Kumar'),
    (2, 'Yashwanth Kuntla'),
    (3, 'Swaraj Msani')
])

# Printing records from the customers table
cursor.execute("Select * from customers")
print("\n Customers Table \n")
rows = cursor.fetchall()  
for row in rows:
    print(row) 

# Inserting records into the products table
cursor.executemany(''' 
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?); 
''', [
    (1, 'Mobile'),
    (2, 'Smart TV'),
    (3, 'Watch'),
    (4, 'Camera')
])

# Printing records from the products table
cursor.execute("Select * from products")
print("\n Products Table \n")
rows = cursor.fetchall()  
for row in rows:
    print(row)  

# Inserting records into the orders table
cursor.executemany(''' 
    INSERT INTO orders (order_id, customer_id, product_id, order_date) 
    VALUES (?, ?, ?, ?); 
''', [
    (101, 1, 1, '2024-08-09'), 
    (102, 1, 2, '2024-08-22'),  
    (103, 2, 3, '2024-08-19'), 
    (104, 3, 4, '2024-08-02'),  
])

# Printing records from the orders table
cursor.execute("Select * from orders")
print("\n Orders Table \n")
rows = cursor.fetchall() 
for row in rows:
    print(row)  

# Performing a multiple join
cursor.execute('''
    SELECT customers.customer_name, products.product_name, orders.order_date
    FROM orders
    JOIN customers ON orders.customer_id = customers.customer_id  
    JOIN products ON orders.product_id = products.product_id; 
''')

rows = cursor.fetchall()  

print("Customer Name  | Product Name  | Order Date")
print("-------------------------------------------")
for row in rows:
    customer_name = row[0] 
    product_name = row[1] 
    order_date = row[2]     
    print(f"{customer_name:<14} | {product_name:<12} | {order_date}")  

# Committing and closing the connection
conn.commit()  
conn.close()   