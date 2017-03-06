#!/usr/bin/env python

import pyglet
from time import time, sleep
from generate_images import *
from pyglet.text import Label, HTMLLabel

from pyglet.gl import *

window = pyglet.window.Window()
image = pyglet.resource.image('img/2017-03-05-153649_2560x1558_scrot.png')
image.scale = 0.1

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()
