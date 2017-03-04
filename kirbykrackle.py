#!/usr/bin/env python
from PIL import Image, ImageDraw
from random import randint
import sys
import os

def invokeKirby():
    with open(os.devnull, 'w') as f:
        message = '''O Jack Kirby, master of comics, I call upon thee:
            guide our random function and make us some cool krackles.'''
        f.write(message)

    print 'Jack Kirby invocation successful.'

def drawCircle(draw, x, y, radius):
    draw.ellipse((x, y, x + radius, y + radius),
        fill="black", outline="black")

width = 800
height = 600

try:
    starting_points = int(sys.argv[1])
    number_of_circles = int(sys.argv[2])
    max_distance = int(sys.argv[3])
except:
    print 'You\'re doing it wrong.'
    print 'Usage: kirbykrackle.py' + \
        '<starting points> <number of circles> <max distance> (<output file>)'
    sys.exit()

try:
    output_file = sys.argv[4]
except:
    output_file = False

invokeKirby()

R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)

img = Image.new('RGB', (width, height), (R, G, B))
draw = ImageDraw.Draw(img)

for i in xrange(starting_points):
    x = randint(0, width)
    y = randint(0, height)

    for p in xrange(number_of_circles):
        x += randint(0 - max_distance, max_distance)
        y += randint(0 - max_distance, max_distance)
        radius = randint(2, max_distance)

        drawCircle(draw, x, y, radius)

if output_file:
    img.save(output_file)
    print 'Image saved at', output_file
else:
    img.show()
