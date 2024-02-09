from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
import pandas as pd

from .dataprocessors import ProbabilityFilter

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("Pipe Cleaner")
        
        self.processing_modules = [
            ProbabilityFilter(title="Filter by Probability")
        ]

        # Dummy data
        df = pd.DataFrame({
            "Sequence": [1, 2, 3],
            "Probability": [4, 5, 6],
            "Assigned Modifications": [7, 8, 9]
        })

        for module in self.processing_modules:
            df = module.preprocess(df)
            layout.addWidget(module)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)