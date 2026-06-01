from storage.engine import StorageEngine

storage = StorageEngine()

MODULES = {
    "1": "tickets.json",
    "2": "machines.json",
    "3": "users.json"
}


def main_menu():
    print("\n==============================")
    print("        CMMS SYSTEM")
    print("==============================")
    print("1. Tickets")
    print("2. Machines")
    print("3. Users")
    print("4. Exit")
    print("==============================")


def module_menu(name):
    print(f"\n====== {name.upper()} MENU ======")
    print("1. Load Data")
    print("2. Find by ID")
    print("3. Update by ID")
    print("4. Delete by ID")
    print("5. Back")


def run_module(file):
    while True:
        module_menu(file)

        choice = input("Enter choice: ")

        if choice == "1":
            print(storage.load_data(file))

        elif choice == "2":
            try:
                rid = int(input("Enter ID: "))
            except ValueError:
                print("Please enter a numeric ID.")
                continue

            print(storage.find_by_id(file, rid))

        elif choice == "3":
            try:
                rid = int(input("Enter ID: "))
            except ValueError:
                print("Please enter a numeric ID.")
                continue

            key = input("Field to update: ")
            value = input("New value: ")

            print(storage.update_by_id(file, rid, {key: value}))

        elif choice == "4":
            try:
                rid = int(input("Enter ID: "))
            except ValueError:
                print("Please enter a numeric ID.")
                continue

            print(storage.delete_by_id(file, rid))

        elif choice == "5":
            break

        else:
            print("Invalid choice")

def run():
    while True:
        main_menu()
        choice = input("Select module: ")

        if choice in MODULES:
            run_module(MODULES[choice])

        elif choice == "4":
            print("Exiting CMMS...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    run()