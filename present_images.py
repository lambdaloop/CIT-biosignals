#!/usr/bin/env python

import pyglet
from time import time, sleep
from generate_images import *
from pyglet.text import Label, HTMLLabel
from threading import Thread

from pyglet.gl import *

images = gen_images()

class MainScreen(pyglet.window.Window):
    def __init__ (self,
            width=800,
            height=600,
            background_color = (0, 0,0,0)):
        super(MainScreen, self).__init__(width, height, fullscreen = False)
        self.x, self.y = 0, 0

        #self.bg = CustomSprite(figbg)
        self.image = None
        self.alive = 1
        # sets the background color
        gl.glClearColor(*background_color)

    def image_thread(self):
        for image_path in images:
            print(image_path)
            self.image = pyglet.resource.image(image_path)
            self.image.anchor_x = self.image.width // 2
            self.image.anchor_y = self.image.height // 2
            sleep(5)

    def on_draw(self):
        self.render()
    
    def render(self):
        self.clear()
        print('render')
        if self.image is not None:
            self.image.blit(self.width/2, self.height/2)

        sleep(0.01)
            
        self.flip()
            
    def run(self):
        self.thread = Thread(target=self.image_thread)
        self.thread.start()
        
        while self.alive == 1:
            self.render()

            # -----------> This is key <----------
            # This is what replaces pyglet.app.run()
            # but is required for the GUI to not freeze
            #
            event = self.dispatch_events()

            


# window.clear()
# image.blit(0, 0)

x = MainScreen()
x.run()





