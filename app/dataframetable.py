from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QPushButton, QFileDialog
import pandas as pd

from .dataframetablemodel import DataFrameTableModel

class DataFrameTable(QWidget):
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.table = QTableView()
        layout.addWidget(self.table)

        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(self.export)
        layout.addWidget(self.export_button)

        self.setLayout(layout)
        self._df = pd.DataFrame()

    def set_df(self, df):
        self._df = df
        self.table.setModel(DataFrameTableModel(self._df))
        
    def export(self):
        if self._df is not None:
            file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv);;TSV Files (*.tsv);;Excel Files (*.xlsx)")
            if file_name:
                if file_name.endswith(".csv"):
                    self._df.to_csv(file_name, index=False)
                elif file_name.endswith(".tsv"):
                    self._df.to_csv(file_name, sep="\t", index=False)
                elif file_name.endswith(".xlsx"):
                    self._df.to_excel(file_name, index=False)
