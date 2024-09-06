"Assignment 5, Example 1, Mouse Events"

# Ensure that the 'current working directory' is set
# properly so that Python can find the image files.

import os
os.chdir(os.path.split(__file__)[0])


from sc8pr import Sketch, Image
from sc8pr.sprite import Sprite

def setup(sk):
    "Initialize the sketch"
    sk.bg = Image("img/sky.png")
    sk["player"] = Sprite("img/alien.png").config(
        pos=sk.center, width=sk.width / 10
    ).bind(ondrag, onclick, onmouseover)
    sk.bind(onclick=missed)

def onclick(alien, ev):
    print("Ouch! You hit me with button {}.".format(ev.button))

def onmouseover(alien, ev):
    print("That tickles!")

def ondrag(alien, ev):
    print("Wheeeeeee!")
    x, y = alien.pos
    dx, dy = ev.rel
    alien.pos = x + dx, y + dy

def missed(sk, ev):
    "onclick handler for the sketch"
    print("You missed!")

# Play the sketch
Sketch().play()
