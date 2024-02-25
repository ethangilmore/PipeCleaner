from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from PyQt6.QtCore import pyqtSignal

from .fileinput import FileInput

class FileGroup(QWidget):

    files_opened = pyqtSignal(list)

    def __init__(self, group_name):
        super().__init__()
        layout = QVBoxLayout()

        self.title_label = QLabel(group_name)
        layout.addWidget(self.title_label)

        self.file_list = QListWidget()
        layout.addWidget(self.file_list)

        self.file_input = FileInput()
        self.file_input.files_opened.connect(self.update_list)
        self.file_input.files_opened.connect(self.files_opened)
        layout.addWidget(self.file_input)

        self.setLayout(layout)

    def update_list(self, file_list):
        self.file_list.clear()
        self.file_list.addItems(file_list)
