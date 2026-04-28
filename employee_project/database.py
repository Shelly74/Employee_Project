import sqlite3

def connect():
    conn = sqlite3.connect("employee.db")
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        department TEXT,
        salary REAL
    )
    """)

    conn.commit()
    conn.close()

def insert(name, age, dept, salary):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)",
        (name, age, dept, salary)
    )

    conn.commit()
    conn.close()

def fetch():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    conn.close()
    return rows

def update(emp_id, name, age, dept, salary):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE employees
        SET name=?, age=?, department=?, salary=?
        WHERE id=?
    """, (name, age, dept, salary, emp_id))

    conn.commit()
    conn.close()

def delete(emp_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))

    conn.commit()
    conn.close()

def search(name=""):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()

    conn.close()
    return rows
