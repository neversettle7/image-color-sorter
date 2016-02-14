# The time library is needed to measure execution time
# PIL library to manipulate images
# colorsys library to manipulate colors
# operator library to sort the values of the array in the fastest way
from PIL import Image
import sys
import time
from sorter import *

start_time = time.time()


def imgopen(filename):
    """This function opens an image file"""
    img = Image.open(filename)
    loadedimg = img.load()
    return img, loadedimg


def imgcreate(width, height):
    """This function creates a new image file - IT IS NOT SAVING IT"""
    img = Image.new("RGB", (width, height))
    newloaded = img.load()
    return img, newloaded


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
    return size, width, height


def getpixels(image, width, height):
    """This function gets the pixels of the image and stores them in an array"""
    array = []
    """print("--------------------------\n"
          "----- ORIGINAL IMAGE -----\n"
          "--------------------------\n")"""
    for y in range(0, height):
        for x in range(0, width):
            # red, green, blue = (image[x, y])
            array.append(image[x, y])
            """print("Values for pixel of x: {0} and y: {1}".format(x + 1, y + 1))
            print("RGB values: {0}".format(image[x, y]))  # we get the rgb value for debug purposes
            print("HSV values: {0}".format(hsvcolors))
            print("\n")"""
            pass
    pass
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


def run(fileinput, userchoice):
    """
    :param fileinput:
    :param userchoice:
    :return:
    """

    sorter = Sorter()

    print("\nExecuting {0} algorithm\n".format(userchoice))
    # Open the file, get the content and the size
    oldimg, oldimgcontent = imgopen(fileinput)
    size = getsize(oldimg)
    width = size[1]
    height = size[2]

    # We store the pixel values of the original image in an array
    pixvalues = getpixels(oldimgcontent, width, height)

    algostarttime = time.time()

    if userchoice == "hsp":
        sortedvalues = sorter.sort_hsp(pixvalues)
    # HSL sorting - We have to convert the values from RGB to HSL and then sort
    if userchoice == "hsl":
        pixvalues = sorter.rgbtohsl(pixvalues)
        sortedvalues = sorter.sort_hsl(pixvalues)
    # HSV sorting - We have to convert the values from RGB to HSV and then sort
    if userchoice == "hsv":
        pixvalues = sorter.rgbtohsv(pixvalues)
        sortedvalues = sorter.sort_hsv(pixvalues)
    if userchoice == "red":
        sortedvalues = sorter.sort_firstvalue(pixvalues)
    if userchoice == "rellum":
        sortedvalues = sorter.sort_rellum(pixvalues)  # print(pixvalues)
        # print(sortedvalues)

    print("--- algorithm execution time: %s s--" % (time.time() - algostarttime))

    newimg, newimgcontent = imgcreate(width, height)

    # Write the content of the image
    writepixels(sortedvalues, newimgcontent, width, height)

    # Save the image
    saveimg(newimg, "output/img-output-" + userchoice + ".jpg")

    print("\nOutput file: output/img-output-" + userchoice + ".jpg\n")
    return


# Let the user insert the filename and the chosen algorithm
print("\n\n-------------------------------------------------")
print("Insert the name of the image you want to sort")
print("PLEASE NOTE: the image should be in the \"input\" folder.")
print("Insert the name WITHOUT the folder path (example: image.jpg)\n")
fileinput = input("Leave blank if you want to use the default image (img-input-small.jpg): ")
if fileinput == "":
    fileinput = "img-input-small.jpg"
fileinput = "input/" + fileinput
print("\nWhich sorting algorithm do you want to use?\n")
print("1. Hue sorting (HSV)")
print("2. Brightness - HSP color model (RGB)")
print("3. Relative luminance")
print("4. Red - Simple red sorting (RGB)")
print("5. HSL")
print("0. All of the available algorithms")

algo = {'1': 'hsv', '2': 'hsp', '3': 'rellum', '4': 'red', '5': 'hsl'}
userinput = input("Select the algorithm: ")
if userinput in algo:
    userchoice = algo[userinput]
    run(fileinput, userchoice)
elif userinput == "0":
    for x in range(1, len(algo) + 1):
        userchoice = algo[str(x)]
        run(fileinput, userchoice)
        pass
else:
    print("Number not recognised. Exiting program.")
    sys.exit()

print("-- total exec time: %s seconds --" % (time.time() - start_time))