import sys

from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    from app import MainWindow
    window = MainWindow()
    window.show()
    app.exit(app.exec())

if __name__ == "__main__":
    main()