import sys
import os
import json
from PyQt6.QtWidgets import QApplication
from main_app import MainWindow

if __name__ == '__main__':

    flag = os.path.exists("datas/data.json")

    if not flag:
        os.mkdir("datas")
        with open("datas/data.json", "w") as f:
            f.write(json.dumps([]))

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())