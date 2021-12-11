import sys
from InvestmentCalculator import Ui_MainWindow as InvCalc_Window
from PyQt5.QtWidgets import QMainWindow, QApplication


class Main(QMainWindow, InvCalc_Window):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


















if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())
