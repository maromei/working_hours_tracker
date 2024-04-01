import sys
import logging

from PyQt5.QtWidgets import QApplication

from working_hours_tracker.display import MainWindow


logger = logging.getLogger(__name__)


def run():

    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec_()


if __name__ == "__main__":

    try:
        run()
    except Exception as e:
        logger.error(f"Error in Main: {e}")
        raise e
