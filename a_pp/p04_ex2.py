"""
CSE 2110: Procedural Programming
Pre- & Post-Conditions
Example 2

"""

def intOnly(num: int):
    assert type(num) is int, "Argument must be an integer"

intOnly("Bad data")
