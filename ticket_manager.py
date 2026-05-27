from datetime import datetime
from models import Ticket


class TicketManager:

    def __init__(self):
        self.tickets = []

    def create_ticket(
        self,
        ticket_id,
        machine_id,
        description,
        reported_by
    ):

        ticket = Ticket(
            ticket_id=ticket_id,
            machine_id=machine_id,
            description=description,
            status="OPEN",
            reported_by=reported_by,
            reported_at=datetime.now()
        )

        self.tickets.append(ticket)

        print(f"Ticket {ticket_id} created successfully")

    def assign_ticket(self, ticket_id, technician_name):

        for ticket in self.tickets:

            if ticket.ticket_id == ticket_id:

                ticket.status = "IN_PROGRESS"
                ticket.assigned_to = technician_name
                ticket.assigned_at = datetime.now()

                print(f"Ticket {ticket_id} assigned")

                return

        print("Ticket not found")

    def close_ticket(
        self,
        ticket_id,
        closed_by,
        root_cause,
        resolution_notes
    ):

        for ticket in self.tickets:

            if ticket.ticket_id == ticket_id:

                ticket.status = "CLOSED"
                ticket.closed_by = closed_by
                ticket.closed_at = datetime.now()
                ticket.root_cause = root_cause
                ticket.resolution_notes = resolution_notes

                print(f"Ticket {ticket_id} closed")

                return

        print("Ticket not found")

    def list_tickets(self):

        if not self.tickets:
            print("No tickets found")
            return

        for ticket in self.tickets:

            print("\n-------------------")
            print(f"Ticket ID   : {ticket.ticket_id}")
            print(f"Machine ID  : {ticket.machine_id}")
            print(f"Status      : {ticket.status}")
            print(f"Reported By : {ticket.reported_by}")

    def get_ticket(self, ticket_id):

        for ticket in self.tickets:

            if ticket.ticket_id == ticket_id:
                return ticket

        return None

    def validate_role(self, role, action):

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
                "CLOSE"
            ]
        }

        allowed_actions = permissions.get(role, [])

        return action in allowed_actions


if __name__ == "__main__":

    tm = TicketManager()

    tm.create_ticket(
        "TKT001",
        "MC001",
        "Motor Failure",
        "Shubham"
    )

    tm.assign_ticket(
        "TKT001",
        "Technician A"
    )

    tm.close_ticket(
        "TKT001",
        "Technician A",
        "Bearing Failure",
        "Bearing replaced"
    )

    tm.list_tickets()