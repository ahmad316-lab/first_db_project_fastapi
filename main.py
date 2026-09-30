from fastapi import FastAPI
from app.routers.router import student_router


from app.models.models import Student
from app.schemas.schemas import StudentCreate
from app.utils.db import get_db

app = FastAPI()
app.include_router(student_router)