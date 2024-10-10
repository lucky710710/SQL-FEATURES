# Import SQLite library
import sqlite3

# Connect to the database
conn = sqlite3.connect('Students_Composite_Key_Constraint.db')
cursor = conn.cursor()

# Create students table
cursor.execute('''CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL);''')

# Create courses table
cursor.execute('''CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL);''')

# Create student_courses table with a composite primary key
cursor.execute('''CREATE TABLE student_courses (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id));''')

# Inserting data into the students table
cursor.execute('INSERT INTO students (student_id, student_name) VALUES (1, "Lalith Kumar");')
cursor.execute('INSERT INTO students (student_id, student_name) VALUES (2, "Yashwanth Kuntla");')

# Inserting data into the courses table
cursor.execute('INSERT INTO courses (course_id, course_name) VALUES (101, "Artificial Intelligence");')
cursor.execute('INSERT INTO courses (course_id, course_name) VALUES (102, "Big Data Analytics");')

# Inserting data into student_courses table 
cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (1, 1023);')
cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (2, 1011);')

# Display the data in the student_courses table
print("\nCurrent data in the student_courses table:")
cursor.execute('SELECT * FROM student_courses')
for row in cursor.fetchall():
    print(row)

# Insert duplicate data with student_id and course_id 
try:
    cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (1, 1023);') 
except sqlite3.IntegrityError as e:
    print("Error:", e)  

# Inserting another record with a different course_id for the same student_id
cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (1, 1011);')

# Commit and close the connection
conn.commit()
conn.close()