# Importing SQLite library
import sqlite3

# Establishing a connection to SQLite database
conn = sqlite3.connect('Authors_Books_Foreign_Key_Definition.db')
cursor = conn.cursor()

# Create the authors table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY,
        author_name TEXT NOT NULL
    );
''')

# Create the books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        book_title TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );
''')

# Insert records into the authors table 
cursor.executemany('''
    INSERT INTO authors (author_id, author_name) 
    VALUES (?, ?);
''', [
    (1, 'Agatha Christie'),
    (2, 'Isaac Asimov'),
    (3, 'F. Scott Fitzgerald')
])

# Display records from the authors table
cursor.execute("SELECT * FROM authors")
print("\n Author Table \n")
authors_rows = cursor.fetchall()
for row in authors_rows:
    print(row)

# Insert records into the books table 
cursor.executemany('''
    INSERT INTO books (book_id, book_title, author_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Murder on the Orient Express', 1),
    (2, 'Foundation', 2),
    (3, 'The Great Gatsby', 3)
])

# Display records from the books table
cursor.execute("SELECT * FROM books")
print("\n Books Table \n")
books_rows = cursor.fetchall()
for row in books_rows:
    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()