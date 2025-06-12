# This script connects python to Postgresql
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="postgres",
    password="root",
    port="5432"
)
# Taking custom input
name = input("Enter the name to be entered : ")
age = input("Enter the age to be entered : ")

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")

# Insert a record
cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name,age))

# Commit the transaction
conn.commit()

# Fetch and display records
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close cursor and connection
cur.close()
conn.close()
