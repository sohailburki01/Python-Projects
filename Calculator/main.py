class Calculator:
    def __init__(self):
        self.current_value = 0

    def add(self, num):
        self.current_value += num
        return self.current_value

    def subtract(self, num):
        self.current_value -= num
        return self.current_value

    def multiply(self, num):
        self.current_value *= num
        return self.current_value

    def divide(self, num):
        if num == 0:
            return "Cannot divide by zero"
        self.current_value /= num
        return self.current_value

    def exponent(self, num):
        self.current_value **= num
        return self.current_value

    def nth_root(self, n):
        self.current_value **= (1 / n)
        return self.current_value

    def start(self):
        self.current_value = float(input("Enter first number: "))

        operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
            "^": self.exponent,
            "√": self.nth_root
        }

        while True:
            print("\nAvailable Operations:")
            for op in operations:
                print(op)

            operation = input("Pick an operation: ")
            num = float(input("Enter next number: "))

            if operation in operations:
                result = operations[operation](num)

                if operation == "√":
                    print(f"{num}√{self.current_value} = {result}")
                else:
                    print(f"Result = {result}")
            else:
                print("Invalid operation!")
                continue

            choice = input(
                "Type 'y' to continue with current result or 'n' to start new calculation: "
            )

            if choice.lower() == 'n':
                self.start()
                break


calc = Calculator()
calc.start()