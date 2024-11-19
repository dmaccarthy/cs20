import os, fnmatch

allItems = os.listdir()
pngFiles =  fnmatch.filter(allItems, "*.png")
print("All items:", allItems)
print("PNG files:", pngFiles)