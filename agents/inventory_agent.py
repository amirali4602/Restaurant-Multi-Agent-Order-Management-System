from agents.base_agent import BaseAgent

from agents.behaviours.inventory.inventory_listener import InventoryListener


class InventoryAgent(BaseAgent):

    async def setup(self):
        await super().setup()

        self.add_behaviour(
            InventoryListener()
        )