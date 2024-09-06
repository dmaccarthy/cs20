"""
CSE 2110: Procedural Programming
Pre- & Post-Conditions
Example 4

"""

def sortThree(num1: float, num2: float, num3: float) -> tuple:
    "Sort three numbers from lowest to highest"

    # Preconditions...
    errorMsg = "All arguments must be integers or floats"
    assert type(num1) in (int, float), errorMsg
    assert type(num2) in (int, float), errorMsg
    assert type(num3) in (int, float), errorMsg

    # Sort the numbers...
    lowest = min(num1, num2, num3)
    highest = max(num1, num2, num3)
    total = num1 + num2 + num3
    middle = total - lowest - highest

    # Postcondition...
    assert lowest <= middle and middle <= highest

    return lowest, middle, highest


# Main program
print(sortThree(3, 1, -2.5))
print(sortThree(3, 1, False))
