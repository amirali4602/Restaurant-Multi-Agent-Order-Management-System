from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QFrame


class StatCard(QFrame):

    def __init__(self, title: str):
        super().__init__()

        self.setObjectName("statCard")

        layout = QVBoxLayout(self)

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("statTitle")

        self.value = QLabel("-")
        self.value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value.setObjectName("statValue")

        layout.addWidget(self.title)
        layout.addWidget(self.value)
        self.setMinimumHeight(75)
    def set_value(self, value):
        self.value.setText(str(value))