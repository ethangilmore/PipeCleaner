from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox
    
class ProcessingModule(QFrame):

    def __init__(self, data_processor):
        super().__init__()
        layout = QVBoxLayout()
        header_layout = QHBoxLayout()

        # Active checkbox
        self.active_checkbox = QCheckBox()
        self.active_checkbox.setChecked(True)
        self.active_checkbox.toggled.connect(self.toggle_active)
        header_layout.addWidget(self.active_checkbox)

        # Title
        self.title_label = QLabel()
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        layout.addLayout(header_layout)

        # Child Widget
        self.data_processor = data_processor()
        layout.addWidget(self.data_processor)

        self.setLayout(layout)
        self.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Raised)

    def __call__(self, title):
        self.title_label.setText(title)
        return self

    def toggle_active(self, checked):
        self.data_processor.setEnabled(checked)
        self.title_label.setEnabled(checked)

    def preprocess(self, df):
        return self.data_processor.preprocess(df)
    
    def process(self, df):
        if self.active_checkbox.isChecked():
            return self.data_processor.process(df)
        else:
            return df
