"Example 2 - Updating the Text"

from random import randint
from sc8pr import Sketch
from sc8pr.text import Text, Font, BOLD

def setup(sk):
    "Initialize the sketch"
    sk.config(bg="yellow", frameRate=4)
    sk += Text(0).bind(ondraw).config(
        font = Font.mono(),
        fontSize = 48,
        fontStyle = BOLD,
        pos = sk.center,
        bg = "red",
        padding = 6
    )

def ondraw(text, ev):
    "Change the number"
    text.config(data=randint(0,100))

# Play the sketch
Sketch().play()
