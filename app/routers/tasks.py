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


@router.post("")
def post_task(task: CreateTask):
    users_data = JSONTool("users.json").read()
    if users_data.get(task.username) != task.password:
        raise HTTPException(status_code=401, detail="invalid credentials")

    tasks_tool_instance = JSONTool("tasks.json")
    task_data_dict = task.model_dump()
    task_data_dict.update({"task_id": str(uuid.uuid4())})
    tasks_tool_instance.write_task(task_data_dict)

    return JSONResponse(status_code=201, content={"status": "created"})

@router.delete("/{username}/{task_id:str}")
def delete_task(task_id: str, username: str):
    users_data = JSONTool("users.json").read()
    if not users_data.get(username):
        raise HTTPException(status_code=401, detail="user not found")

    tasks_tool_instance = JSONTool("tasks.json")
    tasks_tool_instance.delete_task(username=username, task_id=task_id)

    return JSONResponse(status_code=200, content={"status": "deleted"})