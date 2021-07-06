import sys
import speech_recognition
import pyttsx3
from uiTroLyAo import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication

ai_mouth = pyttsx3.init()
ai_ear = speech_recognition.Recognizer()

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
    
        self.uic.btStart.clicked.connect(lambda: self.pressed_it())
        self.uic.btStop.clicked.connect(lambda: self.main_win.close())

    def pressed_it(self):
        while True:
            with speech_recognition.Microphone() as mic:
                audio = ai_ear.listen(mic)
            try:
                you = ai_ear.recognize_google(audio)
                self.uic.chatHuman.setText(str(you))
            except:
                you = ""
            
            if you == "":
                ai_brain = "I can't hear you, please try again"
            elif "hello" in you:
                ai_brain = "Hello frend"
            elif "doing" in you:
                ai_brain = "I speak with you"
            elif "bye" in you:
                ai_brain = "bye friend"
                self.uic.txtBot.setText(str(ai_brain))
                ai_mouth.say(ai_brain)
                ai_mouth.runAndWait()
                break
            else:
                ai_brain = "oh"

            self.uic.txtBot.setText(str(ai_brain))
            ai_mouth.say(ai_brain)
            ai_mouth.runAndWait()

    def show(self):
        self.main_win.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())