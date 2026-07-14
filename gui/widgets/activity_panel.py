from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel


class ActivityPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Agent Activity"))

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        self.log.append("Waiting for incoming orders...")

        layout.addWidget(self.log)

    def add_log(self, text):

        self.log.append(text)