from dataclasses import dataclass
from datetime import datetime
from typing import Optional


# User Model
@dataclass
class User:
    user_id: int
    name: str
    role: str
    email: str


# Machine Model
@dataclass
class Machine:
    machine_id: int
    machine_name: str
    location: str
    status: str


# Ticket Model
@dataclass
class Ticket:
    ticket_id: int
    machine_id: int
    created_by: int
    issue: str
    status: str
    opened_at: datetime
    closed_at: Optional[datetime] = None
    root_cause: Optional[str] = None


# Analytics Summary Model
@dataclass
class AnalyticsSummary:
    total_breakdowns: int
    mttr: float
    mtbf: float