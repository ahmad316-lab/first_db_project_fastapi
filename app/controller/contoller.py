from fastapi import Depends
from app.utils.db import get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import StudentCreate
from app.models.models import Student
from sqlalchemy import select, update, delete
from app.errors.error import StudentNotFound


def create_student(student: StudentCreate, db: Session):
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

def get_students(
    search: str | None,
    min_age: int | None,
    max_age: int | None,
    db: Session
):
    stmt = select(Student)

    if search is not None:
        stmt = stmt.where(
            Student.name.ilike(f"%{search}%")
        )

    if min_age is not None:
        stmt = stmt.where(
            Student.age >= min_age
        )

    if max_age is not None:
        stmt = stmt.where(
            Student.age <= max_age
        )

    res = db.execute(stmt)

    students = res.scalars().all()

    return students


def get_student_by_id(s_id: int, db: Session ):

    query = select(Student).where(Student.id == s_id)
    
    res = db.execute(query)

    st = res.scalars().first()

    if st is None:
        raise StudentNotFound
    
    return st




def update_student(s_id: int, student: StudentCreate, db: Session ):
    st = update(Student).where(Student.id == s_id).values(
        name = student.name,
        email = student.email,
        age = student.age,
    )

    res =  db.execute(st)
    if res.rowcount == 0:
            raise StudentNotFound
    
    db.commit()

    return {
        "message" : "Updated"
    }


def delete_student(s_id: int, db: Session ):
    st = delete(Student).where(Student.id == s_id)

    res = db.execute(st)
    if res.rowcount == 0:
            raise StudentNotFound
    db.commit()

    return {
        "message" : "Deleted"
    }





