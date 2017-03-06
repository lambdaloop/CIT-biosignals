import pygame
from pygame.locals import *
from constants import *
from generate_images import *
import time
import pandas as pd
from pylsl import StreamInfo, StreamOutlet
import random

pygame.init()
#pygame.mouse.set_visible(False)

from screen import screen
from drawstuff import *

study_time = int(time.time())
print(study_time)

info = StreamInfo('Ganglion_EEG', 'Markers', 1, 0.0, 'int32',
                  'marker')
outlet = StreamOutlet(info)

images = gen_images()

def check_for_key(key=K_ESCAPE):
    while True:
        event = pygame.event.poll()
        if event.type == 0:
            return False
        elif event.dict.get('key', -1) == key:
            return True

def check_for_escape():
    return check_for_key(K_ESCAPE)

def finish_stuff(early=False):
    return


text_slide("""Start recording and
press space to continue""")
while not check_for_key(K_SPACE):
    pass

focus_slide()
outlet.push_sample([-1], time.time())
time.sleep(0.5)

images = [(path, pygame.image.load(path)) for path in images]

t = time.time()

for image_path, img in images:
    # if d['is_shown'] != 1:
    #     continue

    # word = d['word']
    print(time.time() - t)
    t = time.time()

    print(image_path, hash(image_path))
    image_slide(img)
    outlet.push_sample([hash(image_path)], time.time())
    time.sleep(4)

    if check_for_escape():
        finish_stuff(early=True)
        exit()

    focus_slide()
    outlet.push_sample([-1], time.time())
    time.sleep(2.0)

    if check_for_escape():
        finish_stuff(early=True)
        exit()

