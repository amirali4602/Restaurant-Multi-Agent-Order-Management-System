from agents.base_agent import BaseAgent

from agents.behaviours.order.order_listener import OrderListener
from agents.behaviours.order.send_inventory_request import (
    SendInventoryRequest,
)


class OrderAgent(BaseAgent):

    async def setup(self):

        await super().setup()

        self.add_behaviour(
            OrderListener()
        )

    def submit_order(self, order):

        self.add_behaviour(
            SendInventoryRequest(order)
        )

