from registr import regist
from recognize import recogn
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QInputDialog, QLineEdit, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
import sys
from viewrecord1 import Ui_Form
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data =[]
        self.fc =[]
        self.title = "Register student window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        label = QLabel("<h1>SIR CHHOTU RAM INSTITUTE OF ENGINEERING & TECHNOLOGY</h1><h1>Welcome to Face Recognition Attendence System</h1><br> <b>Choose an option :<b>")
        label.setAlignment(Qt.AlignTop)
        self.setCentralWidget(label)
        button1 = QPushButton("Register",self)
        button1.move(100,230)
        button1.clicked.connect(self.on_click)
        button =QPushButton("View",self)
        button.move(300,230)
        button.clicked.connect(self.openWindow)
        button2 = QPushButton("Attendence",self)
        button2.move(500,230)
        button2.clicked.connect(self.attendence)
        self.InitWindow()

    def InitWindow(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        exitButton = QAction("Exit",self)
        exitButton.setShortcut("Ctrl+E")
        exitButton.setStatusTip("Exit Application")
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.statusBar().showMessage("Created By :- Afjal Ahamad and Aamir Ali (S.C.R.I.E.T)")

        self.show()
    def on_click(self):
        roll, okPressed = QInputDialog.getInt(self, "Enter Roll Number","Your Rollno:", 28, 0, 100, 1)
        if okPressed:
            name, okPressed1 = QInputDialog.getText(self, "Enter your Name","Your Name:", QLineEdit.Normal, "")
            if okPressed1:
                regist.record_face(self,roll)
            else:
                return 0
        else:
            return 0
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def attendence(self):
        recogn.recog(self)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

