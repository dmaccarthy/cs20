"Assignment 1, Example 1 - Sketch Background"

from sc8pr import Sketch, Image

def setup(sk):
    "Display an image as the sketch background"
    sk.bg = Image("img/sky.png")

# Play the sketch
Sketch().play()
