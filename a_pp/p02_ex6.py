"""
CSE 2110: Procedural Programming
Variable Scope
Example 6

"""

ABSOLUTE_ZERO = -273.15
IDEAL_GAS_CONST = 8.314
AVOGADROS_NUM = 6.02e23

def pressure(n, T, V):
    "Calculate ideal gas pressure"
    P = n * IDEAL_GAS_CONST * (T - ABSOLUTE_ZERO) / V
    return P

def main():
    # Input...
    T = float(input("Temperature in Celsius: "))
    V = float(input("Volume in litres: "))
    n = float(input("Number of moles: "))

    # Processing...
    P = pressure(n, T, V)
    N = n * AVOGADROS_NUM

    # Output...
    print("The pressure is {:.2f} kPa.".format(P))
    print("There are {:.2e} molecules of gas.".format(N))

main()
