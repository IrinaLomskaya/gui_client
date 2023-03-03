import encodings
import sys
import socket
import threading
import requests
import json
from io import StringIO
from PySide6.QtWidgets import QApplication, QMainWindow

from main_win_edit import Ui_MainWindow, QPushButton


class AngleCounter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_calculate.clicked.connect(lambda: self.create_json())



    def take_value_x(self):
        value = self.ui.lineEdit_x.text()
        return value

    def take_value_y(self):
        value = self.ui.lineEdit_y.text()
        return value

    def take_value_g(self):
        value = self.ui.lineEdit_g.text()
        return value

    def take_value_r(self):
        value = self.ui.lineEdit_R.text()
        return value

    def create_json(self):
        x = self.take_value_x()
        y = self.take_value_y()
        g = self.take_value_g()
        R = self.take_value_r()
        myList = [{'x': x, 'y': y}]
        list_g = [{'g': g}]
        send = requests.post("http://localhost:5556/api/flask_server", data=myList).json()
        azimuth = send[0]["azimuth"]
        elevation = send[0]["elevation"]
        speed = send[0]["speed"]
        self.ui.label_azim.setText(str(azimuth))
        self.ui.label_elev.setText(str(elevation))
        self.ui.label_V.setText(str(speed))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AngleCounter()
    window.show()
    window.setFixedSize(724, 264)


    sys.exit(app.exec())