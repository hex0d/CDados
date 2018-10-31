import sys
from PyQt4 import QtGui as qt

app = qt.QApplication(sys.argv)
window = qt.QWidget()
window.show()
sys.exit(app.exec_())