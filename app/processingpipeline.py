from PyQt6.QtWidgets import QWidget, QVBoxLayout

from .dataprocessors import ProbabilityFilter, ContaminantFilter

class ProcessingPipeline(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.data_processors = [
            ProbabilityFilter(title="Filter by Probability"),
            ContaminantFilter(title="Filter by Contaminant")
        ]

        for data_processor in self.data_processors:
            layout.addWidget(data_processor)
        layout.addStretch()

        self.setLayout(layout)

    def preprocess(self, df):
        for data_processor in self.data_processors:
            df = data_processor.preprocess(df)
        return df
    
    def process(self, df):
        for data_processor in self.data_processors:
            df = data_processor.process(df)
        return df
