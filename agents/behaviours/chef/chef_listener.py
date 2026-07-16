import asyncio
import random
from datetime import datetime

from config.settings import CHEF_FAILURE_RATE
from database.repository import OrderRepository
from spade.behaviour import CyclicBehaviour
from spade.message import Message

from messaging.performatives import Performative

from models.order import Order
from models.order_status import OrderStatus

from services.logger import AppLogger
from services.notification_service import NotificationService

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
        NotificationService.chef_cooking()
        NotificationService.cooking_started(order)
        if random.random() < CHEF_FAILURE_RATE:
            order.status = OrderStatus.CANCELLED.value
            order.failure_stage = "Chef"
            order.failure_reason = random.choice(
                [
                    "Oven malfunction",
                    "Chef unavailable",
                    "Kitchen equipment failure",
                    "Power outage in kitchen",
                ]
            )

            order.completed_at = datetime.now().isoformat(
                timespec="seconds"
            )

            OrderRepository.save(order)

            AppLogger.warning(
                f"[{order.order_id}] {order.failure_reason}"
            )

            reply = Message(
                to=str(msg.sender)
            )

            reply.set_metadata(
                "performative",
                Performative.CHEF_FAILED.value
            )

            reply.body = order.to_json()

            await self.send(reply)

            return
        order.cooking_time = random.randint(2, 5)

        await asyncio.sleep(order.cooking_time)

        order.status = OrderStatus.READY.value
        NotificationService.chef_ready()
        NotificationService.cooking_finished(order)
        NotificationService.delivery_started()
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