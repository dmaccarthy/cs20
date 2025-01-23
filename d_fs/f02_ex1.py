text = open("myData.txt", encoding="UTF-8")
for line in text:
    print(line.rstrip())
text.close()