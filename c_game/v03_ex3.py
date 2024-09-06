"Example 3 - Text Inputs"

from sc8pr import Sketch
from sc8pr.gui.textinput import TextInput
from sc8pr.text import Font, BOLD

def setup(sk):
    "Initialize the sketch"
    sk.bg ="yellow"
    sk += TextInput("", "Name?").config(
        font = Font.mono(),
        fontSize = 48,
        fontStyle = BOLD,
        pos = sk.center,
        bg = "red",
        padding = 6
    ).bind(ondraw)

def ondraw(text, ev):
    "Print the text data"
    frame = text.sketch.frameCount
    print(frame, text.data)

# Play the sketch
Sketch().play()
