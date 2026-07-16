from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QFrame, QVBoxLayout


class AgentCard(QFrame):

    COLORS = {
        "IDLE": "#9E9E9E",
        "WAITING": "#9E9E9E",

        "RUNNING": "#FF9800",
        "CHECKING": "#FF9800",
        "COOKING": "#FF9800",
        "DELIVERING": "#FF9800",

        "DONE": "#4CAF50",
        "READY": "#4CAF50",
        "COMPLETED": "#4CAF50",
        "DELIVERED": "#4CAF50",

        "FAILED": "#F44336",
        "CANCELLED": "#F44336",
    }

    def __init__(self, icon, title):
        super().__init__()

        self.setObjectName("agentCard")

        layout = QVBoxLayout(self)

        self.title = QLabel(f"{icon} {title}")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("agentTitle")

        self.status = QLabel("IDLE")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status.setObjectName("agentStatus")

        layout.addWidget(self.title)
        layout.addWidget(self.status)

        self.set_status("IDLE")

    def set_status(self, status):

        color = self.COLORS.get(
            status.upper(),
            "#1565C0"
        )

        self.status.setText(status)

        self.status.setStyleSheet(
            f"""
            font-size:18pt;
            font-weight:bold;
            color:{color};
            """
        )