from dataclasses import dataclass
from datetime import datetime
from typing import Optional
#my code 

ROLES = [
    "ADMIN",
    "MAINTENANCE",
    "OPERATOR"
]

TICKET_STATUS = [
    "OPEN",
    "IN_PROGRESS",
    "CLOSED"
]

@dataclass
class User:
    user_id: str
    username: str
    password: str
    role: str


@dataclass
class Machine:
    machine_id: str
    machine_name: str
    location: str


@dataclass
class Ticket:
    ticket_id: str
    machine_id: str
    description: str
    status: str
    reported_by: str
    reported_at: datetime

    assigned_to: Optional[str] = None
    assigned_at: Optional[datetime] = None

    closed_by: Optional[str] = None
    closed_at: Optional[datetime] = None

    root_cause: Optional[str] = None
    resolution_notes: Optional[str] = None


@dataclass
class BreakdownAnalytics:
    machine_id: str
    mttr_hours: float
    mtbf_hours: float


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
