#Importing SQLite library
import sqlite3  

# Connect to database
conn = sqlite3.connect('Students_Foreign_Key.db')
cursor = conn.cursor()

# Enable foreign key constraint enforcement
cursor.execute('PRAGMA foreign_keys = ON;')

# Create a table with a primary key
cursor.execute('''CREATE TABLE students (
    student_id INTEGER PRIMARY KEY, 
    student_name TEXT NOT NULL);''')

# Create courses table with a composite primary key
cursor.execute('''CREATE TABLE courses (
    course_id INTEGER, 
    course_name TEXT NOT NULL, 
    department_id INTEGER, 
    PRIMARY KEY (course_id, department_id));''')

# Create student_courses table with foreign key references
cursor.execute('''CREATE TABLE student_courses (
    student_id INTEGER,
    course_id INTEGER,
    department_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id, department_id) REFERENCES courses(course_id, department_id) ON DELETE CASCADE,
    PRIMARY KEY (student_id, course_id, department_id));''')

# Insert data into students and courses tables
cursor.execute('INSERT INTO students (student_id, student_name) VALUES (1, "Lalith Kumar");')
cursor.execute('INSERT INTO students (student_id, student_name) VALUES (2, "Yashnwanth Kuntla");')
cursor.execute('INSERT INTO courses (course_id, course_name, department_id) VALUES (101, "Artificial Intelligence", 1);')
cursor.execute('INSERT INTO courses (course_id, course_name, department_id) VALUES (102, "Big Data Analytics", 1);')

# Insert data into student_courses table
cursor.execute('INSERT INTO student_courses (student_id, course_id, department_id) VALUES (1, 101, 1);')
cursor.execute('INSERT INTO student_courses (student_id, course_id, department_id) VALUES (2, 102, 1);')

# Display the current data in the student_courses table
print("\nCurrent data in the student_courses table:")
cursor.execute('SELECT * FROM student_courses')
for row in cursor.fetchall():
    print(row)

# Attempt to insert invalid data for student_id
cursor.execute('INSERT INTO student_courses (student_id, course_id, department_id) VALUES (3, 101, 1);')

# Attempt to insert invalid data for course_id
cursor.execute('INSERT INTO student_courses (student_id, course_id, department_id) VALUES (1, 103, 1);')

# Commit and close the connection
conn.commit()
conn.close()