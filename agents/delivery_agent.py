from agents.base_agent import BaseAgent

from agents.behaviours.delivery.delivery_listener import DeliveryListener


class DeliveryAgent(BaseAgent):

    async def setup(self):

        await super().setup()

        self.add_behaviour(
            DeliveryListener()
        )