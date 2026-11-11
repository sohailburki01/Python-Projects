def precedence(op):
    #priority order for operations
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    if op == '^':
        return 3
    return 0


def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    elif op == '^':
        return a ** b
    
def nth_root(x,n):
    if n==0:
        raise ValueError("root cannot be zero")
    if x<0:
        if n%2 == 0:
            raise ValueError("even root of negative number does not exist")
        return -((-x)**(1/n))
    return x**(1/n)


def apply_operator(values, operators):
    op = operators.pop()

    if len(values) < 2:
        raise ValueError("Invalid expression")

    b = values.pop()
    a = values.pop()

    values.append(calculate(a, b, op))


def evaluate(expression):
    values = []
    operators = []

    i = 0
    n = len(expression)
    expect_operand = True

    while i < n:
        ch = expression[i]

        # Ignore spaces
        if ch.isspace():
            i += 1
            continue

        # Read number (integer or decimal)
        if ch.isdigit() or ch == '.':
            if not expect_operand:
                raise ValueError("Missing operator")

            num = ""
            dots = 0

            while i < n and (expression[i].isdigit() or expression[i] == '.'):
                if expression[i] == '.':
                    dots += 1

                if dots > 1:
                    raise ValueError("Invalid decimal number")

                num += expression[i]
                i += 1

            if num == '.':
                raise ValueError("Invalid number")

            values.append(float(num))
            expect_operand = False
            continue

        # Opening parenthesis
        elif ch == '(':
            if not expect_operand:
                raise ValueError("Missing operator before '('")

            operators.append(ch)
            expect_operand = True

        # Closing parenthesis
        elif ch == ')':
            if expect_operand:
                raise ValueError("Invalid expression or empty parentheses")

            while operators and operators[-1] != '(':
                apply_operator(values, operators)

            if not operators:
                raise ValueError("Mismatched parentheses")

            operators.pop()
            expect_operand = False

        # Operators
        elif ch in '+-*/^':

            # Unary plus and minus
            if expect_operand:
                if ch == '+':
                    i += 1
                    continue

                if ch == '-':
                    values.append(0.0)
                    operators.append('-')

                    i += 1
                    continue

                raise ValueError("Operator missing left operand")

            while (operators and
                   operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(ch)):

                apply_operator(values, operators)

            operators.append(ch)
            expect_operand = True

        else:
            raise ValueError(f"Invalid character: {ch}")

        i += 1

    if expect_operand and n > 0:
        raise ValueError("Expression cannot end with an operator")

    # Process remaining operators
    while operators:
        if operators[-1] == '(':
            raise ValueError("Mismatched parentheses")

        apply_operator(values, operators)

    if len(values) != 1:
        raise ValueError("Invalid expression")

    return values[0]


# Interactive calculator
def calculator():
    print("Advanced Two-Stack Calculator")
    print("Supported: +, -, *, /, ^, decimals, negative numbers, ()")
    print("Type 'quit' to exit.")

    while True:
        expression = input("\nEnter expression: ").strip()

        if expression.lower() == 'quit':
            print("Goodbye!")
            break

        if not expression:
            continue

        try:
            result = evaluate(expression)
            print("Result:", result)

        except (ValueError, ZeroDivisionError, OverflowError) as e:
            print("Error:", e)


if __name__ == "__main__":
    calculator()
