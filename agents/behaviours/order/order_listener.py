import json

from spade.behaviour import CyclicBehaviour
from spade.message import Message

from config.settings import CHEF_AGENT_JID
from messaging.performatives import Performative
from services.logger import AppLogger


class OrderListener(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=5)

        if msg is None:
            return

        performative = msg.get_metadata("performative")

        if performative == Performative.INVENTORY_OK.value:

            AppLogger.info(
                "OrderAgent <- InventoryAgent | INVENTORY_OK"
            )

            response = json.loads(msg.body)

            AppLogger.info(
                f"Inventory Status: {response['status']}"
            )

            if response["status"] != "available":
                AppLogger.warning(
                    "Inventory unavailable."
                )
                return

            order = {
                "customer": "John",
                "items": {
                    "Pizza": 2,
                    "Drink": 1
                }
            }

            chef_message = Message(
                to=CHEF_AGENT_JID
            )

            chef_message.set_metadata(
                "performative",
                Performative.PREPARE_ORDER.value
            )

            chef_message.body = json.dumps(order)

            await self.send(chef_message)

            AppLogger.info(
                "OrderAgent -> ChefAgent | PREPARE_ORDER"
            )

        elif performative == Performative.ORDER_READY.value:

            response = json.loads(msg.body)

            AppLogger.info(
                "OrderAgent <- ChefAgent | ORDER_READY"
            )

            AppLogger.info(
                "Order completed successfully!"
            )