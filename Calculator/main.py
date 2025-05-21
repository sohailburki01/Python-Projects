def format_result(result):
    """Return int if result is whole number, else float."""
    if result % 1 == 0:
        return int(result)
    return result

def add(na1, na2):
    """ This function will return the sum of two numbers """
    return format_result(na1 + na2)

def exponent(ne1, ne2):
    """This function will return the power of two numbers"""
    return format_result(ne1 ** ne2)

def nth_root(nr1, n):
    """Getting the nth root of nr1"""
    return format_result(nr1 ** (1 / n))

def subtract(ns1, ns2):
    """ This function will return the difference of two numbers """
    return format_result(ns1 - ns2)

def multiply(nm1, nm2):
    """ This function will return the product of two numbers """
    return format_result(nm1 * nm2)

def divide(nd1, nd2):
    """ This function will return the ratio of two numbers """
    return nd1 / nd2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent,
    "√": nth_root
}


def calculator():
    """ This function contains the code that will work as you wish to proceed \
    an operation """
    
    num1 = input("What's the first number?(to pick √, hold alt + 251 (on numpad)): ")
    for symbol in operations:
        print(symbol)

    while True:
        operation_symbol = input("Pick an operation: ")
        num2 = input("What's the next number?: ")
        try:
            calculation_function = operations[operation_symbol]
            answer = calculation_function(float(num1), float(num2))
        except KeyError:
            print("Invalid operation. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        if operation_symbol == "√":
            print(f"{num2} {operation_symbol} {num1} = {answer}")
        else:
            print(f"{num1} {operation_symbol} {num2} = {answer}")

        next = input(f"Type 'y' to continue calculating with {answer},\
             or type 'n' to start a new calculation" + "\nIf you want to shut down the calc, press anything else :" )
        if next == "y":
            num1 = answer
        elif next == "n":
            print("Starting a new calculation...")
            calculator()
        else:
            print("Exiting the calculator.")
            break


calculator()
