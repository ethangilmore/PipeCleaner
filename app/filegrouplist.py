from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QListWidget
from PyQt6.QtCore import pyqtSignal
import pandas as pd

from .filegroup import FileGroup

class FileGroupList(QWidget):

    data_changed = pyqtSignal(pd.DataFrame)

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.file_groups = []
        for _ in range(3):
            file_group = FileGroup(f"Group {_ + 1}")
            file_group.files_opened.connect(self.files_opened)
            self.file_groups.append(file_group)
            layout.addWidget(file_group)

        self.setLayout(layout)

    def files_opened(self, file_list):
        dfs = []
        for file_group in self.file_groups:
            df = file_group.file_input.df
            if df is None: continue
            df['groupname'] = file_group.title_label.text()
            dfs.append(df)
        self.df = pd.concat(dfs)

        self.data_changed.emit(self.df)

