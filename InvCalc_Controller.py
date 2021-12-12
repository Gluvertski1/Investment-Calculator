import sys
from InvestmentCalculator import Ui_MainWindow as InvCalc_Window
from PyQt5.QtWidgets import QMainWindow, QApplication


class Main(QMainWindow, InvCalc_Window):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.calculate_Button.clicked.connect(self.calculate)
        self.additional_Box.setPlainText("0")

    def calculate(self):
        # A = P(1+(r/n)^nt
        # A - final amount
        # P - Principle
        # r - interest rate
        # n - number of times interest applied per time period
        # t - numebr of time periods elapsed

        principle = int(self.initial_Box.toPlainText())

        interest_rate = float(self.rate_Box.toPlainText())/100
        t = int(self.years_Box.toPlainText())
        n = self.comboBox.currentText()

        additional = int(self.additional_Box.toPlainText())

        if n == "Annually":
            num_n = 1
        elif n == "Semi-Annually":
            num_n = 2
        elif n == "Quarterly":
            num_n = 4
        elif n == "Montly":
            num_n = 12
        elif n == "Semi-Monthly":
            num_n = 12*2
        elif n == "Biweekly":
            num_n = 52*2
        elif n == "Weekly":
            num_n = 52
        else:
            num_n = 365

        N_T = num_n*t
        A = principle*(1+(interest_rate/num_n))**N_T

        if A > principle:
            interest = A - principle - additional
        else:
            interest = principle - A - additional

        self.balance_Label.setText(str("{:.2f}".format(A)))
        self.start_Amount_Label.setText(self.initial_Box.toPlainText())
        self.contributions_Label.setText(self.additional_Box.toPlainText())
        self.Interest_Label.setText(str("{:.2f}".format(interest)))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())
