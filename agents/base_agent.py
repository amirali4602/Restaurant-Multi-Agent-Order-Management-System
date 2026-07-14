from spade.agent import Agent


class BaseAgent(Agent):

    async def setup(self):
        print(f"{self.name} started.")