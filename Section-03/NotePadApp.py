from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt6.QtPrintSupport import QPrinter
import sys
from NotePad import Ui_MainWindow

class NotePadWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

    #---------------Signal Connection Section-----------------
        self.actionSave.triggered.connect(self.save_file)
        self.actionNew.triggered.connect(self.file_new)
        self.actionOpen.triggered.connect(self.open_file)
      

    #------------Maybe Save Function----------------
    def maybe_save(self):
        if not self.textEdit.document().isModified():
            return True
        
        ret = QMessageBox.warning(self, "Application", 
                                    "The document has been modified.\n Do you want to save your changes?", 
                                    QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
        if ret ==QMessageBox.StandardButton.Save:
            return self.save_file()
        
        if ret == QMessageBox.StandardButton.Cancel:
            return self.show()
        return True

    #---------------File Save Function---------------------
    def save_file(self):
        filename = QFileDialog.getSaveFileName(self,"Save File")
        if filename[0]:
            f =open(filename[0], 'w')
            with f:
                text = self.textEdit.toPlainText()
                f.write(text)
                QMessageBox.about(self, "Save FIle", "File have been saved")

    #------------------New File Function------------------------------
    def file_new(self):
        if self.maybe_save():
            self.textEdit.clear()
            
    #------------------Open File Function-----------------------
    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", '/home')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    #-----------------Print Function--------------------
    # from PyQt6.QtPrintSupport import QPrinter --> inded libraries
    

app = QApplication(sys.argv)
Note = NotePadWindow()
sys.exit(app.exec())
