"Assignment 1, Example 3 - Sprites"

from sc8pr import Sketch, Image
from sc8pr.sprite import Sprite

def setup(sk):
    "Create a background and a single sprite"
    sk.bg = Image("img/sky.png")
    sk += Sprite("img/alien.png")

# Play the sketch
Sketch().play()
