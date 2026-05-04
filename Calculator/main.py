class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square_root(self, a):
        return a ** 0.5


def run_calculator():
    calc = Calculator()

    operations = {
        "+": calc.add,
        "-": calc.subtract,
        "*": calc.multiply,
        "/": calc.divide,
        "√": calc.square_root
    }

    num1 = float(input("What's the first number?: "))

    while True:
        print("Available operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        if operation_symbol == "√":
            result = operations[operation_symbol](num1)
            print(f"√{num1} = {result}")
        else:
            num2 = float(input("What's the next number?: "))
            result = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue with {result}, or 'n' to exit: ")

        if choice == "y":
            num1 = result
        else:
            break


if __name__ == "__main__":
    run_calculator() 
