import random
import os
import glob

def gen_image():
	images = glob.glob("img/*.png")
	print(images)
	rand_images = random.sample(images, len(images))
	print(rand_images)
	return rand_images