from spade.behaviour import CyclicBehaviour

from messaging.message_builder import MessageBuilder
from messaging.performatives import Performative

from services.logger import AppLogger


class InventoryListener(CyclicBehaviour):

    async def run(self):

        message = await self.receive(timeout=1)

        if message is None:
            return

        AppLogger.info(
            f"InventoryAgent received: {message.body}"
        )

        reply = MessageBuilder.create(
            to=str(message.sender),
            performative=Performative.INVENTORY_OK.value,
            body="Inventory available"
        )

        await self.send(reply)

        AppLogger.info(
            "InventoryAgent replied."
        )