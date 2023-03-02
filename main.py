import encodings
import sys
import socket
import threading
import requests
import json
from PySide6.QtWidgets import QApplication, QMainWindow

from main_win_cor import Ui_MainWindow, QPushButton


class AngleCounter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_calculate.clicked.connect(lambda: self.create_json())
        self.ui.pushButton_send.clicked.connect(lambda: self.read_sock())

    def take_value_x0(self):
        value = self.ui.lineEdit_x0.text()
        return value

    def take_value_y0(self):
        value = self.ui.lineEdit_y0.text()
        return value

    def take_value_z0(self):
        value = self.ui.lineEdit_z0.text()
        return value

    def take_value_x(self):
        value = self.ui.lineEdit_x.text()
        return value

    def take_value_y(self):
        value = self.ui.lineEdit_y.text()
        return value

    def take_value_z(self):
        value = self.ui.lineEdit_z.text()
        return value

    def take_value_v0(self):
        value = self.ui.lineEdit_v0.text()
        return value

    def take_value_g(self):
        value = self.ui.lineEdit_g.text()
        return value

    def take_value_r(self):
        value = self.ui.lineEdit_R.text()
        return value

    def create_json(self):
        x0 = self.take_value_x0()
        y0 = self.take_value_y0()
        z0 = self.take_value_z0()
        x = self.take_value_x()
        y = self.take_value_y()
        z = self.take_value_z()
        v0 = self.take_value_v0()
        g = self.take_value_g()
        R = self.take_value_r()
        myList = [{'x0': x0, 'y0': y0, 'z0': z0}, {'x': x, 'y': y, 'z': z}, {'v0': v0, 'g': g, 'R': R}]
        jsonString = json.dumps(myList, indent=4)
        file_json = open("ToServer.json", "w")
        file_json.write(jsonString)
        return file_json

    def read_sock(self):
        ip = '127.0.0.1'
        port = 5557

        server = socket.socket()
        server.connect((ip, port))
        f_name = input(str(self.create_json()))
        server.send((bytes(f_name, encoding='UTF-8')))
        f = open(f_name, "rb")
        l = f.read(1024)
        while l:
            server.send(l)
            #l = f.read(1024)
            print(f)
        f.close()
        server.close()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AngleCounter()
    window.show()
    window.setFixedSize(724, 361)


    sys.exit(app.exec())