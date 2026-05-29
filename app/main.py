from fastapi import FastAPI
from app import routers as basic_routers


app = FastAPI()
app.include_router(basic_routers.router)


@app.get("/")
def root():
    return {"message": "Hello"}
