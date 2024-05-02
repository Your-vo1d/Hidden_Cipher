import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from interface import Ui_Hidden_cipher

class HiddenCipherApp(QMainWindow, Ui_Hidden_cipher):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hidden Cipher")
        self.setWindowIcon(QIcon("../../Загрузки/caesar-cipher.png"))
        
        # Добавьте здесь необходимую логику вашего приложения
        
def main():
    app = QApplication(sys.argv)
    window = HiddenCipherApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
