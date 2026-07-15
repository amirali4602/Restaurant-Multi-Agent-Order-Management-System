from dataclasses import dataclass
from datetime import datetime


@dataclass
class AgentMessage:

    performative: str

    sender: str

    receiver: str

    order_id: str

    body: dict

    timestamp: datetime