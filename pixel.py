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
    print(img)
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
            hsvcolors = colorsys.rgb_to_hsv(red, green, blue)
            array.append(hsvcolors)
            """print("Values for pixel of x: {0} and y: {1}".format(x + 1, y + 1))
            print("RGB values: {0}".format(image[x, y]))  # we get the rgb value for debug purposes
            print("HSV values: {0}".format(hsvcolors))
            print("\n")"""
            pass
    pass
    return array


def sortarray(array):
    """This function just sorts the array
    """
    array.sort()
    return (array)


def writepixels(array, image, width, height):
    """This function writes the pixel values in the output image"""
    """print("------------------------\n"
          "----- EDITED IMAGE -----\n"
          "------------------------\n")"""
    i = 0
    for y in range(0, height):
        for x in range(0, width):
            # Write the new color
            hue, saturation, value = array[i]
            rgbvalues = colorsys.hsv_to_rgb(hue, saturation, value)
            red, green, blue = rgbvalues
            image[x, y] = int(red), int(green), int(blue)
            """print("Values for pixel of x: {0} and y: {1}".format(x + 1, y + 1))
            print("RGB values: {0}".format(image[x, y]))  # we get the rgb value for debug purposes
            print("HSV values: {0}".format(array[i]))
            print("\n")"""
            i += 1
            #print(image[x, y])
        pass
    pass
    return (image)


oldimg, oldimgcontent = imgopen("oldimg.jpg")
size = getsize(oldimg)
width = size[1]
height = size[2]

# We store the pixel values of the original image in an array
pixvalues = getpixels(oldimgcontent, width, height)

sortedvalues = sortarray(pixvalues)

#print(pixvalues)
#print(sortedvalues)

newimg, newimgcontent = imgcreate(width, height)

sortedimg = writepixels(sortedvalues, newimgcontent, width, height)

# Pixel values are correct, but there's an error on the save process
# because the output image is not right
saveimg(newimg, "newimg.jpg")

print("\n-- exec time: %s seconds --" % (time.time() - start_time))
