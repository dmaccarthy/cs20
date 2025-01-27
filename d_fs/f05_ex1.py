textAsBytes = bytes("© 2025", encoding="UTF-8")
print(textAsBytes)          # b'\xc2\xa9 2025'
print(list(textAsBytes))    # [194, 169, 32, 50, 48, 50, 53]
