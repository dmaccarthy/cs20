with open("myData.txt", encoding="UTF-8") as text:
    for line in text:
        print(line.rstrip())