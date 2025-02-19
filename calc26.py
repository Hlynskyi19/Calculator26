import sys
import doctest
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)


# Арифметичні функції з doctest
def add(a: float, b: float) -> float:
    """
    Returns the sum of a and b.

    >>> add(3, 2)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Returns the result of subtracting b from a.

    >>> subtract(5, 3)
    2
    >>> subtract(10, 20)
    -10
    >>> subtract(7, 0)
    7
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Returns the product of a and b.

    >>> multiply(4, 2)
    8
    >>> multiply(-1, 5)
    -5
    >>> multiply(0, 10)
    0
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Returns the result of dividing a by b.

    >>> divide(6, 2)
    3.0
    >>> divide(9, 3)
    3.0
    >>> divide(5, 2)
    2.5
    >>> divide(1, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


# Графічний інтерфейс калькулятора на PyQt5
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.result_label = QLabel("Результат: ")
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()

        self.add_button = QPushButton("Додати")
        self.sub_button = QPushButton("Відняти")
        self.mul_button = QPushButton("Помножити")
        self.div_button = QPushButton("Поділити")

        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.add_button)
        layout.addWidget(self.sub_button)
        layout.addWidget(self.mul_button)
        layout.addWidget(self.div_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.add_button.clicked.connect(lambda: self.calculate(add))
        self.sub_button.clicked.connect(lambda: self.calculate(subtract))
        self.mul_button.clicked.connect(lambda: self.calculate(multiply))
        self.div_button.clicked.connect(lambda: self.calculate(divide))

    def calculate(self, operation):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = operation(num1, num2)
            self.result_label.setText(f"Результат: {result}")
        except ValueError:
            self.result_label.setText("Помилка: введіть числа!")
        except ZeroDivisionError:
            self.result_label.setText("Помилка: ділення на 0!")


# Запуск програми та тестів
if __name__ == "__main__":
    doctest.testmod()  # Запуск doctest-тестів

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
