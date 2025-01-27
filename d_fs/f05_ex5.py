from struct import pack

num1 = -12345678
num2 = 3.1416
num3 = -45.0
num4 = 6.63e-34
numAsBytes = pack("!i 3d", num1, num2, num3, num4)
print(numAsBytes, list(numAsBytes))
