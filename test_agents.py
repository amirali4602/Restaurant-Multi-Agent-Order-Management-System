import asyncio

from agents.chef_agent import ChefAgent
from agents.order_agent import OrderAgent
from agents.inventory_agent import InventoryAgent

from agents.behaviours.order.send_inventory_request import (
    SendInventoryRequest,
)

from config.settings import *


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
    chef = ChefAgent(
        CHEF_AGENT_JID,
        CHEF_AGENT_PASSWORD,
        verify_security=False,
    )

    # Start agents first
    await order.start(auto_register=False)
    await inventory.start(auto_register=False)
    await chef.start(auto_register=False)

    print("Agents started.")

    # Give them a moment to finish setup()
    await asyncio.sleep(2)

    # Now trigger the OneShotBehaviour
    order.add_behaviour(
        SendInventoryRequest()
    )

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Stopping agents...")

        await order.stop()
        await inventory.stop()

        print("Agents stopped.")


if __name__ == "__main__":
    asyncio.run(main())