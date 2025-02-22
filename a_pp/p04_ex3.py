"""
CSE 2110: Procedural Programming
Pre- & Post-Conditions
Example 3

"""

def recentYear(year: int):
    assert type(year) is int, "Argument must be an integer"
    assert year >= 2019 and year <= 2024, "Invalid year!"
    print(f"{year} is a good year.")

recentYear(2020)
recentYear(1996)
