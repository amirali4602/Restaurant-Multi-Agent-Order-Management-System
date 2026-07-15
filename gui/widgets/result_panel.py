from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QFormLayout

from services.event_bus import event_bus


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

        event_bus.result.connect(
            self.update_result
        )

    def update_result(self, data):

        self.status.setText(
            data.get("status", "Waiting")
        )

        self.driver.setText(
            data.get("driver", "-")
        )

        self.cooking.setText(
            data.get("cooking", "-")
        )

        self.delivery.setText(
            data.get("eta", "-")
        )

    def reset(self):

        self.update_result(
            {
                "status": "Waiting",
                "driver": "-",
                "cooking": "-",
                "eta": "-",
            }
        )