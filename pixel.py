# Importiamo la libreria PIL
from PIL import Image
import colorsys

x = 2
y = 0
value = 100


# This function gets an hexrgb value and converts it to an hsv value
# so it can be sorted in an easier way
def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)


# This function converts hex colors values to rgb
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


# This function converts rgb colors values to hex
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

'''
# Functions usage examples
hex_to_rgb("#ffffff")             #==> (255, 255, 255)
hex_to_rgb("#ffffffffffff")       #==> (65535, 65535, 65535)
rgb_to_hex((255, 255, 255))       #==> '#ffffff'
rgb_to_hex((65535, 65535, 65535)) #==> '#ffffffffffff'
'''

# Can be many different formats.
im = Image.open("imghor.jpg")
pix = im.load()
# Get the width and hight of the image for iterating over
widht, height = im.size
size = im.size
print(size)
# Get the RGBA Value of the a pixel of an image
hexpix = rgb_to_hex(pix[x, y])
print(pix[x, y])
print(hexpix)
hsvpix = get_hsv(hexpix)
print(hsvpix)
