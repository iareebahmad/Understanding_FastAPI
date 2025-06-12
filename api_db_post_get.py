# This app uses fastapi for get/post methods on the postgresql db
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

class Student(BaseModel):
    name: str
    age: int

app = FastAPI()

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="postgres",
    password="root",
    port="5432"
)
cur = conn.cursor()

@app.post("/students")
def create_student(student: Student):
    cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (student.name, student.age))
    conn.commit()
    return {"msg": f"Student {student.name} added successfully"}

@app.get("/students")
def get_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    return {"students": rows}
