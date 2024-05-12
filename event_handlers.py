from PyQt5.QtWidgets import QFileDialog


class EventHandlers:
    def __init__(self, main_window):
        self.main_window = main_window

    def encode_file_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self.main_window, "Select File", "", "Text file (*.txt)", options=options)
        if fileName:
            self.main_window.path_encode_file.setText(fileName)

    def decode_file_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self.main_window, "Select File", "", "Text file (*.txt)", options=options)
        if fileName:
            self.main_window.path_decode_file.setText(fileName)

    def about_button_clicked(self):
        pass

    def path_selection_button_clicked(self):
        options = QFileDialog.Options()

        selected_directory = QFileDialog.getExistingDirectory(
            self.main_window, "Select Directory", options=options)

        if selected_directory:
            self.main_window.path_lineEdit.setText(selected_directory)
