from agents.base_agent import BaseAgent


class OrderAgent(BaseAgent):

    async def setup(self):
        await super().setup()

        print("OrderAgent is ready.")