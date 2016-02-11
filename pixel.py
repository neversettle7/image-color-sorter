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


def imgopen(filename):
    'This function opens an image file'
    img = Image.open(filename)
    print(img)
    loadedimg = img.load()
    return (img, loadedimg)


def imgcreate(width, height):
    'This function creates a new image file - IT IS NOT SAVING IT'
    img = Image.new("RGB", (width, height))
    newloaded = img.load()
    return (img, newloaded)


def saveimg(image, filename):
    'This function saves the image file on the disk'
    image.save(filename)
    return


def getsize(image):
    'This function gets the size of the image'
    width, height = image.size
    size = image.size
    print("\n-- Size of the image is: {0} ({1}x{2})".format(size, width, height))
    return (size, width, height)


def getpixels(image, width, height):
    'This function gets the pixels of the image and stores them in an array'
    array = []
    for x in range(0, width):
        print("Values for pixel of x: {0} and y: {1}".format(x + 1, y + 1))
        print("RGB values: {0}".format(image[x, y]))  # we get the rgb value for debug purposes
        red, green, blue = (image[x, y])
        hsvcolors = colorsys.rgb_to_hsv(red, green, blue)
        print("HSV values: {0}".format(hsvcolors))
        array.append(hsvcolors)
        print("\n")
        pass
    return (array)


def sortarray(array):
    'This function just sorts the array'
    array.sort()
    return (array)


def writepixels(array, image, width, height):
    'This function writes the pixel values in the output image'
    for x in range(0, width):
        # Write the new color
        hue, saturation, value = array[x]
        # print("hue: {0}, sat: {1}, value: {2}\n" .format(hue, saturation, value))
        rgbvalues = colorsys.hsv_to_rgb(hue, saturation, value)
        # print("rgbvalues: ")
        # print(rgbvalues)
        red, green, blue = rgbvalues
        image[x, y] = int(red), int(green), int(blue)
        print(image[x, y])
        pass
    return (image)


oldimg, oldimgcontent = imgopen("imghor.jpg")
size = getsize(oldimg)
width = size[1]
height = size[2]

# Creates an array to store the values
pixvalues = []

pixvalues = getpixels(oldimgcontent, width, height)

sortedvalues = sortarray(pixvalues)

newimg, newimgcontent = imgcreate(width, height)

sortedimg = writepixels(sortedvalues, newimgcontent, width, height)

saveimg(newimg,"newimg.jpg")

print("\n-- exec time: %s seconds --" % (time.time() - start_time))
