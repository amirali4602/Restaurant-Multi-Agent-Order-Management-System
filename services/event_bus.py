from PySide6.QtCore import QObject, Signal


class EventBus(QObject):

    activity = Signal(str)

    order_status = Signal(str)

    inventory_status = Signal(str)

    chef_status = Signal(str)

    delivery_status = Signal(str)

    result = Signal(dict)


event_bus = EventBus()