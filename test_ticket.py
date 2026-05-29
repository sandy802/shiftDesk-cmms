from managers.ticket_manager import TicketManager

ticket_manager = TicketManager()

ticket = {
    "ticket_id": 1001,
    "machine_id": 101,
    "issue": "Motor overheating",
    "priority": "High",
    "status": "Open"
}

ticket_manager.create_ticket(ticket)