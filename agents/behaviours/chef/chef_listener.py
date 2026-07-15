import asyncio
import json

from spade.behaviour import CyclicBehaviour
from spade.message import Message

from messaging.performatives import Performative
from services.logger import AppLogger


class ChefListener(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=5)

        if msg is None:
            return

        performative = msg.get_metadata("performative")

        if performative != Performative.PREPARE_ORDER.value:
            return

        order = json.loads(msg.body)

        AppLogger.info(
            "ChefAgent <- OrderAgent | PREPARE_ORDER"
        )

        AppLogger.info(
            f"Preparing order for {order['customer']}"
        )

        await asyncio.sleep(3)

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

        reply.body = json.dumps({
            "status": "ready"
        })

        await self.send(reply)

        AppLogger.info(
            "ChefAgent -> OrderAgent | ORDER_READY"
        )