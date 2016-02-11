# The time library is needed to measure execution time
import time
start_time = time.time()

# import the PIL library to manipulate images
# colorsys library to manipulate colors
# operator library to sort the values of the array in the fastest way
from PIL import Image
import colorsys
from operator import itemgetter

x = 2
y = 0
value = 100


# This function gets an hexrgb value and converts it to an hsv value
# so it can be sorted in an easier way
def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")  # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i + 2], 16) / 255.0 for i in range(0, 5, 2))
    return colorsys.rgb_to_hsv(r, g, b)


# This function converts hex colors values to rgb
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


# This function converts rgb colors values to hex
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


# Functions usage examples
# hex_to_rgb("#ffffff")             #==> (255, 255, 255)
# hex_to_rgb("#ffffffffffff")       #==> (65535, 65535, 65535)
# rgb_to_hex((255, 255, 255))       #==> '#ffffff'
# rgb_to_hex((65535, 65535, 65535)) #==> '#ffffffffffff'

# We open the image and load it
im = Image.open("imghor.jpg")
pix = im.load()

# We get the width and height of the image for iteration
width, height = im.size
size = im.size
# To print the tuple (which is not printable as string) we need to add a comma after the variable name
print("\n-- Size of the image: %s --\n" % (size,))

# Creates an array to store the values
outpix = []

# Let's cycle through the pixels in the image
for x in range(0, width):
    print("Values for pixel of x: %i and y: %i" % (x+1, y+1))
    print(pix[x, y]) # we get the rgba value for debug purposes
    # Converts the rgb value to hex
    hexpix = rgb_to_hex(pix[x, y])
    print(hexpix) # debug
    # Converts the hex to hsv
    hsvpix = get_hsv(hexpix)
    print(hsvpix)
    # We append the values to the array
    outpix.append(hsvpix)
    print(outpix)
    print("\n")
    pass

# We sort the array
outpix.sort()
print("-- Sorted array: %s" % (outpix,) + " --")

print("\n-- exec time: %s seconds --" % (time.time() - start_time))
