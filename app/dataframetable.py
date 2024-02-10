from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView

from .dataframetablemodel import DataFrameTableModel

class DataFrameTable(QWidget):
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.table = QTableView()
        layout.addWidget(self.table)

        self.setLayout(layout)
        self._df = None

    def set_df(self, df):
        self._df = df
        self.table.setModel(DataFrameTableModel(self._df))
        