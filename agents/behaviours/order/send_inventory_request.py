from spade.behaviour import OneShotBehaviour
from spade.message import Message

from config.settings import INVENTORY_AGENT_JID
from messaging.performatives import Performative

from services.logger import AppLogger
import json

class SendInventoryRequest(OneShotBehaviour):

    async def run(self):

        msg = Message(
            to=INVENTORY_AGENT_JID
        )

        msg.set_metadata(
            "performative",
            Performative.CHECK_INVENTORY.value
        )
        order = {
            "customer": "John",
            "items": {
                "Pizza": 2,
                "Drink": 1
            }
        }
        msg.body = json.dumps(order)

        await self.send(msg)

        AppLogger.info(
            "Inventory request sent."
        )