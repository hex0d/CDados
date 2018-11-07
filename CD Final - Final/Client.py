#####################################################################################
#
#           Project: Estudo Comunicação de Dados
#           Funcion: Tranmit information through net using MLT-3 protocol
#           Owner: Leonardo, Bigarelli, Vitor
#
#####################################################################################



from PyQt5 import QtCore, QtGui, QtWidgets
from Decode import *
import socket
import pickle

class Ui_ClientWindow(object):

    def setupUi(self, ClientWindow):
        ClientWindow.setObjectName("ClientWindow")
        ClientWindow.resize(698, 416)
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"  # Part of the regular expression
        # Regulare expression
        ipRegex = QtCore.QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QtGui.QRegExpValidator(ipRegex)

        self.centralwidget = QtWidgets.QWidget(ClientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.msg_box = QtWidgets.QLineEdit(self.centralwidget)
        self.msg_box.setGeometry(QtCore.QRect(30, 120, 551, 31))
        self.msg_box.setObjectName("msg_box")
        self.bin_opt = QtWidgets.QLabel(self.centralwidget)
        self.bin_opt.setGeometry(QtCore.QRect(30, 170, 551, 41))
        self.bin_opt.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.bin_opt.setObjectName("label_2")
        self.MLT_opt = QtWidgets.QLabel(self.centralwidget)
        self.MLT_opt.setGeometry(QtCore.QRect(30, 250, 551, 41))
        self.MLT_opt.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.MLT_opt.setObjectName("MLT_opt")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(0, 310, 551, 41))
        self.status_label.setObjectName("status_label")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.butt_send = QtWidgets.QPushButton(self.centralwidget)
        self.butt_send.setGeometry(QtCore.QRect(540, 310, 141, 51))
        self.butt_send.setObjectName("butt_send")
        self.butt_send.clicked.connect(self.send)
        self.butt_graph_bin = QtWidgets.QPushButton(self.centralwidget)
        self.butt_graph_bin.setGeometry(QtCore.QRect(590, 170, 61, 41))
        self.butt_graph_bin.setObjectName("butt_graph_bin")
        self.butt_graph_MLT = QtWidgets.QPushButton(self.centralwidget)
        self.butt_graph_MLT.setGeometry(QtCore.QRect(590, 250, 61, 41))
        self.butt_graph_MLT.setObjectName("butt_graph_MLT")
        self.butt_exit = QtWidgets.QPushButton(self.centralwidget)
        self.butt_exit.setGeometry(QtCore.QRect(20, 320, 75, 23))
        self.butt_exit.setObjectName("butt_exit")
        self.butt_exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 241, 31))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ip_box = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_box.setGeometry(QtCore.QRect(204, 70, 113, 20))
        self.ip_box.setObjectName("ip_box")
        self.ip_box.setValidator(ipValidator)
        self.port_box = QtWidgets.QLineEdit(self.centralwidget)
        self.port_box.setGeometry(QtCore.QRect(430, 70, 113, 20))
        self.port_box.setObjectName("port_box")
        self.port_box.setMaxLength(5)
        self.port_box.setValidator(QtGui.QIntValidator())
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 70, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 70, 61, 20))
        self.label_5.setObjectName("label_5")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 170, 551, 61))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 549, 59))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bin_opt = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.bin_opt.setStyleSheet("")
        self.bin_opt.setText("")
        self.bin_opt.setScaledContents(False)
        self.bin_opt.setWordWrap(True)
        self.bin_opt.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.bin_opt)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 240, 551, 61))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 549, 59))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MLT_opt = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.MLT_opt.setStyleSheet("")
        self.MLT_opt.setText("")
        self.MLT_opt.setObjectName("MLT_opt")
        self.horizontalLayout_2.addWidget(self.MLT_opt)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        ClientWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ClientWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName("menubar")
        ClientWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ClientWindow)
        self.statusbar.setObjectName("statusbar")
        ClientWindow.setStatusBar(self.statusbar)
        self.bin_opt.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.MLT_opt.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.retranslateUi(ClientWindow)
        QtCore.QMetaObject.connectSlotsByName(ClientWindow)

    def client_socket(self, host, port, message):
        try:
            sock = socket.socket()
            sock.connect((host, port))
            message = pickle.dumps(message)
            sock.send(message)
            data = sock.recv(1024)
            if data.decode('utf-8') == 'ok':
                print(data.decode('utf-8'))
                sock.close()
                return 1
            else:
                return 0
        except socket.error as e:
            return str(e)

    def retranslateUi(self, ClientWindow):
        _translate = QtCore.QCoreApplication.translate
        ClientWindow.setWindowTitle(_translate("ClientWindow", "Client"))
        self.msg_box.setPlaceholderText(_translate("ClientWindow", "Insert your message here"))
        self.bin_opt.setText(_translate("ClientWindow", ""))
        self.ip_box.setText(_translate("ClientWindow", "127.0.0.1"))
        self.MLT_opt.setText(_translate("ClientWindow", ""))
        self.status_label.setText(_translate("ClientWindow", ""))
        self.butt_send.setText(_translate("ClientWindow", "Send"))
        self.butt_graph_bin.setText(_translate("ClientWindow", "Graph"))
        self.butt_graph_MLT.setText(_translate("ClientWindow", "Graph"))
        self.butt_exit.setText(_translate("ClientWindow", "Exit"))
        self.label.setText(_translate("ClientWindow", "Server Address"))
        self.label_4.setText(_translate("ClientWindow", "IP Address"))
        self.label_5.setText(_translate("ClientWindow", "Port"))
    def send(self):

        if self.ip_box.text() != '':
            ip_addr = self.ip_box.text()  # str
        else:
            self.status_label.setText("Fill Ip Address")
            return
        if self.port_box.text() != '':
            port = int(self.port_box.text())  # int
        else:
            self.status_label.setText("Fill Port")
            return
        if self.ip_box.text() != '' and self.port_box.text() != '':
            self.status_label.setText("")
        self.msg_to_decode = self.msg_box.text()
        self.dec_msg = to_bin(self.msg_to_decode)
        self.str_msg = self.dec_msg['bin_msg']
        self.str_msg = ' '.join(self.str_msg[i:i + 8] for i in range(0, len(self.str_msg), 8))
        self.bin_opt.setText(self.str_msg)
        self.MLT_array = to_MLT(self.dec_msg['array_msg'])
        self.MLT_opt.setText(''.join(str(to_MLT(self.dec_msg['array_msg']))))
        a = self.client_socket(ip_addr,port,self.MLT_array)
        if a == 1:
            self.status_label.setText("Message Was Sent")
        else:
            self.status_label.setText("Error Sending Message")
        return 0



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_ClientWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
