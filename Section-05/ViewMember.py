# Form implementation generated from reading ui file 'c:\Users\MD. SHAMIM\Documents\GitHub\Python-GUI-PyQt6\Section-05\ViewMember.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt6.QtWidgets import QTableWidgetItem


class ViewMember_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"background-color:  #E5E4E2\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton_viewmember = QtWidgets.QPushButton(parent=Dialog)

        #connect signal
        self.pushButton_viewmember.clicked.connect(self.view_member)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_viewmember.setFont(font)
        self.pushButton_viewmember.setStyleSheet("QPushButton {\n"
"background-color: #00766d;\n"
"color: white\n"
"}")
        self.pushButton_viewmember.setObjectName("pushButton_viewmember")
        self.verticalLayout.addWidget(self.pushButton_viewmember)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def view_member(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user="root",
                password="",
                database="library_managemenet"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM addmember_table")
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Members"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Mobile"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Email"))
        self.pushButton_viewmember.setText(_translate("Dialog", "View Members"))
