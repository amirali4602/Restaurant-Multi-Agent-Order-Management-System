from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class ResultPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Final Result"))

        self.status = QLabel("Order Status : Waiting")
        self.driver = QLabel("Driver : -")
        self.cooking = QLabel("Cooking Time : -")
        self.delivery = QLabel("Delivery ETA : -")

        layout.addWidget(self.status)
        layout.addWidget(self.driver)
        layout.addWidget(self.cooking)
        layout.addWidget(self.delivery)