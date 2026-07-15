from PySide6.QtWidgets import QLabel, QGroupBox, QVBoxLayout

from services.event_bus import event_bus


class AgentMonitor(QGroupBox):

    def __init__(self):
        super().__init__("Agent Monitor")

        layout = QVBoxLayout(self)

        self.order = QLabel("⚪ Order Agent      WAITING")
        self.inventory = QLabel("⚪ Inventory Agent  WAITING")
        self.chef = QLabel("⚪ Chef Agent       WAITING")
        self.delivery = QLabel("⚪ Delivery Agent   WAITING")

        layout.addWidget(self.order)
        layout.addWidget(self.inventory)
        layout.addWidget(self.chef)
        layout.addWidget(self.delivery)

        layout.addStretch()

        event_bus.order_status.connect(
            self.set_order_status
        )

        event_bus.inventory_status.connect(
            self.set_inventory_status
        )

        event_bus.chef_status.connect(
            self.set_chef_status
        )

        event_bus.delivery_status.connect(
            self.set_delivery_status
        )
        self.set_order_status("IDLE")
        self.set_inventory_status("IDLE")
        self.set_chef_status("IDLE")
        self.set_delivery_status("IDLE")
    def set_order_status(self, status):
        self.order.setText(f"🤖 Order Agent      {status}")

    def set_inventory_status(self, status):
        self.inventory.setText(f"📦 Inventory Agent  {status}")

    def set_chef_status(self, status):
        self.chef.setText(f"👨‍🍳 Chef Agent       {status}")

    def set_delivery_status(self, status):
        self.delivery.setText(f"🚚 Delivery Agent   {status}")