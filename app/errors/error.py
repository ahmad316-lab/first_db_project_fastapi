from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

class StudentNotFound(Exception):
    pass

@app.exception_handler()
async def student_not_found ( req: Request, exc: StudentNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content="Student Not Found"
    )
