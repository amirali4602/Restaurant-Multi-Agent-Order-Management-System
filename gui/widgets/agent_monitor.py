from PySide6.QtWidgets import QLabel, QGroupBox, QVBoxLayout


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

    def set_order_status(self, status):
        self.order.setText(f"🤖 Order Agent      {status}")

    def set_inventory_status(self, status):
        self.inventory.setText(f"📦 Inventory Agent {status}")

    def set_chef_status(self, status):
        self.chef.setText(f"👨‍🍳 Chef Agent      {status}")

    def set_delivery_status(self, status):
        self.delivery.setText(f"🚚 Delivery Agent  {status}")