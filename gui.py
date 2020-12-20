import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import redismodel

class PWManagerGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Enter the masterpassword")
        self.button2 = QtWidgets.QPushButton("Press, to get password")
        self.button3 = QtWidgets.QPushButton("Press, to set password")

        
        self.lineEdit1 = QtWidgets.QLineEdit()
        self.lineEdit1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)#password mode
        self.lineEdit2 = QtWidgets.QLineEdit("Enter site name")
        self.lineEdit3 = QtWidgets.QLineEdit("Enter site name and then the password next to it")
        self.lineEdit4 = QtWidgets.QLineEdit()
        self.lineEdit4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)#password mode
        

        self.text = QtWidgets.QTextEdit("Hello user!")

        self.layout = QtWidgets.QVBoxLayout()
        self.sublayout = QtWidgets.QHBoxLayout()
        self.sublayout.addWidget(self.lineEdit3)
        self.sublayout.addWidget(self.lineEdit4)

        self.layout.addWidget(self.text)

        self.layout.addWidget(self.lineEdit1)
        self.layout.addWidget(self.button)
        
        self.layout.addWidget(self.lineEdit2)
        self.layout.addWidget(self.button2)

        self.layout.addLayout(self.sublayout)
        self.layout.addWidget(self.button3)
        
        self.setLayout(self.layout)

        

        self.setStyleSheet("""
        background-color: #363333;
        color: #ffffff;
        font-family: Titillium;
        font-size: 18px;
        """)
        self.button.setStyleSheet("""
        background-color: #4E4C08;
        color: #ffffff;
        font-family: Titillium;
        font-size: 18px;
        """)
        self.button2.setStyleSheet("""
        background-color: #4E4C08;
        color: #ffffff;
        font-family: Titillium;
        font-size: 18px;
        """)
        self.button3.setStyleSheet("""
        background-color: #4E4C08;
        color: #ffffff;
        font-family: Titillium;
        font-size: 18px;
        """)

        self.redis_manager = redismodel.PasswordManager(6379, 'localhost', 0)

        self.button.clicked.connect(self.getMasterPassword)
        self.button2.clicked.connect(self.getPassword)
        self.button3.clicked.connect(self.setPassword)
 

    @QtCore.Slot()
    def getMasterPassword(self):
        """
            takes the text value from the first line Edit box, which is the box containing the masterpassword
            upon entering the button, the, the application will establish connection to the redis database with the correct password
        """
        input_text = self.lineEdit1.text()
        self.lineEdit1.setText('')
        self.redis_manager = redismodel.PasswordManager(6379, 'localhost', 0, _password=input_text)
        self.text.setText('Password entered')


    def getPassword(self):
        """
            invokes the getHash method from the redis model, and returns and displays the value in the gui application window
        """
        key_value = self.lineEdit2.text().lower()
        response = self.redis_manager.getHash(key_value)
        self.text.setText(response)
    
    def setPassword(self):
        """
            sets the password in the database in an encrypted format
        """
        key_value = self.lineEdit3.text().lower()
        password = self.lineEdit4.text()

        response = self.redis_manager.setHash(key_value, password)
        self.text.setText(response)