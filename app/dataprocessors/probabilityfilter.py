from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QDoubleSpinBox

from ..processingmodule import ProcessingModule

@ProcessingModule
class ProbabilityFilter(QWidget):

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        # Column to filter
        layout.addWidget(QLabel("Column to filter"))
        self.column_dropdown = QComboBox()
        self.column_dropdown.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        layout.addWidget(self.column_dropdown)
        layout.addSpacing(16)

        # Threshold
        layout.addWidget(QLabel("Threshold"))
        self.threshold_spinbox = QDoubleSpinBox()
        self.threshold_spinbox.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
        self.threshold_spinbox.setMinimum(0)
        self.threshold_spinbox.setMaximum(100)
        self.threshold_spinbox.setValue(95)
        layout.addWidget(self.threshold_spinbox)
        layout.addStretch()

        self.setLayout(layout)

    def preprocess(self, df):
        self.column_dropdown.clear()
        self.column_dropdown.addItems(df.columns.tolist())

        return df

    def process(self, df):
        column = self.column_dropdown.currentText()
        threshold = self.threshold_spinbox.value()

        if column:
            return df[df[column] >= threshold]
        else:
            return df