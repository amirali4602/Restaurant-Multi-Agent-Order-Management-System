import json
import uuid
from dataclasses import dataclass
from typing import Dict

from models.order_status import OrderStatus


@dataclass
class Order:
    order_id: str
    customer: str
    items: Dict[str, int]
    status: str

    @classmethod
    def create(cls, customer, items):
        return cls(
            order_id=str(uuid.uuid4()),
            customer=customer,
            items=items,
            status=OrderStatus.RECEIVED.value,
        )

    def to_json(self):
        return json.dumps({
            "order_id": self.order_id,
            "customer": self.customer,
            "items": self.items,
            "status": self.status,
        })

    @classmethod
    def from_json(cls, data):
        data = json.loads(data)

        return cls(
            order_id=data["order_id"],
            customer=data["customer"],
            items=data["items"],
            status=data["status"],
        )
    def __str__(self):
        return (
            f"Order("
            f"id={self.order_id}, "
            f"customer={self.customer}, "
            f"status={self.status}, "
            f"items={self.items})"
        )