import os

from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
import pandas as pd

class FileInput(QWidget):

    files_opened = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.file_button = QPushButton("Select Files")
        self.file_button.clicked.connect(self.open_files)
        layout.addWidget(self.file_button)

        self.setLayout(layout)
        self.df = None

    def read_file(self, filename):
        if filename.endswith(".csv"):
            return pd.read_csv(filename)
        elif filename.endswith(".tsv"):
            return pd.read_csv(filename, sep="\t")
        elif filename.endswith(".xlsx"):
            return pd.read_excel(filename)
        else:
            raise ValueError("File type not supported")

    def open_files(self):
        filenames, _ = QFileDialog.getOpenFileNames(self)

        dfs = []
        for filename in filenames:
            df = self.read_file(filename)
            df['filename'] = os.path.basename(filename)
            dfs.append(df)
        self.df = pd.concat(dfs)

        self.files_opened.emit(filenames)

