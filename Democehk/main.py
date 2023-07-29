from PyQt6 import QtWidgets
from ui_design import Ui_LoginDialog, Ui_HomeDialog

class LoginDialog(QtWidgets.QDialog, Ui_LoginDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.login)

    def login(self):
        # Perform login authentication here
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        # For simplicity, assume successful login for "admin" with password "admin123"
        if username == "admin" and password == "admin123":
            self.switch_to_home_page()

    def switch_to_home_page(self):
        self.home_page = HomeDialog()
        self.home_page.show()
        self.close()  # Automatically close the Login dialog

class HomeDialog(QtWidgets.QDialog, Ui_HomeDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_logout.clicked.connect(self.logout)

    def logout(self):
        self.close()
        self.login_page = LoginDialog()
        self.login_page.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    login_page = LoginDialog()
    login_page.show()

    sys.exit(app.exec())
