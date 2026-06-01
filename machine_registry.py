import datetime
from storage.engine import StorageEngine
import os
import csv 

class MachineRegistry:

    def __init__(self):
        self.storage = StorageEngine() 
        self.breakdown_types = set()

    # ADD MACHINE 

    def add_machine(self,code,name,location_id):
        machine = self.storage.load_data("machines.json")

        for m in machine:
            if m["machine_id"] == code:
                raise Exception("Machine code already exists")
            
        new_machine ={
            "machine_id" : code,
            "machine_name" : name,
            "location_id" : "location_id",
            "status" : "Active",
            "is_active" : True,
            "created_at" : str(datetime.date.today())
        }
    

        machine.append(new_machine)
        self.storage.save_data("machines.json", machine)

        return new_machine


 # LIST MACHINES 

    def list_machines(self):
        machine = self.storage.load_data("machines.json")

        return [m for m in machine if m.get("is_active", True)]

# UPDATE MACHINES 

    # UPDATE MACHINE
    def update_machine(self, machine_id, name=None, location_id=None):
        machines = self.storage.load_data("machines.json")

        for m in machines:
            if m["machine_id"] == machine_id:

                if name:
                    m["machine_name"] = name

                if location_id:
                    m["location_id"] = location_id

                self.storage.save_data("machines.json", machines)
                return m

        raise Exception("Machine not found")     
            

# DEACTIVATE MACHINES 

    def deactivate_machine(self, machine_id):
        machines = self.storage.load_data("machines.json")

        for m in machines:
            if m["machine_id"] == machine_id:
                m["is_active"] = False
                m["status"] = "inactive"

                self.storage.save_data("machines.json", machines)
                return m

        raise Exception("Machine not found")
# BREAKDOWN TYPE

    def add_breakdown_type(self , name):
        self.add_breakdown_types.add(name)
        return list (self.breakdwon_types)
    
    def list_breakdown_types(self):
        return list(self.breakdown_types)
        

    def export_machines_csv(self, filepath="outputs/machines.csv"):
     machines = self.storage.load_data("machines.json")

     os.makedirs(os.path.dirname(filepath), exist_ok=True)

     with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "machine_id",
            "machine_name",
            "location_id",
            "status",
            "is_active",
            "created_at"
        ])

        writer.writeheader()

        for m in machines:
            writer.writerow({
                "machine_id": m.get("machine_id"),
                "machine_name": m.get("machine_name"),
                "location_id": m.get("location_id"),
                "status": m.get("status"),
                "is_active": m.get("is_active"),
                "created_at": m.get("created_at")
            })

     return filepath

if __name__ == "__main__":

    registry = MachineRegistry()

    # test add machine (optional)
    registry.add_machine("", "", "")

    machines = registry.list_machines()
    print("\n=== MACHINES ===")
    for m in machines:
        print(m)

    # export CSV test
    file_path = registry.export_machines_csv()
    print("CSV created at:", file_path)




if __name__ == "__main__":

    registry = MachineRegistry()

    while True:
        print("\n===== MACHINE REGISTRY =====")
        print("1. Add Machine")
        print("2. List Machines")
        print("3. Update Machine")
        print("4. Deactivate Machine")
        print("5. Export CSV")
        print("6. Exit")

        choice = input("Enter choice: ")

        # -------------------------
        # ADD MACHINE
        # -------------------------
        if choice == "1":
            code = input("Enter Machine ID: ")
            name = input("Enter Machine Name: ")
            location = input("Enter Location ID: ")

            try:
                result = registry.add_machine(code, name, location)
                print("Machine Added:", result)
            except Exception as e:
                print("Error:", e)

        # -------------------------
        # LIST MACHINES
        # -------------------------
        elif choice == "2":
            machines = registry.list_machines()

            print("\nID\tNAME\tLOCATION\tSTATUS")
            for m in machines:
                print(f"{m['machine_id']}\t{m['machine_name']}\t{m['location_id']}\t{m['status']}")

        # -------------------------
        # UPDATE MACHINE
        # -------------------------
        elif choice == "3":
            mid = input("Enter Machine ID: ")
            name = input("New Name (press enter to skip): ")
            loc = input("New Location (press enter to skip): ")

            name = name if name.strip() != "" else None
            loc = loc if loc.strip() != "" else None

            try:
                updated = registry.update_machine(mid, name, loc)
                print("Updated:", updated)
            except Exception as e:
                print("Error:", e)

        # -------------------------
        # DEACTIVATE MACHINE
        # -------------------------
        elif choice == "4":
            mid = input("Enter Machine ID: ")

            try:
                result = registry.deactivate_machine(mid)
                print("Deactivated:", result)
            except Exception as e:
                print("Error:", e)

        # -------------------------
        # EXPORT CSV
        # -------------------------
        elif choice == "5":
            path = registry.export_machines_csv()
            print("CSV Created at:", path)

        # -------------------------
        # EXIT
        # -------------------------
        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

import pandas as pd

df = pd.read_csv("outputs/machines.csv")
print(df)