from fastapi import FastAPI, HTTPException
from models import Student, Feedback
from database import students
from nlp_utils import analyze_sentiment, smart_search
from uuid import uuid4

app = FastAPI(
    title="AI-Powered Student RESTful API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "API is running"}   # removed extra space



@app.post("/students")
def create_student(student: Student):
    student_id = str(uuid4())
    student_dict = student.dict()
    student_dict["id"] = student_id
    students.append(student_dict)

    return {
        "message": "Student created",
        "student": student_dict
    }



@app.get("/students")
def get_students():
    return {"students": students}



@app.get("/students/{student_id}")
def get_student(student_id: str):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")



@app.put("/students/{student_id}")
def update_student(student_id: str, updated_student: Student):
    for student in students:
        if student["id"] == student_id:
            student.update(updated_student.dict())
            return {
                "message": "Student updated",
                "student": student
            }

    raise HTTPException(status_code=404, detail="Student not found")



@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student deleted"}

    raise HTTPException(status_code=404, detail="Student not found")



@app.post("/feedback")
def analyze_feedback(feedback: Feedback):
    result = analyze_sentiment(feedback.text)

    return {
        "text": feedback.text,
        "analysis": result
    }



@app.get("/search")
def search_student(query: str):
    results = smart_search(students, query)

    if not results:
        raise HTTPException(status_code=404, detail="No matching students found")

    return {"count": len(results), "students": results}
