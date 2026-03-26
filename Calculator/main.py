def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exponent(a, b):
    return a ** b

def nth_root(a, n):
    return a ** (1 / n)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent,
    "√": nth_root
}


num1 = float(input("Enter first number: "))

for op in operations:
    print(op)

while True:
    op = input("Choose operation: ")
    num2 = float(input("Enter next number: "))

    result = operations[op](num1, num2)

    if op == "√":
        print(num2, "√", num1, "=", result)
    else:
        print(num1, op, num2, "=", result)

    cont = input("Continue? (y/n): ")

    if cont == "y":
        num1 = result
    else:
        break
