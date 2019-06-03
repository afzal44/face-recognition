# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import mysql.connector
from PyQt5.QtWidgets import QTableWidget


class Ui_Form(object):
    tableWidget: QTableWidget

    def __init__(self):
        object.__init__(self)
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName("localhost")
        self.db.setDatabaseName("attendencesystemusingfacerecogniztion")
        self.db.setUserName("root")
        self.db.setPassword("smalik123")

    def loadData(self):
        status = self.db.open()
        if status == False:
            QtWidgets.QMessageBox.warning(self, "Error", self.db.lastError().text(), QtWidgets.QMessageBox.Discard)
        else:
            self.tableWidget.setColumnCount(4)
            #self.tableWidget.setHorizontalHeaderLabels(['id', 'name', 'surname', 'surname'])
            row = 0
            sql = "SELECT * FROM attendencesheet"
            query = QtSql.QSqlQuery(sql)
            while query.next():
                self.tableWidget.insertRow(row)
                id = QtWidgets.QTableWidgetItem(str(query.value(0)))
                nm = QtWidgets.QTableWidgetItem(str(query.value(1)))
                dtee = QtWidgets.QTableWidgetItem(str(query.value(2)))
                stats = QtWidgets.QTableWidgetItem(str(query.value(3)))

                self.tableWidget.setItem(row, 0, id)
                self.tableWidget.setItem(row, 1, nm)
                self.tableWidget.setItem(row, 2, dtee)
                self.tableWidget.setItem(row, 3, stats)
                row = row + 1
        # self.db.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 120, 501, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 340, 501, 101))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadData)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 541, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "STUDENT ROLL"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form","STATUS"))
        self.pushButton.setText(_translate("Form", "Attendance Details"))
        self.label.setText(_translate("Form", "Student Automatic Attendance System"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

