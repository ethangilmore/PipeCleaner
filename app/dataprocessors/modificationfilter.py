import regex

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit
from PyQt6.QtCore import pyqtSignal

from ..processingmodule import ProcessingModule
from ..columndropdown import ColumnDropdown

@ProcessingModule
class ModificationFilter(QWidget):

    reprocess = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        # Column to filter
        layout.addWidget(QLabel("Column to filter"))
        self.column_dropdown = ColumnDropdown()
        self.column_dropdown.currentIndexChanged.connect(self.reprocess)
        self.column_dropdown.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        layout.addWidget(self.column_dropdown)
        layout.addSpacing(16)

        # Regex template
        layout.addWidget(QLabel("Regex template"))
        self.regex_template_input = QLineEdit()
        self.regex_template_input.textChanged.connect(self.reprocess)
        self.regex_template_input.setText("-?\(\d+\.\d+\)")
        layout.addWidget(self.regex_template_input)
        layout.addStretch()

        self.setLayout(layout)

    def preprocess(self, df):
        new_columns = list(df.columns)
        self.column_dropdown.set_columns(new_columns)

        column = self.column_dropdown.currentText()
        template = self.regex_template_input.text()

        if not column or not template:
            return

        modifications = set()
        for value in df[column]:
            if value:
                modifications.update(regex.findall(template, str(value)))

        print(modifications)
        


    def process(self, df):
        return df
