import asyncio
import threading

from agents.order_agent import OrderAgent
from agents.inventory_agent import InventoryAgent
from agents.chef_agent import ChefAgent
from agents.delivery_agent import DeliveryAgent

from config.settings import *


class AgentManager:

    def __init__(self):

        self.loop = None
        self.thread = None

        self.order_agent = None
        self.inventory_agent = None
        self.chef_agent = None
        self.delivery_agent = None
    def _create_agents(self):

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
    async def _start_agents(self):

        self._create_agents()

        await self.order_agent.start(auto_register=False)
        await self.inventory_agent.start(auto_register=False)
        await self.chef_agent.start(auto_register=False)
        await self.delivery_agent.start(auto_register=False)
    def _run_loop(self):

        self.loop = asyncio.new_event_loop()

        asyncio.set_event_loop(self.loop)

        self.loop.run_until_complete(
            self._start_agents()
        )

        self.loop.run_forever()
    def start(self):

        self.thread = threading.Thread(
            target=self._run_loop,
            daemon=True,
        )

        self.thread.start()
    def submit_order(self, order):

        if self.loop is None:
            return

        self.loop.call_soon_threadsafe(
            self.order_agent.submit_order,
            order,
        )