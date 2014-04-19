from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.app import App

from kivy.uix.widget import Widget


from kivy.core.window import Window
from kivy.core.image import Image
from kivy.properties import ObjectProperty

Builder.load_string('''
<LayoutTree>:
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
        Rectangle:
            source: '2_spade_bot.png'
            pos: self.pos
            size: 15, 50

<PlayerTwoCardHolder>:
    canvas:
        Rectangle:
            source: '2_spade_left.png'
            pos: self.pos
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 240
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 255
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 270
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 285
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 300
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 315
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 330
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 345
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 360
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 375
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 390
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 405
            size: 50, 15
        Rectangle:
            source: '2_spade_left.png'
            pos: 150, 420
            size: 50, 15


<PlayerThreeCardHolder>:
    canvas:
        Rectangle:
            source: '2_spade_top.png'
            pos: self.pos
            size: 15, 50

<PlayerFourCardHolder>:
    canvas:
        Rectangle:
            source: '2_spade_right.png'
            pos: self.pos
            size: 50, 15
''')

class LayoutTree(Widget):
    pass

class botCards(Widget):
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
    pass

class PalaceGameApp(App):
    pass

runTouchApp(LayoutTree())