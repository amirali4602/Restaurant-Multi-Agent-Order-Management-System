from agents.order_agent import OrderAgent


class ApplicationController:

    def __init__(self, order_agent: OrderAgent):

        self.order_agent = order_agent

    def submit_order(self, order):

        self.order_agent.submit_order(order)