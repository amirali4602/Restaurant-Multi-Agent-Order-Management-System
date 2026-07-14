from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from gui.widgets.menu_panel import MenuPanel
from gui.widgets.activity_panel import ActivityPanel
from gui.widgets.result_panel import ResultPanel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restaurant Multi-Agent System")
        self.resize(1200, 700)

        central = QWidget()

        self.setCentralWidget(central)

        root = QVBoxLayout(central)

        top = QHBoxLayout()

        self.menu_panel = MenuPanel()

        self.activity_panel = ActivityPanel()

        top.addWidget(self.menu_panel, 1)

        top.addWidget(self.activity_panel, 2)

        root.addLayout(top)

        self.result_panel = ResultPanel()

        root.addWidget(self.result_panel)