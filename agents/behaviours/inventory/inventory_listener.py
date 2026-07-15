import json

from spade.behaviour import CyclicBehaviour
from spade.message import Message

from messaging.performatives import Performative
from services.logger import AppLogger


class InventoryListener(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=5)

        if msg is None:
            return

        performative = msg.get_metadata("performative")

        if performative != Performative.CHECK_INVENTORY.value:
            return

        order = json.loads(msg.body)

        AppLogger.info(
            "InventoryAgent <- OrderAgent | CHECK_INVENTORY"
        )

        AppLogger.info(
            f"Checking inventory for {order['customer']}"
        )

        AppLogger.info(
            f"Items: {order['items']}"
        )

        response = {
            "status": "available",
            "message": "Inventory verified"
        }

        reply = Message(
            to=str(msg.sender)
        )

        reply.set_metadata(
            "performative",
            Performative.INVENTORY_OK.value
        )

        reply.body = json.dumps(response)

        await self.send(reply)

        AppLogger.info(
            "InventoryAgent -> OrderAgent | INVENTORY_OK"
        )