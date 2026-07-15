from datetime import datetime

from services.event_bus import event_bus


class AppLogger:

    @staticmethod
    def info(message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")

        log = f"[{timestamp}] INFO  {message}"

        print(log)

        event_bus.activity.emit(log)

    @staticmethod
    def warning(message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")

        log = f"[{timestamp}] WARN  {message}"

        print(log)

        event_bus.activity.emit(log)

    @staticmethod
    def error(message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")

        log = f"[{timestamp}] ERROR {message}"

        print(log)

        event_bus.activity.emit(log)