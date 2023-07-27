from PyQt6.QtWidgets import QApplication, QDialog
import sys
app= QApplication(sys.argv)

window = QDialog()

window.show()
sys.exit(app.exec())