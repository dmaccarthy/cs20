"Assignment 4, Example 1 - Keyboard Events"

# Ensure that the 'current working directory' is set
# properly so that Python can find the image files.

import os
os.chdir(os.path.split(__file__)[0])


from sc8pr import Sketch, Image
from sc8pr.sprite import Sprite

def setup(sk):
    "Initialize the sketch"
    sk.bg = Image("img/sky.png")
    sk["player"] = Sprite("img/alien.png").config(pos=sk.center,
        width=sk.width / 10)
    sk.bind(onkeydown)

def onkeydown(sk, ev):
    "Move the alien with the keyboard"
    player = sk["player"]
    x, y = player.pos
    letter = ev.unicode.lower()
    if letter == "a":
        player.pos = x - 5, y
    elif letter == "s":
        player.pos = x + 5, y

# Play the sketch
Sketch().play()
