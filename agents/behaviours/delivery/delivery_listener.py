import asyncio
import random
from datetime import datetime

from spade.behaviour import CyclicBehaviour
from spade.message import Message

from database.repository import OrderRepository

from messaging.performatives import Performative

from models.order import Order
from models.order_status import OrderStatus

from services.logger import AppLogger
from services.notification_service import NotificationService


class DeliveryListener(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=5)

        if msg is None:
            return

        performative = msg.get_metadata("performative")

        if performative != Performative.REQUEST_DELIVERY.value:
            return

        order = Order.from_json(msg.body)

        AppLogger.info(
            "DeliveryAgent <- OrderAgent | REQUEST_DELIVERY"
        )

        AppLogger.info(
            f"[{order.order_id}] Assigning delivery driver..."
        )

        drivers = [
            "Mike",
            "Emma",
            "Alex",
            "Sophia",
            "James",
        ]

        order.driver = random.choice(drivers)
        order.status = OrderStatus.OUT_FOR_DELIVERY.value

        NotificationService.delivery_started()
        NotificationService.delivery_started_result(order)

        AppLogger.info(
            f"[{order.order_id}] Driver assigned: {order.driver}"
        )

        order.delivery_time = random.randint(4, 8)

        await asyncio.sleep(order.delivery_time)

        order.status = OrderStatus.DELIVERED.value
        order.completed_at = datetime.now().isoformat(timespec="seconds")

        OrderRepository.save(order)

        NotificationService.delivery_done()
        NotificationService.order_completed()
        NotificationService.delivery_completed_result(order)

        AppLogger.info(
            f"[{order.order_id}] Order delivered."
        )

        reply = Message(
            to=str(msg.sender)
        )

        reply.set_metadata(
            "performative",
            Performative.DELIVERED.value
        )

        reply.body = order.to_json()

        await self.send(reply)

        AppLogger.info(
            "DeliveryAgent -> OrderAgent | DELIVERED"
        )