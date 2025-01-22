"Assignment 4, Example 2 - Keyboard Events"

from pygame.constants import K_LEFT, K_RIGHT
from sc8pr import Sketch, Image
from sc8pr.sprite import Sprite

def setup(sk):
    "Initialize the sketch"
    sk.bg = Image("img/sky.png")
    sk["player"] = Sprite("img/alien.png").config(
        pos=sk.center, width=sk.width / 10)
    sk.bind(onkeydown)

def onkeydown(sk, ev):
    "Move the alien with the keyboard"
    player = sk["player"]
    x, y = player.pos
    key = ev.key
    if key == K_LEFT:
        player.pos = x - 5, y
    elif key == K_RIGHT:
        player.pos = x + 5, y

# Play the sketch
Sketch().play()
