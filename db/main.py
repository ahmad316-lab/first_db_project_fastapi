from fastapi import FastAPI, Depends
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schema import StudentCreate

app = FastAPI()


@app.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = Student(
        name=student.name,
        email=student.email,
        age=student.age
    )

    db.add(new_student)
    db.commit()

    return {
        "message": "Student created successfully"
    }


@app.get("/students/{s_id}")
def get_students(s_id: int,  db: Session = Depends(get_db)):
    # statement = select(Student).order_by(Student.name.desc())
    # statement = select(Student).limit(3)
    # statement = select(Student).where(Student.age > 21).order_by(Student.age.desc())
    # statement = select(Student.name)
    # statement = select(Student.name, Student.email)
    # statement = select(Student.name).where(Student.age > 21)
    statement = select(Student.name).where(Student.id == s_id)



    result = db.execute(statement)

    students = result.first()

    return students


@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    statement = (
        update(Student)
        .where(Student.id == student_id)
        .values(
            name=student.name,
            email=student.email,
            age=student.age
        )
    )

    db.execute(statement)
    db.commit()

    return {
        "message": "Student updated successfully"
    }

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    statement = delete(Student).where(
        Student.id == student_id
    )

    db.execute(statement)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }