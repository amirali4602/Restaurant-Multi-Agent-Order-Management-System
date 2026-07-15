from spade.behaviour import OneShotBehaviour
from spade.message import Message

from config.settings import INVENTORY_AGENT_JID
from messaging.performatives import Performative

from models.order import Order
from services.logger import AppLogger

class SendInventoryRequest(OneShotBehaviour):

    async def run(self):

        msg = Message(
            to=INVENTORY_AGENT_JID
        )

        msg.set_metadata(
            "performative",
            Performative.CHECK_INVENTORY.value
        )
        order = Order.create(
            customer="John",
            items={
                "Pizza": 2,
                "Drink": 1
            }
        )
        msg.body = order.to_json()

        await self.send(msg)

        AppLogger.info(
            f"[{order.order_id}] Inventory request sent."
        )