from spade.agent import Agent

from services.logger import AppLogger


class BaseAgent(Agent):

    async def setup(self):
        AppLogger.info(
            f"{self.__class__.__name__} connected ({self.jid})"
        )