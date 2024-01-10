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
from table import PercentageTableWidget


class Datasplitter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Datasplitter")

        # Label
        self.input_label = QLabel()
        self.input_label.setText("Enter the path sources of the images")
        self.output_label = QLabel()
        self.output_label.setText(
            "Enter the root path for the output of the splitted images"
        )

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Input box
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Enter path..")
        self.output_path_entry = QLineEdit()
        self.output_path_entry.setPlaceholderText("Enter path..")

        # Button
        self.btn = QPushButton("Find", self)
        self.btn.clicked.connect(self.openFileDialog)
        self.output_btn = QPushButton("Find", self)
        self.output_btn.clicked.connect(self.openFileDialog)
        self.split_btn = QPushButton("Split", self)
        self.split_btn.setMaximumWidth(100)

        # Input path widget
        self.line_edit_button_widget = QWidget()
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.lineEdit)
        self.horizontal_layout.addWidget(self.btn)
        self.line_edit_button_widget.setLayout(self.horizontal_layout)

        # Table
        self.percentage_table = PercentageTableWidget()

        # Output path widget
        self.output_path_widget = QWidget()
        horizontal_layout_output = QHBoxLayout()
        horizontal_layout_output.addWidget(self.output_path_entry)
        horizontal_layout_output.addWidget(self.output_btn)
        self.output_path_widget.setLayout(horizontal_layout_output)

        # Center the split button
        self.widget_split_button = QWidget()
        horizontal_layout_split = QHBoxLayout()
        horizontal_layout_split.addWidget(self.split_btn)
        horizontal_layout_split.setContentsMargins(10, 0, 10, 0)
        self.widget_split_button.setLayout(horizontal_layout_split)

        layout.addWidget(self.input_label)
        layout.addWidget(self.line_edit_button_widget)
        layout.addWidget(self.percentage_table)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_path_widget)
        layout.addWidget(self.widget_split_button)
        self.resize(300, 250)

    def openFileDialog(self):
        # Open file dialog and get the selected directory path
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if path:
            # Set the path in the input box
            self.lineEdit.setText(path)


def main():
    app = QApplication(sys.argv)
    ex = Datasplitter()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
