from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSizePolicy
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
        self.file_group_list.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        layout.addWidget(self.file_group_list)
        layout.setStretchFactor(self.file_group_list, 0)

        self.processing_pipeline = ProcessingPipeline()
        self.file_group_list.data_changed.connect(self.processing_pipeline.set_data)
        layout.addWidget(self.processing_pipeline)
        layout.setStretchFactor(self.processing_pipeline, 0)

        self.preview_table = DataFrameTable()
        self.preview_table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.processing_pipeline.finished_processing.connect(self.preview_table.set_df)
        layout.addWidget(self.preview_table)
        layout.setStretchFactor(self.preview_table, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
