import json
from pathlib import Path


class StorageEngine:

    def __init__(self):
        self.data_path = Path("data")

    def save_data(self, filename, data):
        file_path = self.data_path / filename

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self, filename):
        file_path = self.data_path / filename

        if not file_path.exists():
            return []

        with open(file_path, "r") as file:
            return json.load(file)