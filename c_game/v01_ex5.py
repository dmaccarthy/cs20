"Assignment 1, Example 5 - Animation"

# Ensure that the 'current working directory' is set
# properly so that Python can find the image files.

import os
os.chdir(os.path.split(__file__)[0])


from sc8pr import Sketch, Image, VERTICAL, HORIZONTAL
from sc8pr.sprite import Sprite

def setup(sk):
    "Create a background and a single sprite"
    sk.bg = Image("img/sky.png")
    h = sk.height / 10
    sk += Sprite("img/alien.png").config(spin=2,
        height=h, vel=(2, -1), pos=sk.center,
        bounce=HORIZONTAL, wrap=VERTICAL)

# Play the sketch
Sketch().play()
