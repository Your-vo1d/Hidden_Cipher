import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from interface import Ui_Hidden_cipher


class HiddenCipherApp(QMainWindow, Ui_Hidden_cipher):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hidden Cipher")
        self.setWindowIcon(QIcon("/img/icon.png"))

        self.path_selection_button.clicked.connect(
            self.path_selection_button_clicked)

    def path_selection_button_clicked(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog

        selected_directory = QFileDialog.getExistingDirectory(
            self, "Select Directory", options=options)

        if selected_directory:
            self.path_lineEdit.setText(selected_directory)


def main():
    app = QApplication(sys.argv)
    window = HiddenCipherApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
