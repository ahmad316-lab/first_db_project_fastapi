from fastapi import Depends
from app.utils.db import get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import StudentCreate
from app.models.models import Student
from sqlalchemy import select, update, delete


def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    student = Student(
        name = student.name,
        email = student.email,
        age = student.age,
    )

    db.add(student)
    db.commit()

    return {
        "message" : "Created"
    }

def get_students( db: Session = Depends(get_db)):

    query = select(Student)

    res = db.execute(query)

    return res.scalars().all()


def get_student_by_id(s_id: int, db: Session = Depends(get_db)):

    query = select(Student).where(Student.id == s_id)
    
    res = db.execute(query)


    
    return res.scalars().first()




def update_student(s_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    st = update(Student).where(Student.id == s_id).values(
        name = student.name,
        email = student.email,
        age = student.age,
    )

    db.execute(st)
    db.commit()

    return {
        "message" : "Updated"
    }


def delete_student(s_id: int, db: Session = Depends(get_db)):
    st = delete(Student).where(Student.id == s_id)

    db.execute(st)
    db.commit()

    return {
        "message" : "Deleted"
    }


