# calculator_oop.py
class Calculator:
    def _init_(self, value: float = 0.0):
        self.value = float(value)

    def add(self, x: float):
        self.value = self.value + float(x)
        return self.value

    def subtract(self, x: float):
        self.value = self.value - float(x)
        return self.value

    def multiply(self, x: float):
        self.value = self.value * float(x)
        return self.value

    def divide(self, x: float):
        x = float(x)
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.value = self.value / x
        return self.value

    def exponent(self, x: float):
        self.value = self.value ** float(x)
        return self.value

    def nth_root(self, n: float):
        n = float(n)
        if n == 0:
            raise ValueError("0-th root is undefined")
        # nth root = value ** (1/n)
        self.value = self.value ** (1.0 / n)
        return self.value

    def set_value(self, x: float):
        self.value = float(x)
        return self.value

    def get_value(self):
        return self.value

# CLI wrapper (keeps behaviour similar to original main)
def cli():
    ops = {
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide",
        "^": "exponent",
        "v": "nth_root"
    }

    calc = Calculator()
    try:
        initial = float(input("What's the first number? "))
    except ValueError:
        print("Please enter a number.")
        return

    calc.set_value(initial)

    should_continue = True
    while should_continue:
        print("Available operations:", " ".join(ops.keys()))
        op = input("Pick an operation: ").strip()
        if op not in ops:
            print("Unknown operation. Try again.")
            continue

        try:
            nxt = float(input("What's the next number? "))
        except ValueError:
            print("Please enter a number.")
            continue

        try:
            if op == "v":
                result = calc.nth_root(nxt)
                print(f"{nxt} {op} {calc.get_value()} = {result}")
            else:
                method = getattr(calc, ops[op])
                result = method(nxt)
                print(f"{calc.get_value()} {op} {nxt} = {result}")
        except Exception as e:
            print("Error:", e)
            # do not crash — let user try again
            continue

        cont = input("Type 'y' to continue calculating with result, or 'n' to start new: ").strip().lower()
        if cont == "y":
            # keep calc.value as-is and continue
            pass
        else:
            should_continue = False

if _name_ == "_main_":
    cli()
