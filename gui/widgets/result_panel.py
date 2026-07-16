from PySide6.QtWidgets import (
    QGridLayout,
    QGroupBox,
)

from gui.widgets.stat_card import StatCard
from services.event_bus import event_bus


class ResultPanel(QGroupBox):

    def __init__(self):
        super().__init__("Current Order")

        layout = QGridLayout(self)

        self.status_card = StatCard(
            "Status",
            "Waiting",
        )

        self.driver_card = StatCard(
            "Driver",
            "-",
        )

        self.cooking_card = StatCard(
            "Cooking",
            "-",
        )

        self.delivery_card = StatCard(
            "ETA",
            "-",
        )

        layout.addWidget(self.status_card, 0, 0)
        layout.addWidget(self.driver_card, 0, 1)
        layout.addWidget(self.cooking_card, 0, 2)
        layout.addWidget(self.delivery_card, 0, 3)

        layout.setHorizontalSpacing(16)
        layout.setContentsMargins(10, 10, 10, 10)

        event_bus.result.connect(
            self.update_result
        )

    def update_result(self, data):

        self.status_card.set_value(
            data.get("status", "Waiting")
        )

        self.driver_card.set_value(
            data.get("driver", "-")
        )

        self.cooking_card.set_value(
            data.get("cooking", "-")
        )

        self.delivery_card.set_value(
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