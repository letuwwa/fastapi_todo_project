import requests


BASE_URL = "http://127.0.0.1:8000"
USERNAME = "demo_user"
PASSWORD = "demo_password"


def send_request(
    method: str, path: str, data: dict | None = None, params: dict | None = None
):
    url = f"{BASE_URL}{path}"
    try:
        response = requests.request(method, url, json=data, params=params)
        response_body = response.json() if response.content else None
        return response.status_code, response_body
    except ValueError:
        return response.status_code, response.text


def print_result(title: str, status_code: int | None, response_body):
    print(f"\n{title}")
    print(f"status: {status_code}")
    print(f"response: {response_body}")


def main():
    status_code, response_body = send_request(
        "POST",
        "/users/register",
        {
            "username": USERNAME,
            "password": PASSWORD,
        },
    )
    print_result("Register user", status_code, response_body)

    status_code, response_body = send_request(
        "POST",
        "/tasks",
        {
            "description": "Learn FastAPI",
            "is_done": False,
            "username": USERNAME,
            "password": PASSWORD,
        },
    )
    print_result("Create task", status_code, response_body)

    status_code, response_body = send_request(
        "POST",
        f"/tasks/{USERNAME}",
        {
            "password": PASSWORD,
        },
    )
    print_result("Get user tasks", status_code, response_body)

    if not response_body:
        return

    task_id = response_body[0]["task_id"]

    status_code, response_body = send_request(
        "PUT",
        f"/tasks/done/{USERNAME}",
        params={"task_id": task_id},
    )
    print_result("Mark task as done", status_code, response_body)

    status_code, response_body = send_request(
        "DELETE",
        f"/tasks/{USERNAME}",
        params={"task_id": task_id},
    )
    print_result("Delete task", status_code, response_body)


if __name__ == "__main__":
    main()
