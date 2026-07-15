from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QFormLayout,
    QGroupBox,
    QHeaderView,
    QLabel,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

from database.repository import OrderRepository


class HistoryWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Order History")
        self.resize(1100, 700)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Search Customer"))

        self.search = QLineEdit()
        self.search.setPlaceholderText(
            "Type customer name..."
        )
        layout.addWidget(self.search)

        self.table = QTableWidget()

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.table.setSortingEnabled(True)

        layout.addWidget(self.table)

        # ---------- Statistics ----------
        stats_box = QGroupBox("Statistics")

        stats_layout = QFormLayout(stats_box)

        self.total_orders = QLabel("-")
        self.avg_cooking = QLabel("-")
        self.avg_delivery = QLabel("-")
        self.top_customer = QLabel("-")
        self.top_item = QLabel("-")

        stats_layout.addRow(
            "Total Orders:",
            self.total_orders,
        )

        stats_layout.addRow(
            "Average Cooking Time:",
            self.avg_cooking,
        )

        stats_layout.addRow(
            "Average Delivery Time:",
            self.avg_delivery,
        )

        stats_layout.addRow(
            "Top Customer:",
            self.top_customer,
        )

        stats_layout.addRow(
            "Most Ordered Item:",
            self.top_item,
        )

        layout.addWidget(stats_box)

        self.orders = []

        self.search.textChanged.connect(
            self.load_orders
        )

        self.load_orders()

        self.load_statistics()

    def load_orders(self):

        self.orders = OrderRepository.get_all()

        keyword = self.search.text().lower().strip()

        filtered = []

        for order in self.orders:

            if keyword in order["customer"].lower():
                filtered.append(order)

        headers = [
            "Order ID",
            "Customer",
            "Items",
            "Status",
            "Driver",
            "Cooking (s)",
            "Delivery (s)",
            "Created",
            "Completed",
        ]

        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(filtered))

        for row, order in enumerate(filtered):

            values = [
                order["order_id"],
                order["customer"],
                order["items"],
                order["status"],
                order["driver"] or "-",
                str(order["cooking_time"] or "-"),
                str(order["delivery_time"] or "-"),
                order["created_at"] or "-",
                order["completed_at"] or "-",
            ]

            for column, value in enumerate(values):

                item = QTableWidgetItem(str(value))

                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )

                self.table.setItem(
                    row,
                    column,
                    item,
                )

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.table.resizeRowsToContents()

    def load_statistics(self):

        stats = OrderRepository.get_statistics()

        self.total_orders.setText(
            str(stats["total"])
        )

        self.avg_cooking.setText(
            f'{stats["avg_cooking"]} sec'
        )

        self.avg_delivery.setText(
            f'{stats["avg_delivery"]} sec'
        )

        self.top_customer.setText(
            stats["top_customer"]
        )

        self.top_item.setText(
            stats["most_ordered_item"]
        )