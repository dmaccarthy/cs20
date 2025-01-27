mode = "rb"
with open("myData.txt", mode) as input:
    contents = input.read()
    print(type(contents), contents)
