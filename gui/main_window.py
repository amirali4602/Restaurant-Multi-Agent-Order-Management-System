from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from gui.widgets.menu_panel import MenuPanel
from gui.widgets.agent_monitor import AgentMonitor
from gui.widgets.activity_panel import ActivityPanel
from gui.widgets.result_panel import ResultPanel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self, agent_manager):
        super().__init__()

        self.agent_manager = agent_manager

        self.setWindowTitle("Restaurant Multi-Agent System")
        self.setWindowIcon(QIcon("assets/restaurant.png"))
        self.setMinimumSize(1200,700)
        self.resize(1200,700)

        central = QWidget()

        self.setCentralWidget(central)

        root = QVBoxLayout(central)

        top = QHBoxLayout()

        left = QVBoxLayout()

        right = QVBoxLayout()

        self.menu = MenuPanel()

        self.monitor = AgentMonitor()

        self.activity = ActivityPanel()

        self.result = ResultPanel()

        left.addWidget(self.menu)

        right.addWidget(self.monitor)

        right.addWidget(self.activity)

        top.addLayout(left, 1)

        top.addLayout(right, 2)
        title = QLabel("🍽 Restaurant Multi-Agent Order Management System")
        title.setObjectName("appTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        root.addWidget(title)

        root.addLayout(top)

        root.addWidget(self.result)
        self.statusBar().showMessage("🟢 System Ready")
        self.menu.submit_button.clicked.connect(
            self.submit_order
        )
    def submit_order(self):

        order = self.menu.create_order()

        if order is None:

            self.statusBar().showMessage(
                "❌ Enter customer name and select at least one item."
            )

            return

        self.agent_manager.submit_order(order)

        self.statusBar().showMessage(
            f"✅ Order created for {order.customer}"
        )

        self.menu.clear_form()