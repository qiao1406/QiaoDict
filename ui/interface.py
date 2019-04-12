import sys
from ui import uiform
from PyQt5 import QtCore, QtGui, QtWidgets


app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
ui = uiform.Ui_Form()
ui.setupUi(widget)
widget.show()
sys.exit(app.exec_())
