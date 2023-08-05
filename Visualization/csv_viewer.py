import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog, QWidget, QInputDialog
import pandas as pd
import matplotlib.pyplot as plt

class CSVViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CSV Viewer')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.load_btn = QPushButton('Load CSV')
        self.load_btn.clicked.connect(self.load_csv)
        layout.addWidget(self.load_btn)

        self.plot_btn = QPushButton('Plot Data')
        self.plot_btn.clicked.connect(self.show_plot_dialog)
        layout.addWidget(self.plot_btn)

        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    def load_csv(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)")
        if file_name:
            self.df = pd.read_csv(file_name)

    def plot_data(self, columns):
        if hasattr(self, 'df'):
            self.df[columns].plot(kind='bar')
            plt.title(f'CSV Data Visualization')
            plt.xlabel('X-axis Label')
            plt.ylabel('Y-axis Label')
            plt.legend(columns)
            plt.show()

    def show_plot_dialog(self):
        if hasattr(self, 'df'):
            columns, ok = QInputDialog.getText(self, "Column Selection", "Enter the column names or indices (comma-separated) to plot:")
            if ok:
                try:
                    column_indices = [int(idx) for idx in columns.split(",")]
                except ValueError:
                    column_indices = columns.split(",")

                selected_columns = []
                for idx in column_indices:
                    if isinstance(idx, int):
                        selected_columns.append(self.df.columns[idx])
                    else:
                        selected_columns.append(idx.strip())

                valid_columns = [col for col in selected_columns if col in self.df.columns]

                if valid_columns:
                    self.plot_data(valid_columns)
                else:
                    print("Invalid column names or indices.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CSVViewerApp()
    window.show()
    sys.exit(app.exec())
