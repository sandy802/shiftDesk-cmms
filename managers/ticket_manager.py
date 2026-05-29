from Storage.engine import StorageEngine


class TicketManager:

    def __init__(self):

        self.storage = StorageEngine()

    def create_ticket(self, ticket_data):

        tickets = self.storage.load_data("tickets.json")

        tickets.append(ticket_data)

        self.storage.save_data("tickets.json", tickets)

        print("Ticket created successfully!")

    def view_tickets(self):

        tickets = self.storage.load_data("tickets.json")

        return tickets

    def update_ticket_status(self, ticket_id, new_status):

        tickets = self.storage.load_data("tickets.json")

        for ticket in tickets:

            if ticket["ticket_id"] == ticket_id:

                ticket["status"] = new_status

                self.storage.save_data("tickets.json", tickets)

                print("Ticket status updated!")

                return

        print("Ticket not found!")