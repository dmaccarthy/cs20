with open("myData2.txt", "r+", encoding="UTF-8") as text:
    print("Original File:")
    print(text.read())
    text.seek(11)
    text.write("Star Wars 4: A New Hope")
    text.seek(0)
    print("\nModified File:")
    print(text.read())