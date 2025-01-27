textAsBytes = bytearray("© 1998", encoding="UTF-8")

textAsBytes[-4:] = b"2025"
textAsBytes.extend(b" by Jane Doe")
textAsStr = str(textAsBytes, encoding="UTF-8")

print(textAsBytes) # bytearray(b'\xc2\xa9 2025 by Jane Doe')
print(textAsStr)   # © 2025 by Jane Doe

