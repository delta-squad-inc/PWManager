import redismodel 
import redis
import gui
from PySide6 import QtCore, QtWidgets, QtGui
import sys
import cipher

def main():
    app = QtWidgets.QApplication([])

    widget = gui.PWManagerGUI()
    widget.resize(1080, 720)
    widget.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
