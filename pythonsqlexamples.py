//Connect to sql and bring data from database.
import sqlite3

# Create a connection to the SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY,
                   name TEXT,
                   department TEXT,
                   salary REAL)''')

# Insert some data into the table
cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
               ("Alice", "HR", 50000))
cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
               ("Bob", "Engineering", 60000))
cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
               ("Charlie", "Sales", 55000))

# Commit the changes to the database
conn.commit()

# Execute an SQL query
cursor.execute("SELECT * FROM employees WHERE department=?", ("HR",))

# Fetch and print the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
