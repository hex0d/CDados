# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Server.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(733, 444)
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.butt_graph_bin = QtWidgets.QPushButton(self.centralwidget)
        self.butt_graph_bin.setGeometry(QtCore.QRect(610, 200, 61, 41))
        self.butt_graph_bin.setObjectName("butt_graph_bin")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 551, 41))
        self.label_2.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 551, 41))
        self.label_3.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 80, 61, 20))
        self.label_5.setObjectName("label_5")
        self.butt_exit = QtWidgets.QPushButton(self.centralwidget)
        self.butt_exit.setGeometry(QtCore.QRect(40, 360, 75, 23))
        self.butt_exit.setObjectName("butt_exit")
        self.butt_exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.butt_graph_MLT = QtWidgets.QPushButton(self.centralwidget)
        self.butt_graph_MLT.setGeometry(QtCore.QRect(610, 260, 61, 41))
        self.butt_graph_MLT.setObjectName("butt_graph_MLT")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.butt_send = QtWidgets.QPushButton(self.centralwidget)
        self.butt_send.setGeometry(QtCore.QRect(560, 320, 141, 51))
        self.butt_send.setObjectName("butt_send")
        self.port_box = QtWidgets.QLineEdit(self.centralwidget)
        self.port_box.setGeometry(QtCore.QRect(330, 80, 113, 20))
        self.port_box.setObjectName("port_box")
        self.port_box.setMaxLength(5)
        self.port_box.setValidator(QtGui.QIntValidator())
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 551, 41))
        self.label_4.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 100, 101, 16))
        self.label_6.setObjectName("label_6")
        Server.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Server)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 21))
        self.menubar.setObjectName("menubar")
        Server.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Server)
        self.statusbar.setObjectName("statusbar")
        Server.setStatusBar(self.statusbar)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "ServerMenu"))
        self.butt_graph_bin.setText(_translate("Server", "Graph"))
        self.label_2.setText(_translate("Server", "TextLabel"))
        self.label_3.setText(_translate("Server", "TextLabel"))
        self.label_5.setText(_translate("Server", "Port"))
        self.butt_exit.setText(_translate("Server", "Exit"))
        self.butt_graph_MLT.setText(_translate("Server", "Graph"))
        self.label.setText(_translate("Server", "Server Address"))
        self.butt_send.setText(_translate("Server", "Listen"))
        self.label_4.setText(_translate("Server", "TextLabel"))
        self.label_6.setText(_translate("Server", "Message Received"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_Server()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
