from spade.behaviour import OneShotBehaviour
from spade.message import Message

from config.settings import INVENTORY_AGENT_JID
from messaging.performatives import Performative

from services.logger import AppLogger
from services.notification_service import NotificationService

class SendInventoryRequest(OneShotBehaviour):

    def __init__(self, order):

        super().__init__()

        self.order = order

    async def run(self):

        NotificationService.order_running()
        NotificationService.inventory_checking()
        msg = Message(
            to=INVENTORY_AGENT_JID
        )

        msg.set_metadata(
            "performative",
            Performative.CHECK_INVENTORY.value
        )

        msg.body = self.order.to_json()

        await self.send(msg)

        AppLogger.info(
            f"[{self.order.order_id}] Inventory request sent."
        )