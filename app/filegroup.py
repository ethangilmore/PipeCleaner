from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QListWidget, QHBoxLayout
from PyQt6.QtCore import pyqtSignal

from .fileinput import FileInput

class FileGroup(QFrame):

    files_opened = pyqtSignal(list)

    def __init__(self, group_name):
        super().__init__()
        layout = QVBoxLayout()

        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel("Group: "))
        self.title_label = QLabel(group_name)
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        layout.addLayout(header_layout)

        self.file_list = QListWidget()
        layout.addWidget(self.file_list)

        self.file_input = FileInput()
        self.file_input.files_opened.connect(self.update_list)
        self.file_input.files_opened.connect(self.files_opened)
        layout.addWidget(self.file_input)

        layout.addStretch()
        self.setLayout(layout)
        self.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Raised)

    def update_list(self, file_list):
        self.file_list.clear()
        self.file_list.addItems(file_list)
