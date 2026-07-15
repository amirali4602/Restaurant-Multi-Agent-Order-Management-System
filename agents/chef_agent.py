from agents.base_agent import BaseAgent

from agents.behaviours.chef.chef_listener import ChefListener


class ChefAgent(BaseAgent):

    async def setup(self):
        await super().setup()

        self.add_behaviour(
            ChefListener()
        )