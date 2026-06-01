import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from storage.engine import StorageEngine

storage = StorageEngine()

print("Seed file working")


# ---------------- MACHINES ----------------

machines = [
    {
        "machine_id": 101,
        "machine_name": "CNC Machine",
        "status": "Running",
        "location": "Plant A"
    },
    {
        "machine_id": 102,
        "machine_name": "Conveyor Belt",
        "status": "Maintenance",
        "location": "Plant B"
    },
    {
        "machine_id": 103,
        "machine_name": "Hydraulic Press",
        "status": "Idle",
        "location": "Plant A"
    },
    {
        "machine_id": 104,
        "machine_name": "Cooling System",
        "status": "Running",
        "location": "Warehouse"
    },
    {
        "machine_id": 105,
        "machine_name": "Packaging Unit",
        "status": "Stopped",
        "location": "Plant B"
    }
]


# ---------------- USERS ----------------

users = [
    {
        "user_id": 1,
        "name": "Sandesh",
        "role": "Admin"
    },
    {
        "user_id": 2,
        "name": "Rahul",
        "role": "Technician"
    },
    {
        "user_id": 3,
        "name": "Priya",
        "role": "Manager"
    }
]


# ---------------- BREAKDOWN TYPES ----------------

breakdown_types = [
    {
        "breakdown_id": 1,
        "type": "Electrical Failure"
    },
    {
        "breakdown_id": 2,
        "type": "Mechanical Failure"
    },
    {
        "breakdown_id": 3,
        "type": "Overheating"
    },
    {
        "breakdown_id": 4,
        "type": "Sensor Fault"
    }
]


# ---------------- LOCATIONS ----------------

locations = [
    {
        "location_id": 1,
        "name": "Plant A"
    },
    {
        "location_id": 2,
        "name": "Plant B"
    },
    {
        "location_id": 3,
        "name": "Warehouse"
    }
]


# ---------------- SAVE DATA ----------------

storage.save_data("machines.json", machines)
storage.save_data("users.json", users)
storage.save_data("breakdown_types.json", breakdown_types)
storage.save_data("locations.json", locations)

print("Seed data added successfully!")