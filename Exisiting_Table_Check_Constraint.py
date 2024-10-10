# Import the SQLite library
import sqlite3

# Connect to the existing
conn = sqlite3.connect('Employee_Exisiting_Table_Check_Constrain.db')
cursor = conn.cursor()  # Create a cursor object

# Display the data in the employees table
cursor.execute('select * from employees')
print(cursor.fetchall())

# Insert a record with a negative salary
try:
    cursor.execute('INSERT INTO employees (employee_id, employee_name, salary) VALUES (3, "Lucky", -80000);')
except sqlite3.IntegrityError as e:
    print("Error:", e)

# Commit and close the connection
conn.commit()
conn.close()