import json


class JSONTool:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def write_user(self, data: dict):
        past_data = self.read()
        past_data.update(data)
        with open(self.filename, "w") as f:
            json.dump(past_data, f, indent=4)

    def write_task(self, data: dict):
        past_data = self.read()
        if not past_data or past_data.get(data["username"]) is None:
            past_data[data["username"]] = [
                {"id": data["id"], "description": data["description"], "is_done": data["is_done"]},
            ]
        else:
            past_data[data["username"]].append(
                {"id": data["id"], "description": data["description"], "is_done": data["is_done"]},
            )
        with open(self.filename, "w") as f:
            json.dump(past_data, f, indent=4)

    def delete_task(self, username: str, task_id: str):
        past_data = self.read()
        past_data[username] = [task for task in past_data[username] if task["id"] != task_id]
        with open(self.filename, "w") as f:
            json.dump(past_data, f, indent=4)