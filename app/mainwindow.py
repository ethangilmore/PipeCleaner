from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
import pandas as pd

from .fileinput import FileInput
from .processingpipeline import ProcessingPipeline
from .dataframetable import DataFrameTable

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("Pipe Cleaner")

        self.file_input = FileInput()
        layout.addWidget(self.file_input)
        
        self.processing_pipeline = ProcessingPipeline()
        layout.addWidget(self.processing_pipeline)
        self.file_input.data_changed.connect(self.processing_pipeline.set_df)

        self.preview_table = DataFrameTable()
        layout.addWidget(self.preview_table)
        self.processing_pipeline.finished_processing.connect(self.preview_table.set_df)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)