from struct import pack

data = -12345678, 3.1416, -45.0, 6.63e-34
numAsBytes = pack("!i 3d", *data)
print(numAsBytes, list(numAsBytes))
