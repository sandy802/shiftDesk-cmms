from Storage.engine import StorageEngine

storage = StorageEngine()

print("\n--- FIND TEST ---")
print(storage.find_by_id("tickets.json", 1001))

print("\n--- UPDATE TEST ---")
print(storage.update_by_id("tickets.json", 1001, {"status": "In Progress"}))

print("\n--- DELETE TEST ---")
print(storage.delete_by_id("tickets.json", 1001))

print("\n--- FINAL DATA CHECK ---")
print(storage.load_data("tickets.json"))