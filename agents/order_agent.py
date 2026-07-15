from agents.base_agent import BaseAgent

from agents.behaviours.order.order_listener import OrderListener


class OrderAgent(BaseAgent):

    async def setup(self):
        await super().setup()

        self.add_behaviour(
            OrderListener()
        )