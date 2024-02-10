from PyQt6.QtWidgets import QComboBox

class ColumnDropdown(QComboBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.setCurrentIndex(-1)
        self._columns = []

    def set_columns(self, columns):
        new_columns = list(columns)
        if new_columns == self._columns:
            return
        self._columns = new_columns

        self.selected_column = self.currentText()
        self.clear()
        self.addItems(self._columns)
        self.setCurrentIndex(-1)
        if self.selected_column:
            index = self.findText(self.selected_column)
            self.setCurrentIndex(index)
        else:
            self.setCurrentIndex(-1)
