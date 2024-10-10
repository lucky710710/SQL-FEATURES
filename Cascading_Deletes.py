# Importing SQLite library
import sqlite3

# Connecting to the SQLite database
conn = sqlite3.connect('Products_Cascading_Deletes.db')
cursor = conn.cursor()

# Enabling foreign key constraints to perform cascading deletes
cursor.execute('PRAGMA foreign_keys = ON;')

# Creating the categories table
cursor.execute('''
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL
)
''')

# Creating the products table
cursor.execute('''
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
)
''')

# Inserting sample categories
categories = [
    (1, 'Home Appliances'), 
    (2, 'Apparel'),        
    (3, 'Literature')    
]
cursor.executemany('INSERT INTO categories (category_id, category_name) VALUES (?, ?)', categories)

# Inserting sample products 
products = [
    (1, 'Microwave', 1),    
    (2, 'Washing Machine', 1),
    (3, 'Jeans', 2),       
    (4, 'Fiction Novel', 3)
]
cursor.executemany('INSERT INTO products (product_id, product_name, category_id) VALUES (?, ?, ?)', products)

# Displaying data in categories table
print("Initial data in categories table:")
cursor.execute('SELECT * FROM categories')
print(cursor.fetchall())

# Displaying data in products table
print("\nInitial data in products table:")
cursor.execute('SELECT * FROM products')
print(cursor.fetchall())

# Deleting a category 
cursor.execute('DELETE FROM categories WHERE category_id = 1')

# Displaying data in categories table after deletion
print("\nData in categories table after deleting category_id = 1 (Home Appliances):")
cursor.execute('SELECT * FROM categories')
print(cursor.fetchall())

# Displaying data in products table after the deletion
print("\nData in products table after deleting category_id = 1 (Home Appliances):")
cursor.execute('SELECT * FROM products')
print(cursor.fetchall())

# Committing the changes and closing the database connection
conn.commit()
conn.close()