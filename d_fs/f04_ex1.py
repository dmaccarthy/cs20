with open("myData1.txt", "r", encoding="UTF-8") as text:
    text.seek(8)
    data = text.read(4)
print(data)