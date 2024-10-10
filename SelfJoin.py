# Importing the SQLite library
import sqlite3

# Connecting to the SQLite database
conn = sqlite3.connect('Employees_Self_Join.db')
cursor = conn.cursor()

# Creating the employees table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY, 
        employee_name TEXT NOT NULL,      
        manager_id INTEGER,           
        FOREIGN KEY (manager_id) REFERENCES employees(employee_id) 
    );
''')

# Inserting records into employees table
cursor.executemany(''' 
    INSERT INTO employees (employee_id, employee_name, manager_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Lalith Kumar', None),       
    (2, 'Yashwanth Kuntla', 1),       
    (3, 'Swaraj Msani', 1),  
    (4, 'Mahasvin', 2),       
    (5, 'Hruthwik', 2),  
    (6, 'Mahesh Babu', 3)      
])

# Selecting all records from employees
cursor.execute("SELECT * FROM employees")
print("\n Employees Table\n")
rows = cursor.fetchall() 
for row in rows:
    print(row)

# Performing self join
cursor.execute('''
    SELECT e.employee_name AS Employee, m.employee_name AS Manager
    FROM employees e
    LEFT JOIN employees m ON e.manager_id = m.employee_id; 
''')

# Fetching results of self join
rows = cursor.fetchall()
print("\n Self Join \n")
for row in rows:
    print(row)

# Committing changes and closing connection
conn.commit()
conn.close()