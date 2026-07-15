import sys

from PySide6.QtWidgets import QApplication

from gui.styles import APP_STYLE
from gui.main_window import MainWindow

from services.agent_manager import AgentManager


def main():

    app = QApplication(sys.argv)

    app.setStyleSheet(APP_STYLE)

    # Start the Multi-Agent System
    manager = AgentManager()
    manager.start()

    # Create the GUI
    window = MainWindow(manager)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()