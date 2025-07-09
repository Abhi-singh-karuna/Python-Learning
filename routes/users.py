# app/routes/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def get_users():
    return {"message": "Hello, World!"}
