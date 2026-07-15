from spade.behaviour import CyclicBehaviour
from spade.message import Message

from config.settings import (
    CHEF_AGENT_JID,
    DELIVERY_AGENT_JID,
)

from messaging.performatives import Performative

from models.order import Order
from models.order_status import OrderStatus

from services.logger import AppLogger


class OrderListener(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=5)

        if msg is None:
            return

        performative = msg.get_metadata("performative")

        # -------------------------
        # Inventory Response
        # -------------------------

        if performative == Performative.INVENTORY_OK.value:

            AppLogger.info(
                "OrderAgent <- InventoryAgent | INVENTORY_OK"
            )

            order = Order.from_json(msg.body)

            AppLogger.info(
                f"[{order.order_id}] Inventory Status: {order.status}"
            )

            if order.status != OrderStatus.INVENTORY_CONFIRMED.value:

                AppLogger.warning(
                    "Inventory unavailable."
                )

                return

            chef_message = Message(
                to=CHEF_AGENT_JID
            )

            chef_message.set_metadata(
                "performative",
                Performative.PREPARE_ORDER.value
            )

            chef_message.body = order.to_json()

            await self.send(chef_message)

            AppLogger.info(
                "OrderAgent -> ChefAgent | PREPARE_ORDER"
            )

        # -------------------------
        # Chef Response
        # -------------------------

        elif performative == Performative.ORDER_READY.value:

            AppLogger.info(
                "OrderAgent <- ChefAgent | ORDER_READY"
            )

            order = Order.from_json(msg.body)

            delivery_message = Message(
                to=DELIVERY_AGENT_JID
            )

            delivery_message.set_metadata(
                "performative",
                Performative.REQUEST_DELIVERY.value
            )

            delivery_message.body = order.to_json()

            await self.send(delivery_message)

            AppLogger.info(
                "OrderAgent -> DeliveryAgent | REQUEST_DELIVERY"
            )

        # -------------------------
        # Delivery Response
        # -------------------------

        elif performative == Performative.DELIVERED.value:

            AppLogger.info(
                "OrderAgent <- DeliveryAgent | DELIVERED"
            )

            order = Order.from_json(msg.body)

            AppLogger.info(
                f"[{order.order_id}] Order delivered successfully!"
            )