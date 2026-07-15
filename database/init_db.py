from database.connection import get_connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orders
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            order_id TEXT NOT NULL,

            customer TEXT NOT NULL,

            items TEXT NOT NULL,

            status TEXT NOT NULL,

            driver TEXT,

            cooking_time INTEGER,

            delivery_time INTEGER,

            created_at TEXT,

            completed_at TEXT
        )
        """
    )

    connection.commit()

    connection.close()


if __name__ == "__main__":

    initialize_database()

    print("Database initialized successfully.")