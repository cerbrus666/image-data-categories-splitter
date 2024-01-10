import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
)


class PercentageTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Percentage Splitter")

        # Create Table
        self.table = QTableWidget(self)
        self.table.setRowCount(3)
        self.table.setColumnCount(2)

        # Set Headers
        self.table.setHorizontalHeaderLabels(["Category", "Percentage"])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Set Row Names and default percentages
        categories = ["Train", "Validation", "Test"]
        default_values = ["70", "20", "10"]  # Default percentage values
        for i, category in enumerate(categories):
            self.table.setItem(i, 0, QTableWidgetItem(category))
            self.table.setItem(i, 1, QTableWidgetItem(default_values[i]))

        # Connect cell changed signal
        # TODO
        # Need to change to auto calculation
        self.table.cellChanged.connect(self.validate_percentages)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.resizeRowsToContents()

    def resizeRowsToContents(self):
        self.table.resizeRowsToContents()
        total_height = (
            self.table.horizontalHeader().height() + 2
        )  # Include header height and a small margin
        for i in range(self.table.rowCount()):
            total_height += self.table.rowHeight(i)
        self.table.setFixedHeight(total_height)

    def validate_percentages(self):
        total_percentage = 0
        for row in range(self.table.rowCount()):
            try:
                percentage = float(self.table.item(row, 1).text())
                total_percentage += percentage
            except ValueError:
                # Handle non-numeric input
                continue

        # Check if the total is 100%
        if total_percentage != 100:
            QMessageBox.warning(
                self, "Invalid Input", "The total percentage must sum up to 100%."
            )
