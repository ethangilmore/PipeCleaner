from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QLineEdit
from PyQt6.QtCore import pyqtSignal

from ..processingmodule import ProcessingModule
from ..columndropdown import ColumnDropdown

@ProcessingModule
class ContaminantFilter(QWidget):

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

        # Keywords
        layout.addWidget(QLabel("Keywords"))
        self.keyword_input = QLineEdit()
        self.keyword_input.textChanged.connect(self.reprocess)
        layout.addWidget(self.keyword_input)
        layout.addStretch()

        self.setLayout(layout)
        self.columns = []

    def preprocess(self, df):
        new_columns = list(df.columns)
        self.column_dropdown.set_columns(new_columns)

    def process(self, df):
        column = self.column_dropdown.currentText()
        keywords = list(filter(lambda x: x, self.keyword_input.text().replace(' ', '').split(',')))

        if self.column_dropdown.currentIndex() == -1 or not keywords:
            return df

        return df[~df[column].apply(str).str.contains('|'.join(keywords), case=False)]