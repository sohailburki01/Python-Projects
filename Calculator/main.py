def add(na1, na2):
    """ This function will return the sum of two numbers """
    return na1 + na2


def exponent(ne1, ne2):
    """This function will return the power of two numbers"""
    return ne1 ** ne2


def nth_root(nr1, n):
    """Getting the nth root of nr1"""
    return nr1 ** (1 / n)


def subtract(ns1, ns2):
    """ This function will return the difference of two numbers """
    return ns1 - ns2


def multiply(nm1, nm2):
    """ This function will return the product of two numbers """
    return nm1 * nm2


def divide(nd1, nd2):
    """ This function will return the ratio of two numbers """
    return nd1 / nd2


def modulus(nm1, nm2):
    """ This function will return the modulus of two numbers """
    return nm1 % nm2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent,
    "√": nth_root,
    "%": modulus
}


def calculator():
    """ This function contains the code that will work as you wish to proceed \
    an operation """
    should_continue = False
    # Input Validation so only numbers can be entered
    while not should_continue:
        try:
            num1 = float(input("What's the first number?(to pick √, hold alt + 251 (on numpad)): "))
            should_continue = True
        except Exception as err:
            print("Please enter a number.")
            should_continue = False
        print("")

    should_continue2 = False
    while not should_continue2:
        operation_symbol = input("Pick an operation: +, -, *, /, ^, √, %: ")
        if operation_symbol in ("+", "-", "*", "/", "^", "√", "%"):
            should_continue2 = True
        else:
            print("Please enter a valid operation")
            should_continue2 = False
        print("")

    should_continue3 = False
    # Input Validation so only numbers can be entered
    while not should_continue3:
        try:
            num2 = float(input("What's the next number?: "))
            should_continue3 = True
        except Exception as err:
            print("Please enter a number.")
            should_continue3 = False
        print("")

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    if operation_symbol == "√":
        print(f"{num2} {operation_symbol} {num1} = {answer}")
    else:
        print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer},\
         or type 'n' to start a new calculation: ") == "y":
        num1 = answer
    else:
        should_continue = False
    calculator()


calculator()
