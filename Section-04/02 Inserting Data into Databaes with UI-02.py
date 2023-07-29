from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
import re


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_username = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout.addWidget(self.lineEdit_username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_password = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_password.setMaxLength(8)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_insert = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_insert.setFont(font)
        self.pushButton_insert.setObjectName("pushButton_insert")

        self.pushButton_insert.clicked.connect(self.insert_data)
        self.verticalLayout.addWidget(self.pushButton_insert)
        self.label_result = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def insert_data(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="pyqtdb"
            )

            mycursor = mydb.cursor()
            username = self.lineEdit_username.text()
            password = self.lineEdit_password.text()
            
            
            # Password length requirements: Minimum 6 characters, Maximum 6 characters
            if len(password) != 8:
                self.label_result.setText("Password length must be 8 characters.")
                self.label_result.setStyleSheet("color: red")
                return

            # Password strength requirements: At least 1 digit, 1 uppercase letter, and 1 special character
            if not (re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search(r"[!@#$%^&*()_+{}|:<>?~-]", password)):
                self.label_result.setText("Weak password!")
                self.label_result.setStyleSheet("color: red")
                return

            query = "INSERT INTO pyqtusers (username, password) VALUES (%s, %s)"
            value = (username, password)

            mycursor.execute(query, value)
            mydb.commit()

            self.label_result.setText("Data Inserted")
            self.label_result.setStyleSheet("color: green")

        except mc.Error as e:
            self.label_result.setText("Error Inserting Data.")
            self.label_result.setStyleSheet("color: red")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Inserting Data to MySQL Database"))
        self.label.setText(_translate("Form", "Username:"))
        self.label_2.setText(_translate("Form", "Password: "))
        self.pushButton_insert.setText(_translate("Form", "Insert Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
