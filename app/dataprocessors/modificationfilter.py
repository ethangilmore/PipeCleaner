import regex

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QCheckBox
from PyQt6.QtCore import pyqtSignal

from ..processingmodule import ProcessingModule
from ..columndropdown import ColumnDropdown

@ProcessingModule
class ModificationFilter(QWidget):

    reprocess = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        modification_layout = QHBoxLayout()

        # column to filter
        input_layout.addWidget(QLabel("column to filter"))
        self.column_dropdown = ColumnDropdown()
        self.column_dropdown.currentIndexChanged.connect(self.reprocess)
        self.column_dropdown.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        input_layout.addWidget(self.column_dropdown)
        input_layout.addSpacing(16)

        # Regex template
        input_layout.addWidget(QLabel("Regex template"))
        self.regex_template_input = QLineEdit()
        self.regex_template_input.textChanged.connect(self.reprocess)
        self.regex_template_input.setText("-?\(\d+\.\d+\)")
        input_layout.addWidget(self.regex_template_input)
        input_layout.addStretch()

        layout.addLayout(input_layout)
        modification_layout.addStretch()
        layout.addLayout(modification_layout)
        self.setLayout(layout)

        self.modifications = set()
        self.modification_checkboxes = []

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

        if modifications == self.modifications:
            return
        self.modifications = modifications

        for checkbox in self.modification_checkboxes:
            checkbox.deleteLater()

        self.modification_checkboxes = []

        for modification in self.modifications:
            checkbox = QCheckBox(str(modification))
            checkbox.stateChanged.connect(self.reprocess)
            self.modification_checkboxes.append(checkbox)
            self.layout().itemAt(1).layout().insertWidget(len(self.modification_checkboxes) - 1, checkbox)

    def process(self, df):
        if self.column_dropdown.currentIndex() == -1:
            return df

        column = self.column_dropdown.currentText()
        template = self.regex_template_input.text()

        if not column or not template:
            return df

        modifications = [checkbox.text() for checkbox in self.modification_checkboxes if checkbox.isChecked()]
        if not modifications:
            return df

        return df[df[column].str.contains('|'.join(modifications), case=False, na=False)]
