from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QInputDialog, QMessageBox
from PyQt6.QtCore import pyqtSignal
import pandas as pd

from .filegroup import FileGroup

class FileGroupList(QWidget):

    data_changed = pyqtSignal(pd.DataFrame)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.add_group_button = QPushButton("Add Group")
        self.add_group_button.clicked.connect(self.add_group)
        button_layout.addWidget(self.add_group_button)

        self.remove_group_button = QPushButton("Remove Group")
        self.remove_group_button.clicked.connect(self.remove_group)
        button_layout.addWidget(self.remove_group_button)
        layout.addLayout(button_layout)
        
        self.file_groups = []

        layout.addLayout(QHBoxLayout())
        self.setLayout(layout)

    def add_group(self):
        group_name, ok = QInputDialog.getText(self, "Group Name", "Enter a name for the group")
        if not ok or not group_name:
            return
        if any(group_name == file_group.title_label.text() for file_group in self.file_groups):
            QMessageBox.critical(self, "Error", "Group name already exists")
            return
        

        file_group = FileGroup(group_name)
        file_group.files_opened.connect(self.files_opened)
        self.file_groups.append(file_group)
        self.layout().itemAt(1).addWidget(file_group)

    def remove_group(self):
        if self.file_groups:
            file_group = self.file_groups.pop()
            file_group.deleteLater()

    def files_opened(self, file_list):
        dfs = []
        for file_group in self.file_groups:
            df = file_group.file_input.df
            df['groupname'] = file_group.title_label.text()
            dfs.append(df)
        self.df = pd.concat(dfs)

        self.data_changed.emit(self.df)

