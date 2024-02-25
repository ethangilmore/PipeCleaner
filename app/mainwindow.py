from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
import pandas as pd

from .filegrouplist import FileGroupList
from .processingpipeline import ProcessingPipeline
from .dataframetable import DataFrameTable

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("Pipe Cleaner")

        self.file_group_list = FileGroupList()
        layout.addWidget(self.file_group_list)

        self.processing_pipeline = ProcessingPipeline()
        layout.addWidget(self.processing_pipeline)
        self.file_group_list.data_changed.connect(self.processing_pipeline.set_data)

        self.preview_table = DataFrameTable()
        layout.addWidget(self.preview_table)
        self.processing_pipeline.finished_processing.connect(self.preview_table.set_df)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
