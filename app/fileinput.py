from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QVBoxLayout

class FileInput(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.file_button = QPushButton("Open File")
        self.file_button.clicked.connect(self.open_file)
        layout.addWidget(self.file_button)

        self.setLayout(layout)

    def open_file(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")
        if fileName:
            print(fileName)