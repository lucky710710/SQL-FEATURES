# Importing SQLite library
import sqlite3

# Connecting to database
conn = sqlite3.connect('Employees_Department_Full_Outer_Join.db')
cursor = conn.cursor()

# Creating employees table
cursor.execute('''
    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name TEXT NOT NULL,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(department_id)
    );
''')

# Creating the department table
cursor.execute('''
    CREATE TABLE departments (
        department_id INTEGER PRIMARY KEY,
        department_name TEXT NOT NULL
    );
''')

# Inserting into table
cursor.executemany('''
    INSERT INTO departments (department_id, department_name) 
    VALUES (?, ?);
''', [
    (1, 'HR'),
    (2, 'Engineering'),
    (3, 'Marketing'),
    (4, 'Sales')
])

# Printing the department table
cursor.execute("Select *from departments")
print("\n Departments Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

# Inserting data intothe table
cursor.executemany('''
    INSERT INTO employees (employee_id, employee_name, department_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Lalith Kumar', 1),      
    (2, 'Yashwanth Kuntla', 2),     
    (3, 'Mahasvin', None),  
    (4, 'Swaraj Msani', 3)      
])

# Printing the table
cursor.execute("Select *from employees")
print("\n Employees Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

# Performing the join
cursor.execute('''
    SELECT employees.employee_name, departments.department_name
    FROM employees
    LEFT JOIN departments ON employees.department_id = departments.department_id

    UNION

    SELECT employees.employee_name, departments.department_name
    FROM departments
    LEFT JOIN employees ON employees.department_id = departments.department_id;
''')

print("\n Full Outer Join \n")
rows = cursor.fetchall()
for row in rows:
    print(rows)

conn.commit()
conn.close()