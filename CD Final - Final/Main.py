#####################################################################################
#
#           Project: Estudo Comunicação de Dados
#           Funcion: Tranmit information through net using MLT-3 protocol
#           Owner: Leonardo, Bigarelli, Vitor
#
#####################################################################################



################################ -- Imports -- #######################################

from Client import *
from Server import *

################################ -- MainMenu UI -- #######################################

class Ui_MainMenu(object):
    #open new client UI window
    def openClient(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ClientWindow()
        self.ui.setupUi(self.window)
        w.hide()
        self.window.show()
    #open new server UI window
    def openServer(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Server()
        self.ui.setupUi(self.window)
        w.hide()
        self.window.show()
    #setup for the MainMenu ui elements
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(720, 238)
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.butt_client = QtWidgets.QPushButton(self.centralwidget)
        self.butt_client.setGeometry(QtCore.QRect(430, 50, 171, 91))
        self.butt_client.setObjectName("butt_client")
        self.butt_client.clicked.connect(self.openClient)
        self.butt_server = QtWidgets.QPushButton(self.centralwidget)
        self.butt_server.setGeometry(QtCore.QRect(140, 50, 161, 91))
        self.butt_server.setObjectName("butt_server")
        self.butt_server.clicked.connect(self.openServer)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.butt_exit = QtWidgets.QPushButton(self.centralwidget)
        self.butt_exit.setGeometry(QtCore.QRect(630, 170, 75, 23))
        self.butt_exit.setObjectName("butt_exit")
        self.butt_exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName("menubar")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)
        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "MLT-3 Decoder"))
        self.butt_client.setText(_translate("MainMenu", "Client"))
        self.butt_server.setText(_translate("MainMenu", "Server"))
        self.label.setText(_translate("MainMenu", "Choose your Service"))
        self.butt_exit.setText(_translate("MainMenu", "Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())

