# creating a list from single line input
try:
    # enter the separator
    separator = input("Enter the separator symbol (e.g., ',' or '-') : ")
    if not separator:
        raise ValueError("Separator cannot be empty.")

    # enter the string
    string = input("Enter the string: ")
    if not string:
        raise ValueError("Input string cannot be empty.")

    # split the string using the separator
    lst = string.split(separator)
    print("List:", lst)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
