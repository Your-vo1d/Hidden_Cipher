import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from src.interface import Ui_Hidden_cipher
from src.event_handlers import EventHandlers


class HiddenCipherApp(QMainWindow, Ui_Hidden_cipher):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hidden Cipher")
        self.setWindowIcon(QIcon("/img/icon.png"))

        # Создаем экземпляр класса для обработчиков событий
        self.event_handlers = EventHandlers(self)

        # Подключаем обработчики событий к соответствующим кнопкам
        self.path_selection_button.clicked.connect(
            self.event_handlers.path_selection_button_clicked)
        self.select_encode_file_button.clicked.connect(
            self.event_handlers.encode_file_clicked)
        self.about_button.clicked.connect(
            self.event_handlers.about_button_clicked)
        self.select_decode_file_button.clicked.connect(
            self.event_handlers.decode_file_clicked)
        

def main():
    app = QApplication(sys.argv)
    window = HiddenCipherApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
