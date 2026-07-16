import random
from datetime import datetime

from spade.behaviour import CyclicBehaviour
from spade.message import Message

from config.settings import INVENTORY_FAILURE_RATE
from database.repository import OrderRepository
from messaging.performatives import Performative

from models.order import Order
from models.order_status import OrderStatus

from services.logger import AppLogger
from services.notification_service import NotificationService


class InventoryListener(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=5)

        if msg is None:
            return

        performative = msg.get_metadata("performative")

        if performative != Performative.CHECK_INVENTORY.value:
            return

        order = Order.from_json(msg.body)

        AppLogger.info(
            "InventoryAgent <- OrderAgent | CHECK_INVENTORY"
        )

        AppLogger.info(
            f"[{order.order_id}] Checking inventory for {order.customer}"
        )

        AppLogger.info(
            f"Items: {order.items}"
        )

        NotificationService.inventory_checking()

        # -----------------------------
        # Inventory Failure Simulation
        # -----------------------------

        if random.random() < INVENTORY_FAILURE_RATE:

            unavailable_item = random.choice(
                list(order.items.keys())
            )

            order.status = OrderStatus.CANCELLED.value
            order.failure_stage = "Inventory"
            order.failure_reason = (
                f"{unavailable_item} is out of stock"
            )
            order.completed_at = datetime.now().isoformat(
                timespec="seconds"
            )

            OrderRepository.save(order)

            NotificationService.inventory_done()

            AppLogger.warning(
                f"[{order.order_id}] {order.failure_reason}"
            )

            reply = Message(
                to=str(msg.sender)
            )

            reply.set_metadata(
                "performative",
                Performative.INVENTORY_FAILED.value
            )

            reply.body = order.to_json()

            await self.send(reply)

            AppLogger.info(
                "InventoryAgent -> OrderAgent | INVENTORY_FAILED"
            )

            return

        # -----------------------------
        # Success
        # -----------------------------

        order.status = OrderStatus.INVENTORY_CONFIRMED.value

        NotificationService.inventory_done()
        NotificationService.inventory_result(order)

        reply = Message(
            to=str(msg.sender)
        )

        reply.set_metadata(
            "performative",
            Performative.INVENTORY_OK.value
        )

        reply.body = order.to_json()

        await self.send(reply)

        AppLogger.info(
            "InventoryAgent -> OrderAgent | INVENTORY_OK"
        )