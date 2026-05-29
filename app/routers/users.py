from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/users", tags=["users"])
FAKE_DB = {}


class User(BaseModel):
    username: str
    password: str


@router.post("/register")
def register_user(user: User):
    FAKE_DB[user.username] = user.password
    return {"message": "user registered"}
