from agents.base_agent import BaseAgent


class InventoryAgent(BaseAgent):

    async def setup(self):
        await super().setup()

        print("InventoryAgent is ready.")