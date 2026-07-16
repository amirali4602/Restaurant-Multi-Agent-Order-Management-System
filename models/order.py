import json
import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Dict

from models.order_status import OrderStatus


@dataclass
class Order:
    order_id: str
    customer: str
    items: Dict[str, int]
    status: str

    driver: str = ""
    cooking_time: int = 0
    delivery_time: int = 0

    created_at: str = ""
    completed_at: str = ""

    failure_stage: str = ""
    failure_reason: str = ""

    @classmethod
    def create(cls, customer, items):

        return cls(
            order_id=str(uuid.uuid4()),
            customer=customer,
            items=items,
            status=OrderStatus.RECEIVED.value,
            created_at=datetime.now().isoformat(timespec="seconds"),
        )

    def to_json(self):

        return json.dumps(
            {
                "order_id": self.order_id,
                "customer": self.customer,
                "items": self.items,
                "status": self.status,
                "driver": self.driver,
                "cooking_time": self.cooking_time,
                "delivery_time": self.delivery_time,
                "created_at": self.created_at,
                "completed_at": self.completed_at,
                "failure_stage": self.failure_stage,
                "failure_reason": self.failure_reason,
            }
        )

    @classmethod
    def from_json(cls, data):

        data = json.loads(data)

        return cls(
            order_id=data["order_id"],
            customer=data["customer"],
            items=data["items"],
            status=data["status"],
            driver=data.get("driver", ""),
            cooking_time=data.get("cooking_time", 0),
            delivery_time=data.get("delivery_time", 0),
            created_at=data.get("created_at", ""),
            completed_at=data.get("completed_at", ""),
            failure_stage=data.get("failure_stage", ""),
            failure_reason=data.get("failure_reason", ""),
        )

    def __str__(self):

        return (
            f"Order("
            f"id={self.order_id}, "
            f"customer='{self.customer}', "
            f"items={self.items}, "
            f"status='{self.status}', "
            f"driver='{self.driver}', "
            f"cooking_time={self.cooking_time}, "
            f"delivery_time={self.delivery_time}, "
            f"failure_stage='{self.failure_stage}', "
            f"failure_reason='{self.failure_reason}'"
            f")"
        )