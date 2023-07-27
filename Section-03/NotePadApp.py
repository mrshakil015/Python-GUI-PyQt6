from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QFontDialog, QColorDialog
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
import sys
from PyQt6.QtCore import QFileInfo, Qt
from PyQt6.QtGui import QFont, QTextCharFormat
from NotePad import Ui_MainWindow


class NotePadWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

    #---------------Signal Connection Section-----------------
        #--File Menu--
        self.actionSave.triggered.connect(self.save_file)
        self.actionNew.triggered.connect(self.file_new)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPrint_Preview.triggered.connect(self.preview_dialog)
        self.actionExport_PDF.triggered.connect(self.export_pdf)
        self.actionQuit.triggered.connect(self.exit_app)

        #--Edit Menu--
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionPaste.triggered.connect(self.textEdit.paste)

        #--Format Menu--
        self.actionBold.triggered.connect(self.text_bold)
        self.actionItalic.triggered.connect(self.text_italic)
        self.actionUnderline.triggered.connect(self.text_underline)

        self.actionAlign_Left.triggered.connect(self.align_left)
        self.actionAlign_Right.triggered.connect(self.align_right)
        self.actionCenter.triggered.connect(self.align_center)
        self.actionAlign_Justify.triggered.connect(self.align_justify)

        self.actionFont.triggered.connect(self.font_dialog)
        self.actionColor.triggered.connect(self.color_dialog)
        self.actionAbout_App.triggered.connect(self.about)

      

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
    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

    #--------------Print Preview Function---------------------
    # from PyQt6.QtPrintSupport import QPrintPreviewDialog --> loaded libraries
    def preview_dialog(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec()

    def print_preview(self, printer):
        self.textEdit.print(printer)

    #----------------Export PDF Section-------------------
    # from PyQt6.QtCore import QFileInfo --> loaded libraries
    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', "PDF files (.pdf)")
        if fn != "":
            if QFileInfo(fn).suffix() == "" :fn += '.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer)

    #--------------Quit Section---------------------------
    def exit_app(self):
        self.close()
        
    #--------------Bold Section---------------------------
    def text_bold(self):
        current_format_bold = self.textEdit.currentCharFormat()
        new_format_bold = QTextCharFormat()

        # Toggle bold property
        new_format_bold.setFontWeight(QFont.Weight.Bold if current_format_bold.fontWeight() == QFont.Weight.Normal else QFont.Weight.Normal)

        # Preserve the existing underline and italic properties
        new_format_bold.setFontItalic(current_format_bold.fontItalic())
        new_format_bold.setFontUnderline(current_format_bold.fontUnderline())

        # Apply the modified format to the selected text
        cursor = self.textEdit.textCursor()
        cursor.mergeCharFormat(new_format_bold)
        self.textEdit.setCurrentCharFormat(new_format_bold)

    #--------------Italic Section---------------------------
    def text_italic(self):
        current_format_italic = self.textEdit.currentCharFormat()
        new_format_italic = QTextCharFormat()

        # Toggle italic property
        new_format_italic.setFontItalic(not current_format_italic.fontItalic())

        # Preserve the existing underline and bold properties
        new_format_italic.setFontWeight(current_format_italic.fontWeight())
        new_format_italic.setFontUnderline(current_format_italic.fontUnderline())

        # Apply the modified format to the selected text
        cursor = self.textEdit.textCursor()
        cursor.mergeCharFormat(new_format_italic)
        self.textEdit.setCurrentCharFormat(new_format_italic)

    #--------------Underline Section---------------------------
    def text_underline(self):
        current_format_underline = self.textEdit.currentCharFormat()
        new_format_underline = QTextCharFormat()

        # Toggle underline property
        new_format_underline.setFontUnderline(not current_format_underline.fontUnderline())

        # Preserve the existing Italic and bold properties
        new_format_underline.setFontWeight(current_format_underline.fontWeight())
        new_format_underline.setFontItalic(current_format_underline.fontItalic())


        # Apply the modified format to the selected text
        cursor = self.textEdit.textCursor()
        cursor.mergeCharFormat(new_format_underline)
        self.textEdit.setCurrentCharFormat(new_format_underline)

    #------------Alignment Section-----------------
    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def align_justify(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    #----------Font Section------------
    def font_dialog(self):
        font, ok = QFontDialog.getFont()
        
        if ok:
            cursor = self.textEdit.textCursor()

            # Preserve the existing formatting of the selected text
            current_format = cursor.charFormat()

            # Set the new font style
            current_format.setFont(font)

            # Apply the modified format to the selected text
            cursor.mergeCharFormat(current_format)
    
    #-----------Color Section--------------
    def color_dialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    #--------About Section---------------
    def about(self):
        QMessageBox.about(self, "About App", "This is simple notepad app with PyQt6")
    
    

app = QApplication(sys.argv)
Note = NotePadWindow()
sys.exit(app.exec())
