from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restaurant Multi-Agent System")
        self.resize(1000, 700)

        container = QWidget()

        layout = QVBoxLayout(container)

        title = QLabel("Restaurant Multi-Agent System")

        layout.addWidget(title)

        self.setCentralWidget(container)