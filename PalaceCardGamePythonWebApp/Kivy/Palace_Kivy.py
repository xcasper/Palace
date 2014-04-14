#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Craig
#
# Created:     11/04/2014
# Copyright:   (c) Craig 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Note:
#   Get Graphics done basically and then upgrade graphics
#   Dont focus on making it look great at first.



#What does it need to do? (not in a particular order)
#
#   *COMPLETE*1) Display a background card table
#
#   2) Area for each player's cards to be displayed, and then display back of
#   cards if not yours to see
#       2A) This needs to update based on what cards a person has
#           2Aa) Card area will display one of each rank of card that a player
#           has in their hand, then will open an additional menu if more then 1
#           of that rank exist
#
#   3) Area for middle pile
#
#   4) Area for each players palace
#
#   5) Area for each players topofpalace (which displays ontop of the palace
#   section)
#
#   6) Allow a player to pick a card, show if he has more then 1 of those cards,
#   and let them choose to play more then 1 if they wish
#       6A) Play will be done by clicking card, and any additional to play, and
#       then clicking middle pile.

#Initial Background Creation
#TODO: Figure out how to move this to .kv file if possible
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from random import random
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.button import Button

Builder.load_string('''
<GridLayout>
    canvas.before:
        BorderImage:
            # BorderImage behaves like the CSS BorderImage
            border: 10, 10, 10, 10
            source: 'C:/Users/Craig/Documents/GitHub/Palace/PalaceCardGamePythonWebApp/Kivy/tablecutout.png'
            pos: self.pos
            size: self.size


<PalaceGame>
    GridLayout:
        size_hint: .9, .9
        # helps display exactly center of screen (pos 0-1)
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1
''')
class PalaceGame(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(PalaceGame, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
                        Rectangle(
                                text="Test",
                                size_hint= (.1, .1),
                                pos_hint={'center_x':.25,
                                        'center_y':.25}))

    #just for testing how kivy functions -- remove for actual game
    def on_touch_down(self, touch):
        with self.canvas.before:
            Color(0, 0, 1)
            #diameter
            d = 60.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class PalaceApp(App):

    def build(self):
        self.game = game = PalaceGame()
        game.bind(
                    size=self._update_rect,
                    pos=self._update_rect)
        with game.canvas.before:
            self.rect = Rectangle(
                                    size=game.size,
                                    pos=game.pos)
        return game

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    PalaceApp().run()