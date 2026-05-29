import uuid
from ..tools import JSONTool
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException


router = APIRouter(prefix="/tasks", tags=["tasks"])


class Task(BaseModel):
    description: str
    is_done: bool
    username: str
    password: str
    id: str = str(uuid.uuid4())


@router.post("")
def post_task(task: Task):
    users_data = JSONTool("users.json").read()
    if users_data.get(task.username) != task.password:
        raise HTTPException(status_code=401, detail="invalid credentials")

    tasks_tool_instance = JSONTool("tasks.json")
    tasks_tool_instance.write_task(task.model_dump())

    return JSONResponse(status_code=201, content={"status": "created"})
