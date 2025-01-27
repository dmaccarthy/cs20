from struct import pack

num = 12345678
numAsBytes = pack("!I", num)
print(numAsBytes, list(numAsBytes))
