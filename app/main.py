from fastapi import FastAPI
from .routers import user_router, task_router


app = FastAPI()
app.include_router(user_router)
app.include_router(task_router)


@app.get("/")
def root():
    return {"message": "Hello"}
