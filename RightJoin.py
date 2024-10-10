# Importing SQLite library
import sqlite3

# Connecting to database
conn = sqlite3.connect('Product_Suppliers_Right_Join.db')
cursor = conn.cursor()

# Creating the products table
cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    );
''')

# Creating the suppliers table
cursor.execute('''
    CREATE TABLE suppliers (
        supplier_id INTEGER PRIMARY KEY,
        supplier_name TEXT NOT NULL
    );
''')

# Creating the product and suppliers table
cursor.execute('''
    CREATE TABLE product_suppliers (
        product_id INTEGER,
        supplier_id INTEGER,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
    );
''')

# Inserting records into the products table with new names
cursor.executemany('''
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Gaming Console'),
    (2, 'Fitness Tracker'),
    (3, 'Smart Speaker'),
    (4, 'Drone'),
    (5, 'VR Headset')
])

# Selecting the records from products table
cursor.execute("SELECT * FROM products")
print("\nProducts Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Inserting records into the suppliers table with new names
cursor.executemany('''
    INSERT INTO suppliers (supplier_id, supplier_name) 
    VALUES (?, ?);
''', [
    (1, 'Innovative Tech Solutions'),
    (2, 'Digital Devices Hub'),
    (3, 'NextGen Electronics')
])

# Selecting records into the suppliers table
cursor.execute("SELECT * FROM suppliers")
print("\nSuppliers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Inserting records into the product and suppliers table
cursor.executemany('''
    INSERT INTO product_suppliers (product_id, supplier_id) 
    VALUES (?, ?);
''', [
    (1, 1),  
    (2, 1),  
    (3, 2), 
    (4, 3)  
])

# Selecting records into the product and suppliers table
cursor.execute("SELECT * FROM product_suppliers")
print("\nProduct Suppliers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Performing the join
cursor.execute('''
    SELECT products.product_name, suppliers.supplier_name  
    FROM products
    LEFT JOIN product_suppliers ON products.product_id = product_suppliers.product_id
    LEFT JOIN suppliers ON product_suppliers.supplier_id = suppliers.supplier_id;
''')

rows = cursor.fetchall()

# Combining using Right join
print("\nRight Join\n")
for row in rows:
    print(row)

# Committing and closing the connection
conn.commit()
conn.close()