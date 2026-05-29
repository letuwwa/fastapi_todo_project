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

    def write(self, data: dict):
        past_data = self.read()
        past_data.update(data)
        with open(self.filename, "w") as f:
            json.dump(past_data, f, indent=4)
