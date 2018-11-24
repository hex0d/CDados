#####################################################################################
#
#           Project: Estudo Comunicação de Dados
#           Funcion: Tranmit information through net using MLT-3 protocol
#           Owner: Leonardo, Bigarelli, Vitor
#
#####################################################################################


from PyQt5 import QtCore, QtGui, QtWidgets
from MPL import *
import threading
import socket
import pickle






class Ui_Server(object):
    lock = threading.Lock()
    recv_data = None

    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(733, 444)
        self.str_msg_save = ''
        self.MLT_array_save = []
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.butt_graph_bin = QtWidgets.QPushButton(self.centralwidget)
        self.butt_graph_bin.setGeometry(QtCore.QRect(610, 200, 61, 41))
        self.butt_graph_bin.setObjectName("butt_graph_bin")
        self.butt_graph_bin.clicked.connect(self.plot_bin)
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
        self.butt_graph_MLT.clicked.connect(self.plot_MLT)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 241, 31))
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(0, 310, 551, 41))
        self.status_label.setObjectName("status_label")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.butt_send = QtWidgets.QPushButton(self.centralwidget)
        self.butt_send.setGeometry(QtCore.QRect(570, 330, 141, 51))
        self.butt_send.setObjectName("butt_send")
        self.butt_send.clicked.connect(self.server_start)
        self.port_box = QtWidgets.QLineEdit(self.centralwidget)
        self.port_box.setGeometry(QtCore.QRect(330, 80, 113, 20))
        self.port_box.setObjectName("port_box")
        self.port_box.setMaxLength(5)
        self.port_box.setValidator(QtGui.QIntValidator())
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 110, 101, 16))
        self.label_6.setObjectName("label_6")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 200, 551, 51))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 549, 49))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bin_opt = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.bin_opt.setStyleSheet("")
        self.bin_opt.setText("")
        self.bin_opt.setWordWrap(True)
        self.bin_opt.setObjectName("bin_opt")
        self.horizontalLayout_2.addWidget(self.bin_opt)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(50, 260, 551, 51))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 549, 49))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.MLT_opt = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.MLT_opt.setStyleSheet("")
        self.MLT_opt.setText("")
        self.MLT_opt.setWordWrap(True)
        self.MLT_opt.setObjectName("MLT_opt")
        self.horizontalLayout_3.addWidget(self.MLT_opt)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(50, 130, 551, 61))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 549, 59))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.str_msg = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.str_msg.setStyleSheet("")
        self.str_msg.setWordWrap(True)
        self.str_msg.setObjectName("str_msg")
        self.horizontalLayout.addWidget(self.str_msg)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
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

    def decoder(self,array_MLT):
        array_msg = []
        array_MLT.insert(0, 0)
        for i, j in zip(array_MLT, array_MLT[1:]):
            if i == j:
                array_msg.append(0)
            else:
                array_msg.append(1)
        bin_opt = ''.join(str(x) for x in array_msg)
        text = self.decode_binary_string(bin_opt)
        return {'bin_opt': bin_opt,  # binary message
                'array_msg': array_msg,
                'text': text}

    def decode_binary_string(self,s):
        return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))

    def display_data(self,data):

        self.MLT_opt.setText(''.join(str(data)))
        printable_data = self.decoder(data)
        bin_str = printable_data['bin_opt']
        bin_str = ' '.join(bin_str[i:i + 8] for i in range(0, len(bin_str), 8))
        self.str_msg_save = bin_str
        self.MLT_array_save = data
        self.bin_opt.setText(bin_str)
        self.str_msg.setText(printable_data['text'])


    def plot_bin(self):
        test = []
        if self.str_msg_save == '':
            self.bin_opt.setText('No Bin MSG')
        else:
            for c in self.str_msg_save:
                if c =='1' or c=='0':
                    test.append(int(c))
                else:
                    continue
            plot_graph(test)
    def plot_MLT(self):
        if len(self.MLT_array_save) <= 1:
            self.MLT_opt.setText('No MLT MSG')
        else:
            plot_graph(self.MLT_array_save)

    def server_socket(self,port):
        host = ''
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((host, port))
        except socket.error as e:
            print(str(e))
        sock.listen(5)
        print("Waiting for Connection")
        while True:
            conn, addr = sock.accept()
            print('Connected to ' + addr[0] + ':' + str(addr[1]))
            data = conn.recv(1024)
            if not data:
                break
            data = pickle.loads(data)
            if type(data) is list:
                conn.send(str.encode('ok'))
                self.display_data(data)
            else:
                conn.send(str.encode('error'))

        conn.close()
        return

    def start_thread(self,port):
        t = threading.Thread(target=self.server_socket,args=[port],daemon=True)
        t.start()
        return

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "Server"))
        self.butt_graph_bin.setText(_translate("Server", "Graph"))
        self.bin_opt.setText(_translate("Server", ""))
        self.MLT_opt.setText(_translate("Server", ""))
        self.label_5.setText(_translate("Server", "Port"))
        self.label_5.setText(_translate("Server", "Port"))
        self.butt_exit.setText(_translate("Server", "Exit"))
        self.status_label.setText(_translate("ClientWindow", "waiting"))
        self.butt_graph_MLT.setText(_translate("Server", "Graph"))
        self.label.setText(_translate("Server", "Server Address"))
        self.butt_send.setText(_translate("Server", "Listen"))
        self.str_msg.setText(_translate("Server", ""))
        self.label_6.setText(_translate("Server", "Message Received"))
    def server_start(self):
        if self.port_box.text() != '':
            port = int(self.port_box.text())  # int
            self.status_label.setText("")
        else:
            self.status_label.setText("Fill Port")
            return
        self.start_thread(port)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_Server()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
