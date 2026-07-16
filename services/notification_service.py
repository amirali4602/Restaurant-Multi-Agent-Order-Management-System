from services.event_bus import event_bus


class NotificationService:

    @staticmethod
    def order_running():
        event_bus.order_status.emit("RUNNING")

    @staticmethod
    def order_completed():
        event_bus.order_status.emit("COMPLETED")

    @staticmethod
    def inventory_checking():
        event_bus.inventory_status.emit("CHECKING")

    @staticmethod
    def inventory_done():
        event_bus.inventory_status.emit("DONE")

    @staticmethod
    def chef_cooking():
        event_bus.chef_status.emit("COOKING")

    @staticmethod
    def chef_ready():
        event_bus.chef_status.emit("READY")

    @staticmethod
    def delivery_started():
        event_bus.delivery_status.emit("DELIVERING")

    @staticmethod
    def delivery_done():
        event_bus.delivery_status.emit("DELIVERED")

    @staticmethod
    def inventory_result(order):

        event_bus.result.emit(
            {
                "status": "Inventory Confirmed",
                "driver": "-",
                "cooking": "-",
                "eta": "-",
            }
        )

    @staticmethod
    def cooking_started(order):

        event_bus.result.emit(
            {
                "status": "Cooking",
                "driver": "-",
                "cooking": "In Progress",
                "eta": "-",
            }
        )

    @staticmethod
    def cooking_finished(order):

        event_bus.result.emit(
            {
                "status": "Ready",
                "driver": "-",
                "cooking": f"{order.cooking_time} sec",
                "eta": "-",
            }
        )

    @staticmethod
    def delivery_started_result(order):

        event_bus.result.emit(
            {
                "status": "Out for Delivery",
                "driver": order.driver,
                "cooking": f"{order.cooking_time} sec",
                "eta": f"{order.delivery_time} sec",
            }
        )

    @staticmethod
    def delivery_completed_result(order):

        event_bus.result.emit(
            {
                "status": "Delivered ✅",
                "driver": order.driver,
                "cooking": f"{order.cooking_time} sec",
                "eta": "Completed",
            }
        )

    @staticmethod
    def order_failed(order):

        event_bus.result.emit(
            {
                "status": f"❌ {order.failure_stage} Failed",
                "driver": "-",
                "cooking": "-",
                "eta": order.failure_reason,
            }
        )