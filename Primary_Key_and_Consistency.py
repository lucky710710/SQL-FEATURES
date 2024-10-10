# Import SQLite library
import sqlite3  

# Connect to database
conn = sqlite3.connect('Courses_Primary_Key_and_Consistency.db')
cursor = conn.cursor() 

# Create table with composite primary key
cursor.execute('''
    CREATE TABLE courses (
        course_id INTEGER,
        course_name TEXT NOT NULL,
        department_id INTEGER,
        PRIMARY KEY (course_id, department_id)
    );
''')

# Insert data into courses table
cursor.execute('''INSERT INTO courses (course_id, course_name, department_id) VALUES (101, 'Artificial Intelligence', 1);''')
cursor.execute('''INSERT INTO courses (course_id, course_name, department_id) VALUES (101, 'Artificial Intelligence', 2);''')

# Insert duplicate course_id and department_id
try:
    cursor.execute('''INSERT INTO courses (course_id, course_name, department_id) VALUES (101, 'Big Data Analytics', 1);''')
except sqlite3.IntegrityError as e:
    print("Error:", e)

# Print the current data in the courses table
print("\nCourses table:")
cursor.execute('SELECT * FROM courses')
for row in cursor.fetchall():
    print(row)

# Commit and close the connection
conn.commit()
conn.close()