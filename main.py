from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory buffer (simulating a database)
students: Dict[int, dict] = {}

# Pydantic model
class Student(BaseModel):
    id: int
    name: str
    city: str

@app.post("/students", response_model=Student)
def create_student(student: Student):
    if student.id in students:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    # print(student.dict()['name'])
    existing_names = [a["name"] for a in students.values()]
    print(f"-----------------{existing_names}")
    if student.name in existing_names:
        raise HTTPException(status_code=400, detail="Student name already exists")
    # print(students)
    students[student.id] = student.dict()
    # print(students)
    print(student.dict()['name'])
    
    
    return student

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

@app.get("/students", response_model=list[Student])
def list_students():
    return list(students.values())

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    if student_id != student.id:
        raise HTTPException(status_code=400, detail="ID in path and body must match")
    students[student_id] = student.dict()
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": f"Student with id {student_id} deleted"}

# 👇 This makes it executable with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)





# app/main.py

# from fastapi import FastAPI
# from db import engine, metadata
# from routes import users

# import logging

# app = FastAPI()

# # Setup logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# # Include user routes
# app.include_router(users.router, prefix="/api/v1")

# @app.on_event("startup")
# async def startup_event():
#     try:
#         metadata.create_all(bind=engine)www
#         logger.info("Tables created successfully.")
#     except Exception as e:
#         logger.error("Failed to create tables!", exc_info=True)

# @app.on_event("shutdown")
# async def shutdown_event():
#     logger.info("Shutting down application...")


