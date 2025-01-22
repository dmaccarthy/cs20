"Assignment 2, Example 1 - Customizing ondraw"

from random import uniform, randint
from sc8pr import Sketch, Image, BOTH
from sc8pr.sprite import Sprite

def setup(sk):
    "Initialize the sketch"
    sk.bg = Image("img/sky.png")
    sk.alien = Image("img/alien.png")
    sk.bind(ondraw)

def ondraw(sk, ev):
    "Randomly create alien sprites"
    if randint(0, sk.frameRate) == 0:
        h = sk.height / 10
        s = uniform(-2, 2)
        v = uniform(-2, 2), uniform(-2, 2)
        sk += Sprite(sk.alien).config(spin=s, height=h,
            vel=v, pos=sk.center, bounce=BOTH)

# Play the sketch
Sketch().play()
