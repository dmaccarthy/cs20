from struct import unpack

numAsBytes = bytes([0, 188, 97, 78, 8, 92, 81, 205])
numTuple = unpack("!i f", numAsBytes)
print(numTuple)
