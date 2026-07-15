from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QGroupBox
from services.event_bus import event_bus

class ActivityPanel(QGroupBox):

    def __init__(self):
        super().__init__("Activity Log")

        layout = QVBoxLayout(self)

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        self.log.append("===================================")
        self.log.append("Restaurant Multi-Agent System")
        self.log.append("System initialized.")
        self.log.append("Waiting for new orders...")
        self.log.append("===================================")

        layout.addWidget(self.log)
        event_bus.activity.connect(
            self.add
        )
    def add(self, text):

        self.log.append(text)
    def clear(self):
        self.log.clear()