from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QDoubleSpinBox
from PyQt6.QtCore import pyqtSignal

from ..processingmodule import ProcessingModule

@ProcessingModule
class ProbabilityFilter(QWidget):

    reprocess = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        # Column to filter
        layout.addWidget(QLabel("Column to filter"))
        self.column_dropdown = QComboBox()
        self.column_dropdown.setCurrentIndex(-1)
        self.column_dropdown.currentIndexChanged.connect(self.reprocess)
        self.column_dropdown.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        layout.addWidget(self.column_dropdown)
        layout.addSpacing(16)

        # Threshold
        layout.addWidget(QLabel("Threshold"))
        self.threshold_spinbox = QDoubleSpinBox()
        self.threshold_spinbox.valueChanged.connect(self.reprocess)
        self.threshold_spinbox.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
        self.threshold_spinbox.setMinimum(0)
        self.threshold_spinbox.setMaximum(100)
        self.threshold_spinbox.setValue(95)
        layout.addWidget(self.threshold_spinbox)
        layout.addStretch()

        self.setLayout(layout)
        self.columns = []

    def preprocess(self, df):
        new_columns = list(df.select_dtypes(include='number'))
        if new_columns == self.columns:
            return

        self.columns = new_columns
        selected_column = self.column_dropdown.currentText()
        self.column_dropdown.clear()
        self.column_dropdown.addItems(self.columns)
        if selected_column:
            index = self.column_dropdown.findText(selected_column)
            self.column_dropdown.setCurrentIndex(index)
        else:
            self.column_dropdown.setCurrentIndex(-1)

    def process(self, df):
        if self.column_dropdown.currentIndex() == -1:
            return df

        column = self.column_dropdown.currentText()
        threshold = self.threshold_spinbox.value()

        return df[df[column] >= threshold]