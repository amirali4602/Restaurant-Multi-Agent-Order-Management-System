import asyncio

from spade.behaviour import CyclicBehaviour
from spade.message import Message

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

        await asyncio.sleep(2)

        order.status = OrderStatus.OUT_FOR_DELIVERY.value
        NotificationService.delivery_started()
        NotificationService.delivery_completed_result()
        AppLogger.info(
            f"[{order.order_id}] Driver assigned."
        )

        await asyncio.sleep(3)

        order.status = OrderStatus.DELIVERED.value
        NotificationService.delivery_done()
        NotificationService.order_completed()
        NotificationService.delivery_completed_result()
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