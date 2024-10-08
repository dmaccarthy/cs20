"""

"""

# Ensure that the 'current working directory' is set
# properly so that Python can find the image files.

import os
os.chdir(os.path.split(__file__)[0])


from random import uniform, randint
from sc8pr import Sketch, Image, BOTH
from sc8pr.sprite import Sprite, Collisions

def setup(sk):
    "Initialize the sketch"
    sk.bg = Image("img/sky.png")
    sk.alien = Image("img/alien.png")
    sk.bind(ondraw)

def ondraw(sk, ev=None):
    # Remove colliding sprites
    remove = Collisions(sk).among()
    if remove:
        sk -= remove
        print("Removed {} sprites!".format(len(remove)))

    # Randomly create alien sprites
    if randint(0, sk.frameRate) == 0:
        h = sk.height / 10
        s = uniform(-2, 2)
        v = uniform(-2, 2), uniform(-2, 2)
        sk += Sprite(sk.alien).config(spin=s,
            height=h, vel=v, pos=sk.center, bounce=BOTH)

# Play the sketch
Sketch().play()
