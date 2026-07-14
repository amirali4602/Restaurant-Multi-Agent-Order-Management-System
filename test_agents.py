import asyncio

from agents.order_agent import OrderAgent
from agents.inventory_agent import InventoryAgent

from config.settings import *
import logging

# logging.basicConfig(level=logging.DEBUG)

async def main():

    order = OrderAgent(
        ORDER_AGENT_JID,
        ORDER_AGENT_PASSWORD,
        verify_security=False,
    )

    inventory = InventoryAgent(
        INVENTORY_AGENT_JID,
        INVENTORY_AGENT_PASSWORD,
        verify_security=False,
    )
    await order.start(auto_register=False)
    await inventory.start(auto_register=False)

    print("Agents started.")

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())