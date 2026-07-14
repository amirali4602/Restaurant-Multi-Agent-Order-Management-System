from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
)


class MenuPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Menu")
        layout.addWidget(title)

        self.customer_name = QLineEdit()
        self.customer_name.setPlaceholderText("Customer Name")

        layout.addWidget(self.customer_name)

        self.items = {}

        foods = [
            "Pizza",
            "Burger",
            "Pasta",
            "Drink",
            "Fries"
        ]

        for food in foods:

            row = QHBoxLayout()

            label = QLabel(food)

            spin = QSpinBox()
            spin.setRange(0, 20)

            row.addWidget(label)
            row.addStretch()
            row.addWidget(spin)

            layout.addLayout(row)

            self.items[food] = spin

        self.submit_button = QPushButton("Submit Order")

        layout.addStretch()

        layout.addWidget(self.submit_button)