import sys
from typing import Text
from PyQt5.QtWidgets import QApplication, QMainWindow
from caculator import Ui_MainWindow

class MainWindow:
    def __init__(self):
        #khai báo các biến
        #biến màn hình chính
        self.main_win = QMainWindow()
        #biến gui
        self.uic = Ui_MainWindow()
        #hàm gui
        self.uic.setupUi(self.main_win)
    
        self.uic.BT0.clicked.connect(lambda: self.pressed_it("0"))
        self.uic.BT1.clicked.connect(lambda: self.pressed_it("1"))
        self.uic.BT2.clicked.connect(lambda: self.pressed_it("2"))
        self.uic.BT3.clicked.connect(lambda: self.pressed_it("3"))
        self.uic.BT4.clicked.connect(lambda: self.pressed_it("4"))
        self.uic.BT5.clicked.connect(lambda: self.pressed_it("5"))
        self.uic.BT6.clicked.connect(lambda: self.pressed_it("6"))
        self.uic.BT7.clicked.connect(lambda: self.pressed_it("7"))
        self.uic.BT8.clicked.connect(lambda: self.pressed_it("8"))
        self.uic.BT9.clicked.connect(lambda: self.pressed_it("9"))

        self.uic.BTXoaTungSo.clicked.connect(lambda: self.pressed_Arrow())
        self.uic.BTXoaHet.clicked.connect(lambda: self.pressed_it("C"))

        self.uic.BTCong.clicked.connect(lambda: self.pressed_it("+"))
        self.uic.BTTru.clicked.connect(lambda: self.pressed_it("-"))
        self.uic.BTNhan.clicked.connect(lambda: self.pressed_it("*"))
        self.uic.BTChia.clicked.connect(lambda: self.pressed_it("/"))

        self.uic.BTThapPhan.clicked.connect(lambda: self.pressed_it("."))
        self.uic.BTAm.clicked.connect(lambda: self.pressed_am_duong())

        self.uic.BTBang.clicked.connect(lambda: self.pressed_kq())

# xử lý âm và dương
    def pressed_am_duong(self):
        screen_1 = self.uic.screen.text()
        if "-" in screen_1:
            self.uic.screen.setText(screen_1.replace("-", ""))
        else:
            self.uic.screen.setText(f'-{screen_1}')

# xóa từng thành phần trong máy 
    def pressed_Arrow(self):
        screen_1 = self.uic.screen.text()
        screen_1 = screen_1[:-1]
        self.uic.screen.setText(screen_1)

    def pressed_it(self, pressed):
# nếu ấn C thì sẽ xóa hết
        if pressed == "C":
            self.uic.screen.setText("0")
# nếu text trên màn hình bằng 0 thì nó sẽ gán cho nó trống
        else:
            if self.uic.screen.text() == "0": 
                self.uic.screen.setText("")
            self.uic.screen.setText(f'{self.uic.screen.text()}{pressed}')

# kết quả (xử lý tính toán)
    def pressed_kq(self):
        screen_1 = self.uic.screen.text()
        try:
            result = eval(screen_1)
            self.uic.screen.setText(str(result))
        except:
            self.uic.screen.setText("ERROR")
    def show(self):
        self.main_win.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())