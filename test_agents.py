import asyncio

from agents.order_agent import OrderAgent
from agents.inventory_agent import InventoryAgent
from agents.chef_agent import ChefAgent
from agents.delivery_agent import DeliveryAgent

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

    delivery = DeliveryAgent(
        DELIVERY_AGENT_JID,
        DELIVERY_AGENT_PASSWORD,
        verify_security=False,
    )

    # Start agents
    await order.start(auto_register=False)
    await inventory.start(auto_register=False)
    await chef.start(auto_register=False)
    await delivery.start(auto_register=False)

    print("Agents started.")

    # Wait until all agents are ready
    await asyncio.sleep(2)

    # Trigger workflow
    order.add_behaviour(
        SendInventoryRequest()
    )

    try:
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:

        print("\nStopping agents...")

        await order.stop()
        await inventory.stop()
        await chef.stop()
        await delivery.stop()

        print("Agents stopped.")


if __name__ == "__main__":
    asyncio.run(main())