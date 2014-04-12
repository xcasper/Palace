from kivy.app import App
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class PalaceGame(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(PalaceGame, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
                        Button(
                                text="Test",
                                size_hint= (.1, .1),
                                pos_hint={'center_x':.25,
                                        'center_y':.25}))

    #just for testing how kivy functions -- remove for actual game
    def on_touch_down(self, touch):
        with self.canvas:
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
            Color(0, 1, 0, 1) # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(
                                    size=game.size,
                                    pos=game.pos)
        return game

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    PalaceApp().run()