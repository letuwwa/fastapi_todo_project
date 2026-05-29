from ..tools import JSONTool
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException


router = APIRouter(prefix="/users", tags=["users"])


class User(BaseModel):
    username: str
    password: str


@router.post("/register")
def register_user(user: User):
    json_tool_instance = JSONTool("users.json")

    json_users_data = json_tool_instance.read()
    if json_users_data.get(user.username):
        raise HTTPException(status_code=409, detail="already exists")

    if len(user.password) == 0:
        raise HTTPException(status_code=400, detail="password cannot be empty")

    json_tool_instance.write_user({user.username: user.password})

    return JSONResponse(status_code=201, content={"status": "success"})
