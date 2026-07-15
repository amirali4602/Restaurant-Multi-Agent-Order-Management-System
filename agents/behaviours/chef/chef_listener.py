import asyncio

from spade.behaviour import CyclicBehaviour
from spade.message import Message

from messaging.performatives import Performative

from models.order import Order
from models.order_status import OrderStatus

from services.logger import AppLogger


class ChefListener(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=5)

        if msg is None:
            return

        performative = msg.get_metadata("performative")

        if performative != Performative.PREPARE_ORDER.value:
            return

        order = Order.from_json(msg.body)

        AppLogger.info(
            "ChefAgent <- OrderAgent | PREPARE_ORDER"
        )

        AppLogger.info(
            f"[{order.order_id}] Preparing order for {order.customer}"
        )

        order.status = OrderStatus.COOKING.value

        await asyncio.sleep(3)

        order.status = OrderStatus.READY.value

        AppLogger.info(
            "Cooking finished."
        )

        reply = Message(
            to=str(msg.sender)
        )

        reply.set_metadata(
            "performative",
            Performative.ORDER_READY.value
        )

        reply.body = order.to_json()

        await self.send(reply)

        AppLogger.info(
            "ChefAgent -> OrderAgent | ORDER_READY"
        )