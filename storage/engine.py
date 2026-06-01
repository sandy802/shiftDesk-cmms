import json
from pathlib import Path


class StorageEngine:

    def __init__(self):
        self.data_path = Path("data")

    def _get_id_key(self, record):
        """Auto detect ID field"""
        if "id" in record:
            return "id"
        if "machine_id" in record:
            return "machine_id"
        if "user_id" in record:
            return "user_id"
        return None
    

    def load_data(self, filename):

        file_path = self.data_path / filename

        if not file_path.exists():
            return []

        with open(file_path, "r") as file:
            return json.load(file)

    def save_data(self, filename, data):
        file_path = self.data_path / filename

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def find_by_id(self, filename, record_id):
        records = self.load_data(filename)

        for record in records:
            key = self._get_id_key(record)
            if key and record.get(key) == record_id:
                return record

        return None

    def update_by_id(self, filename, record_id, updates):
        records = self.load_data(filename)

        for i, record in enumerate(records):
            key = self._get_id_key(record)
            if key and record.get(key) == record_id:
                records[i].update(updates)
                self.save_data(filename, records)
                return records[i]

        return None

    def delete_by_id(self, filename, record_id):
        records = self.load_data(filename)

        new_records = []
        found = False

        for record in records:
            key = self._get_id_key(record)
            if key and record.get(key) == record_id:
                found = True
                continue
            new_records.append(record)

        if not found:
            return None

        self.save_data(filename, new_records)
        return True