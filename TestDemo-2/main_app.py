import json

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QListWidgetItem, QListView, \
    QStyledItemDelegate, QStyle, QWidget, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QAbstractItemView, \
    QGridLayout, QLabel, QFrame, QVBoxLayout, QItemDelegate, QDialogButtonBox
from PyQt6.QtCore import pyqtSlot, QSize, QStringListModel, QPoint, Qt
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem, QAction


from home_widget import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)