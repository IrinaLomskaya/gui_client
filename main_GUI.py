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
        #self.ui.pushButton_send.clicked.connect(lambda: self.read_sock())
        #self.ui.pushButton_get.clicked.connect(lambda: self.changed_data())

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
        x = self.take_value_x()
        y = self.take_value_y()
        g = self.take_value_g()
        R = self.take_value_r()
        myList = [{'x': x, 'y': y}]
        list_g = [{'g': g}]
        #list_R = [{}]
        jsonString = json.dumps(myList, indent=4)
        jsonString2 = json.dumps(list_g, indent=4)
        file_json = open("ToServer.json", "w")
        file_json2 = open("ToServer_g.json", "w")
        file_json.write(jsonString)
        file_json2.write(jsonString2)
        file_json.close()
        file_json2.close()
        res = requests.put("http://localhost:5556/api/flask_server")

        def op():
            with open('ToClientSolved.json') as file:
                templates = json.load(file)
            return templates
        azimuth = op()[0]["azimuth"]
        elevation = op()[0]["elevation"]
        speed = op()[0]["speed"]
        self.ui.label_azim.setText(str(azimuth))
        self.ui.label_elev.setText(str(elevation))
        self.ui.label_V.setText(str(speed))
        return file_json, file_json2

    #def read_sock(self):
        #res = requests.get("http://localhost:5555/api/flask_test")
        #print(res.json())

    def changed_data(self):
        res = requests.put("http://localhost:5556/api/flask_server")
        k = res.json()
        print(k)
        #data = k[0]['x']
        self.ui.label_azim.setText(str(k))
        #print(data)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AngleCounter()
    window.show()
    window.setFixedSize(724, 264)


    sys.exit(app.exec())