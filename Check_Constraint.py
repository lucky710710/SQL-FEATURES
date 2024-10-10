#Importing SQLite library
import sqlite3

# Connecting to the database
conn = sqlite3.connect('Products_Check_Constraint.db')
cursor = conn.cursor()

# Creating table with a CHECK constraint
cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY, 
        product_name TEXT NOT NULL, 
        price REAL NOT NULL CHECK (price > 0)
    );
''')

# Inserting product records
cursor.execute(''' 
    INSERT INTO products (product_id, product_name, price) 
    VALUES (1, 'Headphones', 49.99); 
''')
cursor.execute('''
    INSERT INTO products (product_id, product_name, price) 
    VALUES (2, 'Smartwatch', 199.99); 
''')

# Printing all records from products table
cursor.execute('''SELECT * FROM products''')
print("\nProducts Table\n")
print(cursor.fetchall())  

# Trying to insert a product with a price of 0
cursor.execute('''
    INSERT INTO products (product_id, product_name, price) 
    VALUES (3, 'Tablet', 0);
''')

# Committing and closing the connection
conn.commit()
conn.close()