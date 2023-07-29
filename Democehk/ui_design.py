from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(300, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_username = QtWidgets.QLineEdit(LoginDialog)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(LoginDialog)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.pushButton_login = QtWidgets.QPushButton(LoginDialog)
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout.addWidget(self.pushButton_login)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.label.setText(_translate("LoginDialog", "Login"))
        self.pushButton_login.setText(_translate("LoginDialog", "Login"))


class Ui_HomeDialog(object):
    def setupUi(self, HomeDialog):
        HomeDialog.setObjectName("HomeDialog")
        HomeDialog.resize(300, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(HomeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(HomeDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton_logout = QtWidgets.QPushButton(HomeDialog)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.verticalLayout.addWidget(self.pushButton_logout)

        self.retranslateUi(HomeDialog)
        QtCore.QMetaObject.connectSlotsByName(HomeDialog)

    def retranslateUi(self, HomeDialog):
        _translate = QtCore.QCoreApplication.translate
        HomeDialog.setWindowTitle(_translate("HomeDialog", "Home"))
        self.label.setText(_translate("HomeDialog", "Welcome to Home"))
        self.pushButton_logout.setText(_translate("HomeDialog", "Logout"))
