from fastapi import APIRouter


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
def tasks_check():
    return {"url": "/tasks"}
