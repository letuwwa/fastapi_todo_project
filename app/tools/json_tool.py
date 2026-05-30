import json


class JSONTool:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, "rb") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def write(self, data: dict):
        with open(self.filename, "wb") as f:
            json_data = json.dumps(data, indent=4)
            f.write(json_data.encode("utf-8"))

    def write_user(self, data: dict):
        past_data = self.read()
        past_data.update(data)
        self.write(past_data)

    def write_task(self, data: dict):
        past_data = self.read()
        if not past_data or past_data.get(data["username"]) is None:
            past_data[data["username"]] = [
                {
                    "task_id": data["task_id"],
                    "description": data["description"],
                    "is_done": data["is_done"],
                },
            ]
        else:
            past_data[data["username"]].append(
                {
                    "task_id": data["task_id"],
                    "description": data["description"],
                    "is_done": data["is_done"],
                },
            )
        self.write(past_data)

    def delete_task(self, username: str, task_id: str):
        past_data = self.read()
        past_data[username] = [
            task for task in past_data[username] if task["task_id"] != task_id
        ]
        self.write(past_data)

    def update_task_done(self, username: str, task_id: str):
        past_data = self.read()
        if past_data.get(username):
            for task in past_data[username]:
                if task["task_id"] == task_id:
                    task["is_done"] = True
                    break
            self.write(past_data)
