from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QLineEdit

from ..processingmodule import ProcessingModule

@ProcessingModule
class ContaminantFilter(QWidget):

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        # Column to filter
        layout.addWidget(QLabel("Column to filter"))
        self.column_dropdown = QComboBox()
        layout.addWidget(self.column_dropdown)
        layout.addSpacing(16)

        # Keywords
        layout.addWidget(QLabel("Keywords"))
        self.keyword_input = QLineEdit()
        layout.addWidget(self.keyword_input)
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
            return df[df[column].str.contains(self.keyword_input.text())]
        else:
            return df