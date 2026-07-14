from spade.agent import Agent


class BaseAgent(Agent):

    async def setup(self):
        print("=" * 50)
        print(f"{self.__class__.__name__} connected")
        print(f"JID: {self.jid}")
        print("=" * 50)