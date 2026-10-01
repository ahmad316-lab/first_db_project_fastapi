from fastapi import APIRouter, status, Depends
from app.utils.db import get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import StudentCreate
from app.controller import contoller


student_router = APIRouter()


@student_router.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db : Session = Depends(get_db)):
    return contoller.create_student(student, db)

@student_router.get("/students")
def get_students(
    search: str | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
    db: Session = Depends(get_db)
):
    return contoller.get_students(
        search,
        min_age,
        max_age,
        db
    )

@student_router.get("/students/{st_id}", status_code=status.HTTP_200_OK)
def get_student_by_id(st_id: int, db : Session = Depends(get_db)):
    return contoller.get_student_by_id(st_id, db)

@student_router.put("/students/{st_id}", status_code=status.HTTP_200_OK)
def update_student(st_id: int, st: StudentCreate, db : Session = Depends(get_db)):
    return contoller.update_student(st_id, st, db)

@student_router.delete("/students/{st_id}", status_code=status.HTTP_200_OK)
def delete_student(st_id: int, db : Session = Depends(get_db)):
    return contoller.delete_student(st_id, db)




