from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

class StudentNotFound(Exception):
    pass

@app.exception_handler(StudentNotFound)
async def student_not_found_exception_handler(request: Request, exc: StudentNotFound):
    return JSONResponse(
        status_code=404,
        content={"message": f"Student not found error: {str(exc)}"},
    )
