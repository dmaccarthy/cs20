data = "Line 4", "Line 5", "Line 6"
filename= "myData.txt"
with open(filename, "a", encoding="UTF-8") as text:
    for line in data:
        text.write(line + "\n")
print("Finished appending to {}.".format(filename))