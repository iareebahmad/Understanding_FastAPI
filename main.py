from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()

students = {
    1 : {
        "Name" : "Mohammad Areeb Ahmad",
        "Age" : 24,
        "Gender" : "Male"
    },
    2 : {
        "Name" : "Asim Khan",
        "Age"  : 25,
        "Gender" : "Male"
    },
    3 : {
        "Name" : "Kamla Haris",
        "Age" : 36,
        "Gender" : "Female"
    }

}
@app.get("/")
def index():
    return {"Name": "First Data"}

# Path Parameter
@app.get("/get-student/{student_id}")
def get_students_info(student_id : int = Path(..., description="The ID of the student you wanna search",gt=0)):
    if student_id in students:
        return students[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student Not Found")

# Query Parameter
@app.get("/find-student")
def find_student(name : str = Query(...,description="Name of the Student to search")):
    for student in students.values():
        if student["Name"].lower() == name.lower():
            return student
    else:
            raise HTTPException(status_code=404, detail="Student Not Found")

# Combining Path and Query Parameter
@app.get("/find-student/{student_id}")
def find_student(student_id: int = Path(..., description="ID of the student to search"),
                 name: str = Query(None, description="Name to match (optional)")):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student ID not found")

    student = students[student_id]

    if name and student["Name"].lower() != name.lower():
        raise HTTPException(status_code=400, detail="Name doesn't match the student ID")

    return student
