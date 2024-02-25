from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QDoubleSpinBox
from PyQt6.QtCore import pyqtSignal

from ..processingmodule import ProcessingModule
from ..columndropdown import ColumnDropdown

@ProcessingModule
class ProbabilityFilter(QWidget):

    reprocess = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        # Column to filter
        layout.addWidget(QLabel("Column to filter"))
        self.column_dropdown = ColumnDropdown()
        self.column_dropdown.currentIndexChanged.connect(self.reprocess)
        layout.addWidget(self.column_dropdown)
        layout.addSpacing(16)

        # Threshold
        layout.addWidget(QLabel("Threshold"))
        self.threshold_spinbox = QDoubleSpinBox()
        self.threshold_spinbox.valueChanged.connect(self.reprocess)
        self.threshold_spinbox.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
        self.threshold_spinbox.setMinimum(0)
        self.threshold_spinbox.setMaximum(100)
        self.threshold_spinbox.setDecimals(4)
        self.threshold_spinbox.setValue(.95)
        layout.addWidget(self.threshold_spinbox)
        layout.addStretch()

        self.setLayout(layout)
        self.columns = []

    def preprocess(self, df):
        new_columns = df.select_dtypes(include='number')
        self.column_dropdown.set_columns(new_columns)

    def process(self, df):
        if self.column_dropdown.currentIndex() == -1:
            return df

        column = self.column_dropdown.currentText()
        threshold = self.threshold_spinbox.value()

        return df[df[column] >= threshold]
