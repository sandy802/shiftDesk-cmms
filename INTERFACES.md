# Storage Engine Interface Contract

## Purpose

This document defines the public methods exposed by the Storage Engine.

All modules must interact with storage only through these methods.

---

# User Methods

### save_user(user)

Saves a new user to storage.

Arguments:
- user (User)

Returns:
- None

---

### get_user_by_id(user_id)

Fetch a user using user ID.

Arguments:
- user_id (int)

Returns:
- User | None

---

# Machine Methods

### save_machine(machine)

Stores a machine record.

Arguments:
- machine (Machine)

Returns:
- None

---

### get_machine_by_id(machine_id)

Fetch machine details.

Arguments:
- machine_id (int)

Returns:
- Machine | None

---

### get_all_machines()

Returns all machines.

Arguments:
- None

Returns:
- list[Machine]

---

# Ticket Methods

### save_ticket(ticket)

Stores a ticket.

Arguments:
- ticket (Ticket)

Returns:
- None

---

### update_ticket(ticket)

Updates existing ticket.

Arguments:
- ticket (Ticket)

Returns:
- None

---

### get_ticket_by_id(ticket_id)

Fetch ticket by ID.

Arguments:
- ticket_id (int)

Returns:
- Ticket | None

---

### get_all_tickets()

Returns all tickets.

Arguments:
- None

Returns:
- list[Ticket]

---

# Analytics Methods

### get_closed_tickets()

Returns only closed tickets.

Arguments:
- None

Returns:
- list[Ticket]