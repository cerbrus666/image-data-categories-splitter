import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QHBoxLayout,
    QLabel,
)


class FileDialogWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Datasplitter")

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Input box
        self.lineEdit = QLineEdit(self)
        self.lineEdit.placeholderText("Enter path..")
        # layout.addWidget(self.lineEdit)

        # Button
        self.btn = QPushButton("Find", self)
        self.btn.clicked.connect(self.openFileDialog)
        # layout.addWidget(self.btn)

        # lineEditButtton widget
        self.line_edit_button_widget = QWidget()
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.lineEdit)
        self.horizontal_layout.addWidget(self.btn)
        self.line_edit_button_widget.setLayout(self.horizontal_layout)

        layout.addWidget(self.line_edit_button_widget)

        self.resize(400, 100)

    def openFileDialog(self):
        # Open file dialog and get the selected directory path
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if path:
            # Set the path in the input box
            self.lineEdit.setText(path)


def main():
    app = QApplication(sys.argv)
    ex = FileDialogWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
