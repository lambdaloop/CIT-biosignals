import random
import os
import glob

def gen_images():
	images = glob.glob("../img/*.png")
	rand_images = random.sample(images, len(images))
	return rand_images
