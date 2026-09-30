from fastapi import FastAPI


from app.models.models import Student
from app.schemas.schemas import StudentCreate
from app.utils.db import get_db

app = FastAPI()