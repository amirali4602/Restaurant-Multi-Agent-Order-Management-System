import sys

from pathlib import Path
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow

from gui.style_loader import load_stylesheet
from services.agent_manager import AgentManager


def main():

    app = QApplication(sys.argv)

    app.setStyleSheet(load_stylesheet())

    # Start the Multi-Agent System
    manager = AgentManager()
    manager.start()

    # Create the GUI
    window = MainWindow(manager)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()