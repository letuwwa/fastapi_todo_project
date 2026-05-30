# FastAPI Todo Project

## Run

Install dependencies:
```bash
uv sync
```

Start the API:
```bash
uv run uvicorn app.main:app --reload
```

Open:
```text
http://127.0.0.1:8000/docs
```

## Endpoints
- `GET /` - health check
- `POST /users/register` - register a user
- `POST /tasks` - create a task
- `POST /tasks/{username}` - get user tasks
- `PUT /tasks/done/{username}` - mark a task as done
- `DELETE /tasks/{username}` - delete a task
