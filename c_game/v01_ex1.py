"Assignment 1, Example 1 - Sketch Background"

# Ensure that the 'current working directory' is set
# properly so that Python can find the image files.

import os
os.chdir(os.path.split(__file__)[0])


from sc8pr import Sketch, Image

def setup(sk):
    "Display an image as the sketch background"
    sk.bg = Image("img/sky.png")

# Play the sketch
Sketch().play()
