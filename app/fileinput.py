from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
import pandas as pd

class FileInput(QWidget):

    data_changed = pyqtSignal(pd.DataFrame)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.file_button = QPushButton("Open File")
        self.file_button.clicked.connect(self.open_file)
        layout.addWidget(self.file_button)

        self.setLayout(layout)
        self._df = None

    def open_file(self):
        fileName, _ = QFileDialog.getOpenFileName(self)
        if not fileName:
            return
        
        if fileName.endswith(".csv"):
            self._df = pd.read_csv(fileName)
        elif fileName.endswith(".tsv"):
            self._df = pd.read_csv(fileName, sep="\t")
        elif fileName.endswith(".xlsx"):
            self._df = pd.read_excel(fileName)
        else:
            raise ValueError("File type not supported")
        
        self.data_changed.emit(self._df)
    