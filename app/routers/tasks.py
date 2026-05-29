import uuid
from ..tools import JSONTool
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException


router = APIRouter(prefix="/tasks", tags=["tasks"])


class CreateTask(BaseModel):
    description: str
    is_done: bool
    username: str
    password: str
    task_id: str = str(uuid.uuid4())


class UserCreds(BaseModel):
    username: str
    password: str


@router.post("")
def post_task(task: CreateTask):
    users_data = JSONTool("users.json").read()
    if users_data.get(task.username) != task.password:
        raise HTTPException(status_code=401, detail="invalid credentials")

    tasks_tool_instance = JSONTool("tasks.json")
    tasks_tool_instance.write_task(task.model_dump())

    return JSONResponse(status_code=201, content={"status": "created"})

@router.delete("/{task_id}")
def delete_task(task_id: str, user: UserCreds):
    users_data = JSONTool("users.json").read()
    if users_data.get(user.username) != user.password:
        raise HTTPException(status_code=401, detail="invalid credentials")

    tasks_tool_instance = JSONTool("tasks.json")
    tasks_tool_instance.delete_task(username=user.username, task_id=task_id)

    return JSONResponse(status_code=200, content={"status": "deleted"})