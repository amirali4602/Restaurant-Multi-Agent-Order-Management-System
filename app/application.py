from agents.order_agent import OrderAgent
from agents.inventory_agent import InventoryAgent
from agents.chef_agent import ChefAgent
from agents.delivery_agent import DeliveryAgent

from config.settings import *


class RestaurantApplication:

    def __init__(self):

        self.order_agent = OrderAgent(
            ORDER_AGENT_JID,
            ORDER_AGENT_PASSWORD,
            verify_security=False,
        )

        self.inventory_agent = InventoryAgent(
            INVENTORY_AGENT_JID,
            INVENTORY_AGENT_PASSWORD,
            verify_security=False,
        )

        self.chef_agent = ChefAgent(
            CHEF_AGENT_JID,
            CHEF_AGENT_PASSWORD,
            verify_security=False,
        )

        self.delivery_agent = DeliveryAgent(
            DELIVERY_AGENT_JID,
            DELIVERY_AGENT_PASSWORD,
            verify_security=False,
        )

    async def start(self):

        await self.order_agent.start(auto_register=False)
        await self.inventory_agent.start(auto_register=False)
        await self.chef_agent.start(auto_register=False)
        await self.delivery_agent.start(auto_register=False)

    async def stop(self):

        await self.order_agent.stop()
        await self.inventory_agent.stop()
        await self.chef_agent.stop()
        await self.delivery_agent.stop()