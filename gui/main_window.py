from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtGui import QShortcut, QKeySequence
from gui.history_window import HistoryWindow
from gui.widgets.activity_panel import ActivityPanel
from gui.widgets.agent_monitor import AgentMonitor
from gui.widgets.menu_panel import MenuPanel
from gui.widgets.result_panel import ResultPanel


class MainWindow(QMainWindow):

    def __init__(self, agent_manager):
        super().__init__()

        self.agent_manager = agent_manager

        self.setWindowTitle("Restaurant Multi-Agent System")
        self.setWindowIcon(QIcon("assets/restaurant.jpg"))
        self.setMinimumSize(1200, 700)
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        root = QVBoxLayout(central)

        top = QHBoxLayout()
        left = QVBoxLayout()
        right = QVBoxLayout()

        self.menu = MenuPanel()
        self.monitor = AgentMonitor()
        self.activity = ActivityPanel()
        self.activity.setMinimumHeight(180)
        self.activity.setMaximumHeight(250)
        self.result = ResultPanel()

        left.addWidget(self.menu)

        right.addWidget(self.monitor)
        right.addWidget(self.activity)

        top.addLayout(left, 1)
        top.addLayout(right, 2)

        title = QLabel(
            "🍽 Restaurant Multi-Agent Order Management System"
        )
        title.setObjectName("appTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        root.addWidget(title)
        root.addLayout(top)
        root.addWidget(self.result)

        self.statusBar().showMessage("🟢 System Ready")

        self.menu.submit_button.clicked.connect(
            self.submit_order
        )

        self.menu.history_button.clicked.connect(
            self.show_history
        )
        self.fullscreen_shortcut = QShortcut(
            QKeySequence("F11"),
            self,
        )

        self.fullscreen_shortcut.activated.connect(
            self.toggle_fullscreen
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

    def show_history(self):

        dialog = HistoryWindow()

        dialog.exec()
    def toggle_fullscreen(self):

        if self.isFullScreen():
            self.showNormal()
            self.showMaximized()
        else:
            self.showFullScreen()