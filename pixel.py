# The time library is needed to measure execution time
# PIL library to manipulate images
# colorsys library to manipulate colors
# operator library to sort the values of the array in the fastest way
from PIL import Image
import colorsys
import time
start_time = time.time()

# Temporary variable until height iteration is developed
y = 0

# We open the image and load it
oldimg = Image.open("imghor.jpg")
pix = oldimg.load()

# We get the width and height of the image for iteration
width, height = oldimg.size
size = oldimg.size
# To print the tuple (which is not printable as string) we need to add a comma after the variable name
print("\n-- Size of the image: %s --\n" % (size,))

# Creates an array to store the values
outpix = []

# Let's cycle through the pixels in the image
for x in range(0, width):
    print("Values for pixel of x: {0} and y: {1}" .format(x+1, y+1))
    print("RGB values: {0}" .format(pix[x, y])) # we get the rgb value for debug purposes
    red, green, blue = (pix[x, y])
    hsvvalues = colorsys.rgb_to_hsv(red, green, blue)
    print("HSV values: {0}" .format(hsvvalues))
    outpix.append(hsvvalues)
    print("\n")
    pass

# We sort the array
outpix.sort()
print("-- Sorted array: %s" % (outpix,) + " --\n")

# Time to create the new image!
newimg = Image.new("RGB", (width, height))
newpix = newimg.load()

# Let's cycle through the image and write the new values
for x in range(0, width):
    # Write the new color
    '''print("outpix: ")
    print(outpix[x])'''
    hue, saturation, value = outpix[x]
    #print("hue: {0}, sat: {1}, value: {2}\n" .format(hue, saturation, value))
    rgbvalues = colorsys.hsv_to_rgb(hue, saturation, value)
    #print("rgbvalues: ")
    #print(rgbvalues)
    red, green, blue = rgbvalues
    newpix[x,y] = int(red), int(green), int(blue)
    print(newpix[x, y])
    pass

# Save the image
newimg.save("newimg.jpg")

print("\n-- exec time: %s seconds --" % (time.time() - start_time))
