#from storage_stub import StorageStub
class TicketManager:
    #########testing
    def create_ticket(self):
        print("Ticket Created")
    #########testing

    #def __init__(self):
        self.storage = StorageStub()
        
    def create_ticket(self):
        print("ticket created ")

    def assign_ticket(self):
        pass
    
    def close_ticket(self):
        pass

    def list_tickets(self):
        pass

    def get_ticket(self, ticket_id):
        pass

    def validate_role(self):
        pass
    
#main 
if __name__ == "__main__":
    tm = TicketManager()
    tm.create_ticket()