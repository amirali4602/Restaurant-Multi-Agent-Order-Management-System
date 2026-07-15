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
    def set_status(self, text):
        self.status.setText(text)


    def set_driver(self, text):
        self.driver.setText(text)


    def set_cooking_time(self, text):
        self.cooking.setText(text)


    def set_delivery_eta(self, text):
        self.delivery.setText(text)


    def reset(self):

        self.set_status("Waiting")
        self.set_driver("-")
        self.set_cooking_time("-")
        self.set_delivery_eta("-")