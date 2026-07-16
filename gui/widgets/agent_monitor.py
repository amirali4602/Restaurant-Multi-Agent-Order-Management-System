from PySide6.QtWidgets import QGridLayout, QGroupBox

from gui.widgets.agent_card import AgentCard
from services.event_bus import event_bus


class AgentMonitor(QGroupBox):

    def __init__(self):
        super().__init__("Agent Monitor")

        layout = QGridLayout(self)

        self.order = AgentCard("🤖", "Order Agent")
        self.inventory = AgentCard("📦", "Inventory Agent")
        self.chef = AgentCard("👨‍🍳", "Chef Agent")
        self.delivery = AgentCard("🚚", "Delivery Agent")

        layout.addWidget(self.order, 0, 0)
        layout.addWidget(self.inventory, 0, 1)
        layout.addWidget(self.chef, 1, 0)
        layout.addWidget(self.delivery, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        event_bus.order_status.connect(
            self.order.set_status
        )

        event_bus.inventory_status.connect(
            self.inventory.set_status
        )

        event_bus.chef_status.connect(
            self.chef.set_status
        )

        event_bus.delivery_status.connect(
            self.delivery.set_status
        )