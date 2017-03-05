import pyglet
from pyglet.text import Label, HTMLLabel

from pyglet.gl import *

key = pyglet.window.key
#figbg = "test.jpg"

class LabelPgl(Label):
    def __init__(self, text, x=0, y=0, font_name = 'Times New Roman',
                 font_size=36):
        super(LabelPgl, self).__init__('Hello, world',
                  font_name=font_name,
                  font_size=font_size,
                  anchor_x='center', anchor_y='center')

    def _draw(self):
        self.draw()


class CustomSprite(pyglet.sprite.Sprite):
    def __init__(self, texture_file, x=0, y=0):
        ## Must load the texture as a image resource before initializing class:Sprite()
        self.texture = pyglet.image.load(texture_file)

        super(CustomSprite, self).__init__(self.texture)
        self.x = x
        self.y = y

    def _draw(self):
        self.draw()

class MainScreen(pyglet.window.Window):
    def __init__ (self):
        super(MainScreen, self).__init__(800, 600, fullscreen = False)
        self.x, self.y = 0, 0

        #self.bg = CustomSprite(figbg)
        self.sprites = []
        self.alive = 1

    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = 0

    def clear_sprites(self):
        try:
            self.clear()
            self.sprites.pop()
        except:
            pass

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE: # [ESC]
            self.alive = 0
        elif symbol == key.C:
            print('Rendering cat')
            self.clear_sprites()
            self.sprites.append(
                    CustomSprite('img/cat.png', x=10, y=10)
                               )
        elif symbol == key.D:
            print('Rendering dog')
            self.clear_sprites()
            self.sprites.append(
                    CustomSprite('img/dog.png', x=10, y=10)
                               )
        elif symbol == key.R:
            print('Rendering hello')
            self.label = HTMLLabel(
                       '''<font face="Times New Roman" size="32" color="white">
                       Hello, <i>world</i></font>''',
                       x=self.width//2, y=self.height//2,
                       anchor_x='center', anchor_y='center')
            self.label.draw()

        elif symbol == key.T:
            print('Rendering hello plain')
            self.label = LabelPgl('Hello, world',
                  font_name='Times New Roman',
                  font_size=36,
                  x=self.width//2, y=self.height//2,
                  )
            self.label.draw()


    def render(self):
        self.clear()
        #self.bg.draw()

        for sprite_obj in self.sprites:
            sprite_obj._draw()

        self.flip()

    def run(self):
        while self.alive == 1:
            self.render()

            # -----------> This is key <----------
            # This is what replaces pyglet.app.run()
            # but is required for the GUI to not freeze
            #
            event = self.dispatch_events()

x = MainScreen()
x.run()


