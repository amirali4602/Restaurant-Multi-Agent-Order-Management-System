from spade.behaviour import CyclicBehaviour

from services.logger import AppLogger


class OrderListener(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=1)

        if msg is None:
            return

        AppLogger.info(
            f"OrderAgent received: {msg.body}"
        )