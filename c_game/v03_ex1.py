"Assignment 3, Example 1 - Text"

from sc8pr import Sketch
from sc8pr.text import Text, Font, BOLD

def setup(sk):
    "Initialize the sketch"
    sk.bg = "yellow"
    sk += Text("Hello, world!").config(
        pos = sk.center,
        font = Font.mono(),
        fontSize = 48,
        fontStyle = BOLD,
        bg = "red",
        color = "white",
        padding = 6
    )

# Play the sketch
Sketch().play()
