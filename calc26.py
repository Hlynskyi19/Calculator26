import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QGridLayout,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()
        self.display = QLineEdit(self)
        self.layout.addWidget(self.display)

        grid_layout = QGridLayout()
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
        ]

        for text, row, col in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col)

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Помилка")
        else:
            self.display.setText(self.display.text() + text)


def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
