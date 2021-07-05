import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from mainui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.stackedWidget.setCurrentWidget(self.uic.screen)

        self.uic.BTScreen1.clicked.connect(self.showScreen_1)
        self.uic.BTScreen2.clicked.connect(self.showScreen_2)
        self.uic.BTScreen3.clicked.connect(self.showScreen_3)
        self.uic.BTHome.clicked.connect(self.showHome)

    def show(self):
        self.main_win.show()

    def showScreen_1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.screen1)

    def showScreen_2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.screen2)

    def showScreen_3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.screen3)  

    def showHome(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.screen)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
