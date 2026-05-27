from ticket_manager import TicketManager


tm = TicketManager()


def validate_access(role, action):

    permissions = {

        "OPERATOR": [
            "CREATE",
            "VIEW"
        ],

        "MAINTENANCE": [
            "VIEW",
            "ASSIGN",
            "CLOSE"
        ],

        "ADMIN": [
            "CREATE",
            "VIEW",
            "ASSIGN",
            "CLOSE",
            "REPORT"
        ]
    }

    allowed_actions = permissions.get(role, [])

    return action in allowed_actions


def create_ticket_handler():

    role = input("Enter Role: ").upper()

    if not validate_access(role, "CREATE"):
        print("Access Denied")
        return

    ticket_id = input("Enter Ticket ID: ")
    machine_id = input("Enter Machine ID: ")
    description = input("Enter Description: ")
    reported_by = input("Reported By: ")

    tm.create_ticket(
        ticket_id,
        machine_id,
        description,
        reported_by
    )


def view_tickets_handler():

    role = input("Enter Role: ").upper()

    if not validate_access(role, "VIEW"):
        print("Access Denied")
        return

    tm.list_tickets()


def assign_ticket_handler():

    role = input("Enter Role: ").upper()

    if not validate_access(role, "ASSIGN"):
        print("Access Denied")
        return

    ticket_id = input("Enter Ticket ID: ")
    technician = input("Assign To: ")

    tm.assign_ticket(
        ticket_id,
        technician
    )


def close_ticket_handler():

    role = input("Enter Role: ").upper()

    if not validate_access(role, "CLOSE"):
        print("Access Denied")
        return

    ticket_id = input("Enter Ticket ID: ")
    closed_by = input("Closed By: ")
    root_cause = input("Root Cause: ")
    resolution_notes = input("Resolution Notes: ")

    tm.close_ticket(
        ticket_id,
        closed_by,
        root_cause,
        resolution_notes
    )


def menu():

    while True:

        print("\n===== SHIFTDESK CMMS =====")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Assign Ticket")
        print("4. Close Ticket")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            create_ticket_handler()

        elif choice == "2":
            view_tickets_handler()

        elif choice == "3":
            assign_ticket_handler()

        elif choice == "4":
            close_ticket_handler()

        elif choice == "5":
            print("Exiting System")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()