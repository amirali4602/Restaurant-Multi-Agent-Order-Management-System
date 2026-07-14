from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QFormLayout


class ResultPanel(QGroupBox):

    def __init__(self):
        super().__init__("Final Result")

        layout = QFormLayout(self)

        self.status = QLabel("Waiting")

        self.driver = QLabel("-")

        self.cooking = QLabel("-")

        self.delivery = QLabel("-")

        layout.addRow("Order Status :", self.status)
        layout.addRow("Assigned Driver :", self.driver)
        layout.addRow("Cooking Time :", self.cooking)
        layout.addRow("Delivery ETA :", self.delivery)