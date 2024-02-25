from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import pyqtSignal
import pandas as pd

from .dataprocessors import ProbabilityFilter, ContaminantFilter, ModificationFilter

class ProcessingPipeline(QWidget):

    finished_processing = pyqtSignal(pd.DataFrame)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.data_processors = [
            ProbabilityFilter(title="Filter by Probability"),
            ContaminantFilter(title="Filter by Contaminant"),
            ModificationFilter(title="Filter by Modification")
        ]

        for data_processor in self.data_processors:
            layout.addWidget(data_processor)
            data_processor.reprocess.connect(self.process)

        self.setLayout(layout)
        self._df = pd.DataFrame()

    def set_data(self, df):
        self._df = df
        self.process()
    
    def process(self):
        df = self._df
        for data_processor in self.data_processors:
            df = data_processor.process(df)
        self.finished_processing.emit(df)
