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
from PySide6.QtWidgets import QGridLayout
from gui.widgets.stat_card import StatCard
from database.repository import OrderRepository
from PySide6.QtGui import QIcon
from PySide6.QtGui import QShortcut, QKeySequence


class HistoryWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Order History")
        self.setWindowIcon(QIcon("assets/restaurant.jpg"))
        self.resize(1300, 750)

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

        # ---------------- Statistics ----------------

        stats_box = QGroupBox("Restaurant Statistics")

        stats_layout = QGridLayout(stats_box)

        self.total_orders = StatCard("Total Orders")
        self.delivered_orders = StatCard("Delivered Orders")
        self.cancelled_orders = StatCard("Cancelled Orders")

        self.success_rate = StatCard("Success Rate")
        self.avg_cooking = StatCard("Avg Cooking")
        self.avg_delivery = StatCard("Avg Delivery")

        self.inventory_failures = StatCard("Inventory Failures")
        self.chef_failures = StatCard("Chef Failures")
        self.delivery_failures = StatCard("Delivery Failures")

        self.top_customer = StatCard("Top Customer")
        self.top_item = StatCard("Most Ordered Item")

        cards = [
            self.total_orders,
            self.delivered_orders,
            self.cancelled_orders,
            self.success_rate,
            self.avg_cooking,
            self.avg_delivery,
            self.inventory_failures,
            self.chef_failures,
            self.delivery_failures,
            self.top_customer,
            self.top_item,
        ]

        columns = 6

        for index, card in enumerate(cards):

            row = index // columns
            column = index % columns

            stats_layout.addWidget(
                card,
                row,
                column,
            )

        layout.addWidget(stats_box)
        self.orders = []

        self.search.textChanged.connect(
            self.load_orders
        )

        self.load_orders()
        self.load_statistics()
        self.fullscreen_shortcut = QShortcut(
            QKeySequence("F11"),
            self,
        )

        self.fullscreen_shortcut.activated.connect(
            self.toggle_fullscreen
        )

    def load_orders(self):

        self.orders = OrderRepository.get_all()

        keyword = self.search.text().lower().strip()

        filtered = [
            order
            for order in self.orders
            if keyword in order["customer"].lower()
        ]

        headers = [
            "Order ID",
            "Customer",
            "Items",
            "Status",
            "Driver",
            "Cooking (s)",
            "Delivery (s)",
            "Failure Stage",
            "Failure Reason",
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
                order["cooking_time"] or "-",
                order["delivery_time"] or "-",
                order["failure_stage"] or "-",
                order["failure_reason"] or "-",
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

        self.total_orders.set_value(
            stats["total"]
        )

        self.delivered_orders.set_value(
            stats["delivered"]
        )

        self.cancelled_orders.set_value(
            stats["cancelled"]
        )

        self.success_rate.set_value(
            f'{stats["success_rate"]}%'
        )

        self.inventory_failures.set_value(
            stats["inventory_failures"]
        )

        self.chef_failures.set_value(
            stats["chef_failures"]
        )

        self.delivery_failures.set_value(
            stats["delivery_failures"]
        )

        self.avg_cooking.set_value(
            f'{stats["avg_cooking"]} sec'
        )

        self.avg_delivery.set_value(
            f'{stats["avg_delivery"]} sec'
        )

        self.top_customer.set_value(
            stats["top_customer"]
        )

        self.top_item.set_value(
            stats["most_ordered_item"]
        )

    def toggle_fullscreen(self):

        if self.isFullScreen():
            self.showNormal()
            self.showMaximized()
        else:
            self.showFullScreen()