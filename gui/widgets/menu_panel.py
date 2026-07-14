from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QGroupBox,
)

from gui.widgets.quantity_selector import QuantitySelector


class MenuPanel(QGroupBox):
    def __init__(self):
        super().__init__("Place Order")

        layout = QVBoxLayout(self)

        # Customer Name
        layout.addWidget(QLabel("Customer Name"))

        self.customer_name = QLineEdit()
        self.customer_name.setPlaceholderText("Enter customer name")
        layout.addWidget(self.customer_name)

        layout.addSpacing(10)

        layout.addWidget(QLabel("Menu"))

        self.items = {}

        foods = [
            "Pizza",
            "Burger",
            "Pasta",
            "Drink",
            "Fries",
        ]

        for food in foods:

            row = QHBoxLayout()

            label = QLabel(food)
            selector = QuantitySelector()

            row.addWidget(label)
            row.addStretch()
            row.addWidget(selector)   # <-- This was missing

            layout.addLayout(row)

            self.items[food] = selector

        layout.addStretch()

        self.submit_button = QPushButton("Submit Order")
        layout.addWidget(self.submit_button)