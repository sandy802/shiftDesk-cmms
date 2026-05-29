from storage.engine import StorageEngine


class TicketManager:

    def __init__(self):
        self.storage = StorageEngine()

    def create_ticket(self, ticket_data):

        tickets = self.storage.load_data("tickets.json")

        tickets.append(ticket_data)

        self.storage.save_data("tickets.json", tickets)

        print("Ticket created successfully!")