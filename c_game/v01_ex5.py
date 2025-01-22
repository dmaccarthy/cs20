"Assignment 1, Example 5 - Animation"

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
