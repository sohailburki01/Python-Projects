import pytest
from main import evaluate, nth_root


# ==========================================
# 1. BASIC ARITHMETIC
# ==========================================

@pytest.mark.parametrize("expression, expected", [
    ("10 + 5", 15),
    ("10 - 5", 5),
    ("10 * 5", 50),
    ("10 / 5", 2),
    ("0 + 5", 5),
    ("0 * 100", 0),
    ("100 - 150", -50),
    ("7 / 2", 3.5),
    ("-10 + 5", -5),
    ("-10 * -5", 50),
])
def test_basic_arithmetic(expression, expected):
    assert evaluate(expression) == pytest.approx(expected)


# ==========================================
# 2. OPERATOR PRECEDENCE
# ==========================================

@pytest.mark.parametrize("expression, expected", [
    ("10 + 5 * 2", 20),
    ("10 * 5 + 2", 52),
    ("20 - 5 * 2", 10),
    ("20 / 5 + 2", 6),
    ("10 + 20 * 3 - 5", 65),
    ("20 / 5 * 2", 8),
    ("10 - 4 + 2", 8),
    ("2 + 3 * 4 / 2", 8),
])
def test_operator_precedence(expression, expected):
    assert evaluate(expression) == pytest.approx(expected)


# ==========================================
# 3. PARENTHESES
# ==========================================

@pytest.mark.parametrize("expression, expected", [
    ("(10 + 5) * 2", 30),
    ("10 * (5 + 2)", 70),
    ("(10 - 5) / 5", 1),
    ("((2 + 3) * 4)", 20),
    ("10 + (5 * (2 + 3))", 35),
    ("(10 + 5) * (2 + 3)", 75),
    ("100 / (5 * 2)", 10),
])
def test_parentheses(expression, expected):
    assert evaluate(expression) == pytest.approx(expected)


# ==========================================
# 4. DECIMAL NUMBERS
# ==========================================

@pytest.mark.parametrize("expression, expected", [
    ("2.5 + 3.5", 6),
    ("2.5 * 4", 10),
    ("10.5 / 2", 5.25),
    ("5.75 - 2.25", 3.5),
    ("0.5 * 0.5", 0.25),
    ("-3.5 + 1.5", -2),
    ("(2.5 + 1.5) * 2", 8),
])
def test_decimal_numbers(expression, expected):
    assert evaluate(expression) == pytest.approx(expected)


# ==========================================
# 5. EXPONENTIATION
# ==========================================

@pytest.mark.parametrize("expression, expected", [
    ("2 ^ 3", 8),
    ("5 ^ 2", 25),
    ("10 ^ 0", 1),
    ("2 ^ 1", 2),
    ("3 ^ 3", 27),
    ("2 ^ -2", 0.25),
    ("4 ^ 0.5", 2),
    ("27 ^ (1/3)", 3),
    ("16 ^ (1/4)", 2),
    ("81 ^ (1/2)", 9),
])
def test_exponentiation(expression, expected):
    assert evaluate(expression) == pytest.approx(expected)


# ==========================================
# 6. ROOTS USING NTH_ROOT
# ==========================================

@pytest.mark.parametrize("x, n, expected", [
    (9, 2, 3),
    (25, 2, 5),
    (27, 3, 3),
    (64, 3, 4),
    (16, 4, 2),
    (32, 5, 2),
    (125, 3, 5),
    (256, 4, 4),
    (-8, 3, -2),
    (-27, 3, -3),
])
def test_nth_root(x, n, expected):
    assert nth_root(x, n) == pytest.approx(expected)


# ==========================================
# 7. ROOT EDGE CASES
# ==========================================

def test_zero_root_degree():
    with pytest.raises(ValueError):
        nth_root(16, 0)


def test_even_root_of_negative_number():
    with pytest.raises(ValueError):
        nth_root(-16, 2)


# ==========================================
# 8. DIVISION BY ZERO
# ==========================================

@pytest.mark.parametrize("expression", [
    "10 / 0",
    "5 / (2 - 2)",
    "100 / (5 - 5)",
])
def test_division_by_zero(expression):
    with pytest.raises(ZeroDivisionError):
        evaluate(expression)


# ==========================================
# 9. INVALID EXPRESSIONS
# ==========================================

@pytest.mark.parametrize("expression", [
    "5 +",
    "* 5",
    "10 + * 5",
    "5..2 + 1",
    "abc + 5",
    "5 5",
    "",
    "()",
    "(5 + 3",
    "5 + 3)",
    "10 + (5 * )",
    "10 + @",
])
def test_invalid_expressions(expression):
    with pytest.raises(ValueError):
        evaluate(expression)


# ==========================================
# 10. UNARY OPERATORS
# ==========================================

@pytest.mark.parametrize("expression, expected", [
    ("-5", -5),
    ("+5", 5),
    ("5 * -2", -10),
    ("-5 + 10", 5),
    ("-(3 + 2)", -5),
    ("--5", 5),
])
def test_unary_operators(expression, expected):
    assert evaluate(expression) == pytest.approx(expected)
