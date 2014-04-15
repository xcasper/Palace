from kivy.base import runTouchApp
from kivy.lang import Builder

from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.core.image import Image
from kivy.properties import ObjectProperty

Builder.load_string('''
<Root>:
    PalaceGame:
        pos: 800, 600
    PlayerOneCardHolder:
        pos: 300, 100
    PlayerTwoCardHolder:
        pos: 150, 225
    PlayerThreeCardHolder:
        pos: 300, 475
    PlayerFourCardHolder:
        pos: 600, 225

<PalaceGame>:
    Image:
        source: 'tablecutout.png'
        allow_stretch: True
        keep_ratio: False
        size: 800, 600

<PlayerOneCardHolder>:
    canvas:
        Color:
            rgba: 0, 0, 0, .5
        Rectangle:
            pos: self.pos
            size: 200, 50

<PlayerTwoCardHolder>:
    canvas:
        Color:
            rgba: 0, 0, 0, .5
        Rectangle:
            pos: self.pos
            size: 50, 200

<PlayerThreeCardHolder>:
    canvas:
        Color:
            rgba: 0, 0, 0, .5
        Rectangle:
            pos: self.pos
            size: 200, 50

<PlayerFourCardHolder>:
    canvas:
        Color:
            rgba: 0, 0, 0, .5
        Rectangle:
            texture: self.card.texture
            pos: self.pos
            size: 50, 200
''')

class Root(Widget):
    pass

class PalaceGame(Widget):
    pass

class PlayerOneCardHolder(Widget):
    pass

class PlayerTwoCardHolder(Widget):
    pass

class PlayerThreeCardHolder(Widget):
    pass

class PlayerFourCardHolder(Widget):
    card = ObjectProperty(None)

    def __init__(self, **kw):
        super(PlayerFourCardHolder, self).__init__(**kw)
        self.card = Image('chips.png')

runTouchApp(Root())