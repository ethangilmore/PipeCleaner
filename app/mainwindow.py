from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
import pandas as pd

from .fileinput import FileInput
from .processingpipeline import ProcessingPipeline

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("Pipe Cleaner")

        self.file_input = FileInput()
        layout.addWidget(self.file_input)
        
        self.processing_pipeline = ProcessingPipeline()
        layout.addWidget(self.processing_pipeline)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)