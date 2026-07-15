from spade.behaviour import CyclicBehaviour

from services.logger import AppLogger


class OrderListener(CyclicBehaviour):

    async def run(self):

        message = await self.receive(timeout=1)

        if message:

            AppLogger.info(
                f"OrderAgent received: {message.body}"
            )