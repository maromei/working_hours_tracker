from datetime import datetime

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton

from working_hours_tracker import settings, time_file


class MainWindow(QMainWindow):

    start_time_btn: QPushButton
    end_time_btn: QPushButton

    start_end_time_btn: QPushButton

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi(settings.get_main_window_ui_path(), self)

        self.setWindowTitle("Worktime Tracker")

        self.start_time_btn.pressed.connect(self.write_start_time)
        self.end_time_btn.pressed.connect(self.write_end_time)

        self.start_end_time_btn.pressed.connect(self.toggle_write_time)

    def toggle_write_time(self):

        now = datetime.now()
        time_file_path = settings.get_time_file_path()

        if time_file.has_open_time(time_file_path):
            time_file.add_end_time(time_file_path, now)
            self.start_end_time_btn.setText("Start")
        else:
            time_file.add_start_time(time_file_path, now)
            self.start_end_time_btn.setText("End")

    def write_start_time(self):

        now = datetime.now()
        time_file_path = settings.get_time_file_path()
        time_file.add_start_time(time_file_path, now)

    def write_end_time(self):

        now = datetime.now()
        time_file_path = settings.get_time_file_path()
        time_file.add_end_time(time_file_path, now)
