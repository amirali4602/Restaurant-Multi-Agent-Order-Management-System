from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QVBoxLayout


class AgentMonitor(QGroupBox):

    def __init__(self):
        super().__init__("Agent Monitor")

        layout = QVBoxLayout(self)

        self.order = QLabel("🤖 Order Agent\nStatus : Idle")
        self.inventory = QLabel("⚪ Inventory Agent WAITING")
        self.chef = QLabel("⚪ Chef Agent      WAITING")
        self.delivery = QLabel("⚪ Delivery Agent WAITING")

        layout.addWidget(self.order)
        layout.addWidget(self.inventory)
        layout.addWidget(self.chef)
        layout.addWidget(self.delivery)

        layout.addStretch()