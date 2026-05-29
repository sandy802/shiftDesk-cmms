from Storage import storageEngine

storage = storageEngine

storage.save_data("users.json", [{"name": "Sandesh"}])

data = storage.load_data("users.json")

print("OUTPUT:", data)