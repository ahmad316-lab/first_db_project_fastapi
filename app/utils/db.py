from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.Config import settings
from app.models.models import Base

engine = create_engine(settings.db_url)
Base.metadata.create_all(engine)

with engine.connect() as conn:
    print("DB Connect Successfully")

LocalSession = sessionmaker(bind=engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

