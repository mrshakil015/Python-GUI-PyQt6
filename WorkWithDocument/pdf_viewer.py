import sys
import io
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pdfminer.high_level import extract_text

class PDFViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Viewer")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.label = QLabel(self)
        self.layout.addWidget(self.label)
        
        self.upload_button = QPushButton("Upload PDF", self)
        self.layout.addWidget(self.upload_button)
        self.upload_button.clicked.connect(self.upload_pdf)
        
    def upload_pdf(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf);;All Files (*)")
        
        if file_name:
            pixmap = QPixmap("path_to_your_pdf_icon.png")  # Replace with the path to an icon/image
            self.label.setPixmap(pixmap)
            self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.label.setScaledContents(True)
            
            # Extract and display PDF content
            text = self.extract_pdf_text(file_name)
            self.display_pdf_content(text)

    def extract_pdf_text(self, pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            text = extract_text(pdf_file)
        return text

    def display_pdf_content(self, content):
        self.label.setText(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFViewerApp()
    window.show()
    sys.exit(app.exec())
