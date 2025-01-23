from os.path import exists

data = "Line 1", "Line 2", "Line 3"
filename = "myData.txt"
if exists(filename):
    print("The file already exists!")
else:
    with open(filename, "w", encoding="UTF-8") as text:
        for line in data:
            text.write(line + "\n")
    print("Finished writing {}.".format(filename))