import json
import sqlite3

from database.connection import get_connection


class OrderRepository:

    @staticmethod
    def save(order):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO orders
            (
                order_id,
                customer,
                items,
                status,
                driver,
                cooking_time,
                delivery_time,
                created_at,
                completed_at,
                failure_stage,
                failure_reason
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                order.order_id,
                order.customer,
                json.dumps(order.items),
                order.status,
                order.driver,
                order.cooking_time,
                order.delivery_time,
                order.created_at,
                order.completed_at,
                order.failure_stage,
                order.failure_reason,
            ),
        )

        connection.commit()
        connection.close()

    @staticmethod
    def get_all():

        connection = get_connection()
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM orders
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        connection.close()

        return rows

    @staticmethod
    def clear():

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("DELETE FROM orders")

        connection.commit()
        connection.close()

    @staticmethod
    def get_statistics():

        connection = get_connection()
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) AS total FROM orders")
        total = cursor.fetchone()["total"]

        cursor.execute(
            """
            SELECT COUNT(*) AS delivered
            FROM orders
            WHERE status='DELIVERED'
            """
        )
        delivered = cursor.fetchone()["delivered"]

        cancelled = total - delivered

        success_rate = (
            round((delivered / total) * 100, 1)
            if total > 0 else 0
        )

        cursor.execute(
            "SELECT AVG(cooking_time) AS avg_cooking FROM orders"
        )
        avg_cooking = cursor.fetchone()["avg_cooking"] or 0

        cursor.execute(
            "SELECT AVG(delivery_time) AS avg_delivery FROM orders"
        )
        avg_delivery = cursor.fetchone()["avg_delivery"] or 0

        cursor.execute(
            """
            SELECT customer, COUNT(*) AS cnt
            FROM orders
            GROUP BY customer
            ORDER BY cnt DESC
            LIMIT 1
            """
        )

        row = cursor.fetchone()
        top_customer = row["customer"] if row else "-"

        cursor.execute("SELECT items FROM orders")

        item_counter = {}

        for row in cursor.fetchall():

            items = json.loads(row["items"])

            for item, quantity in items.items():

                item_counter[item] = (
                    item_counter.get(item, 0)
                    + quantity
                )

        most_ordered_item = "-"

        if item_counter:

            most_ordered_item = max(
                item_counter,
                key=item_counter.get,
            )

        cursor.execute(
            """
            SELECT failure_stage, COUNT(*) AS cnt
            FROM orders
            WHERE failure_stage != ''
            GROUP BY failure_stage
            """
        )

        failures = {
            "Inventory": 0,
            "Chef": 0,
            "Delivery": 0,
        }

        for row in cursor.fetchall():
            failures[row["failure_stage"]] = row["cnt"]

        connection.close()

        return {
            "total": total,
            "delivered": delivered,
            "cancelled": cancelled,
            "success_rate": success_rate,
            "avg_cooking": round(avg_cooking, 1),
            "avg_delivery": round(avg_delivery, 1),
            "top_customer": top_customer,
            "most_ordered_item": most_ordered_item,
            "inventory_failures": failures["Inventory"],
            "chef_failures": failures["Chef"],
            "delivery_failures": failures["Delivery"],
        }