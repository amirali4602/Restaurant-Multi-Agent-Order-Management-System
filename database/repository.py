import json

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
                completed_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            ),
        )

        connection.commit()
        connection.close()

    @staticmethod
    def get_all():

        connection = get_connection()

        connection.row_factory = __import__("sqlite3").Row

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