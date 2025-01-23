import os
from os.path import isfile, isdir, getmtime, getsize
from datetime import date
from random import choice

# Get a random file or folder name
# from the current working directory
item = choice(os.listdir())

# Get info about the item
if isfile(item): kind = "a file"
elif isdir(item): kind = "a folder"
else: kind = "something unknown"
size = getsize(item)
modified = getmtime(item)

# Output the info
print("'{}' is {}.".format(item, kind))
template = "It was last modified on {}."
print(template.format(date.fromtimestamp(modified)))
print("It contains {} bytes of information.".format(size))