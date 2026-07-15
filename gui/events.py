from PySide6.QtCore import QObject, Signal


class GuiEvents(QObject):

    activity = Signal(str)

    order_status = Signal(str)

    inventory_status = Signal(str)

    chef_status = Signal(str)

    delivery_status = Signal(str)

    result_status = Signal(str)

    driver = Signal(str)

    cooking_time = Signal(str)

    delivery_eta = Signal(str)