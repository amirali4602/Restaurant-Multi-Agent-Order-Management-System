from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout


class QuantitySelector(QWidget):
    def __init__(self):
        super().__init__()

        self.value = 0

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        self.minus_btn = QPushButton("−")
        self.plus_btn = QPushButton("+")

        self.minus_btn.setFixedSize(34, 34)
        self.plus_btn.setFixedSize(34, 34)

        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFixedWidth(35)

        layout.addWidget(self.minus_btn)
        layout.addWidget(self.label)
        layout.addWidget(self.plus_btn)

        self.minus_btn.clicked.connect(self.decrease)
        self.plus_btn.clicked.connect(self.increase)
        self.minus_btn.setObjectName("quantityButton")
        self.plus_btn.setObjectName("quantityButton")

        self.label.setObjectName("quantityLabel")
    def increase(self):
        if self.value < 20:
            self.value += 1
            self.label.setText(str(self.value))

    def decrease(self):
        if self.value > 0:
            self.value -= 1
            self.label.setText(str(self.value))

    def get_value(self):
        return self.value

    def reset(self):
        self.value = 0
        self.label.setText("0")