# The time library is needed to measure execution time
# PIL library to manipulate images
# colorsys library to manipulate colors
# operator library to sort the values of the array in the fastest way
from PIL import Image
import colorsys
import time

start_time = time.time()


def imgopen(filename):
    """This function opens an image file"""
    img = Image.open(filename)
    loadedimg = img.load()
    return (img, loadedimg)


def imgcreate(width, height):
    """This function creates a new image file - IT IS NOT SAVING IT"""
    img = Image.new("RGB", (width, height))
    newloaded = img.load()
    return (img, newloaded)


def saveimg(image, filename):
    """This function saves the image file on the disk

    VERY IMPORTANT : do NOT disable delete the subsampling = 0 setting,
    otherwise any outputted jpg file will be red-shifted

    """
    image.save(filename, subsampling=0)
    return


def getsize(image):
    """This function gets the size of the image"""
    width, height = image.size
    size = image.size
    print("\n-- Size of the image is: {0} ({1}x{2})\n".format(size, width, height))
    return (size, width, height)


def getpixels(image, width, height):
    """This function gets the pixels of the image and stores them in an array"""
    array = []
    """print("--------------------------\n"
          "----- ORIGINAL IMAGE -----\n"
          "--------------------------\n")"""
    for y in range(0, height):
        for x in range(0, width):
            red, green, blue = (image[x, y])
            array.append(image[x, y])
            """print("Values for pixel of x: {0} and y: {1}".format(x + 1, y + 1))
            print("RGB values: {0}".format(image[x, y]))  # we get the rgb value for debug purposes
            print("HSV values: {0}".format(hsvcolors))
            print("\n")"""
            pass
    pass
    return array


def rgbtohsv(array):
    arraymod = []
    for x in range(0, len(array)):
        red, green, blue = array[x]
        hsvcolors = colorsys.rgb_to_hsv(red, green, blue)
        arraymod.append(hsvcolors)
        pass
    return arraymod


def hsvtorgb(array):
    arraymod = []
    for x in range(0, len(array)):
        hue, saturation, value = array[x]
        rgbcolors = colorsys.hsv_to_rgb(hue, saturation, value)
        arraymod.append(rgbcolors)
        pass
    return arraymod


def sortarray_firstvalue(array):
    """This function sorts the array simply based on the first value.
       Example: hue for the HSV format (hue, saturation, value), red for RGB and so on"""
    array.sort()
    return array


def writepixels(array, image, width, height):
    """This function writes the pixel values in the output image"""
    """print("------------------------\n"
          "----- EDITED IMAGE -----\n"
          "------------------------\n")"""
    i = 0
    for y in range(0, height):
        for x in range(0, width):
            # Write the new color
            red, green, blue = array[i]
            # image[x, y] = array[i]
            image[x, y] = int(red), int(green), int(blue)
            """print("Values for pixel of x: {0} and y: {1}".format(x + 1, y + 1))
            print("RGB values: {0}".format(image[x, y]))  # we get the rgb value for debug purposes
            print("HSV values: {0}".format(array[i]))
            print("\n")"""
            i += 1
            # print(image[x, y])
        pass
    pass
    return image


print("Which sorting algorithm do you want to use?\n")
print("1. Hue sorting (HSV)")
print("2. Brightness - HSP color model (RGB)")
print("3. Red - Simple red sorting (RGB)")

userinput = input("Enter the number: ")

oldimg, oldimgcontent = imgopen("img-input-large.jpg")
size = getsize(oldimg)
width = size[1]
height = size[2]

# We store the pixel values of the original image in an array
pixvalues = getpixels(oldimgcontent, width, height)

# If the user wants HSV sorting we have to convert the values
if userinput == "1":
    pixvalues = rgbtohsv(pixvalues)

sortedvalues = sortarray_firstvalue(pixvalues)

# print(pixvalues)
# print(sortedvalues)

newimg, newimgcontent = imgcreate(width, height)

# Convert the values back from HSV to RGB to write them in the image
if userinput == "1":
    sortedvalues = hsvtorgb(sortedvalues)

sortedimg = writepixels(sortedvalues, newimgcontent, width, height)

# Pixel values are correct, but there's an error on the save process
# because the output image is not right
saveimg(newimg, "img-output.jpg")

print("-- exec time: %s seconds --" % (time.time() - start_time))
