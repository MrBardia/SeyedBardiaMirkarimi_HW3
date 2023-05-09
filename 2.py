#! usr/bin/python3

import math

def div(a: int, b: int) -> float:
    """a function tu divide two numbers

    Args:
        a (int): first number
        b (int): second number
    Returns:
        float: answer of a divided to b
    """
    try:
        return a/b
    except ZeroDivisionError:
        return math.inf

    

def main():
    x = input("Enter your first number: ")
    y = input("Enter your second number: ")
    try:
        x = int(x)
        y = int(y)
        z = div(x, y)
        print(z)
    except ValueError:
        print("Enter a number Please")
    

"""
    if we don't run this program as a module main() function would be called
"""

if __name__ == "__main__":
    main()


