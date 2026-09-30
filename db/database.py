from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "postgresql+psycopg://postgres:1240@localhost:5432/student_db"


engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

with engine.connect() as connection:
    print("Database connected successfully!")

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()