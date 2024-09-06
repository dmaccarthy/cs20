"Assignment 1, Example 3 - Sprites"

# Ensure that the 'current working directory' is set
# properly so that Python can find the image files.

import os
os.chdir(os.path.split(__file__)[0])


from sc8pr import Sketch, Image
from sc8pr.sprite import Sprite

def setup(sk):
    "Create a background and a single sprite"
    sk.bg = Image("img/sky.png")
    sk += Sprite("img/alien.png")

# Play the sketch
Sketch().play()
