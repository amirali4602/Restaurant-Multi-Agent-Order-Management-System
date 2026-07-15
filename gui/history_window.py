from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)

from database.repository import OrderRepository


class HistoryWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Order History")
        self.resize(1000, 500)

        layout = QVBoxLayout(self)

        self.table = QTableWidget()

        layout.addWidget(self.table)

        self.load_orders()

    def load_orders(self):

        orders = OrderRepository.get_all()

        headers = [
            "Order ID",
            "Customer",
            "Items",
            "Status",
            "Driver",
            "Cooking",
            "Delivery",
            "Created",
            "Completed",
        ]

        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)

        self.table.setRowCount(len(orders))

        for row, order in enumerate(orders):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(order["order_id"]),
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(order["customer"]),
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(order["items"]),
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(order["status"]),
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(order["driver"]),
            )

            self.table.setItem(
                row,
                5,
                QTableWidgetItem(str(order["cooking_time"])),
            )

            self.table.setItem(
                row,
                6,
                QTableWidgetItem(str(order["delivery_time"])),
            )

            self.table.setItem(
                row,
                7,
                QTableWidgetItem(order["created_at"]),
            )

            self.table.setItem(
                row,
                8,
                QTableWidgetItem(order["completed_at"]),
            )

        self.table.resizeColumnsToContents()