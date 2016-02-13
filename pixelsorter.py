# The time library is needed to measure execution time
# PIL library to manipulate images
# colorsys library to manipulate colors
# operator library to sort the values of the array in the fastest way
from PIL import Image
import sys
import colorsys
import time

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


def rgbtohsv(array):
    arraymod = []
    for x in range(0, len(array)):
        red, green, blue = array[x]
        red, green, blue = [x / 255.0 for x in (red, green, blue)]
        hsvcolors = colorsys.rgb_to_hsv(red, green, blue)
        temparray = [hsvcolors, array[x]]
        arraymod.append(temparray)
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


def sort_hsv(array):
    array.sort()
    arraydef = [x[1] for x in array]
    return arraydef


def rgbtohsl(array):
    arraymod = []
    for x in range(0, len(array)):
        red, green, blue = array[x]
        red, green, blue = [x / 255.0 for x in (red, green, blue)]
        # Note that the colorsys library uses "hls" to refer to "hsl", instead of the usual name
        hslcolors = colorsys.rgb_to_hls(red, green, blue)
        temparray = [hslcolors, array[x]]
        arraymod.append(temparray)
        pass
    return arraymod


def hsltorgb(array):
    arraymod = []
    for x in range(0, len(array)):
        hue, saturation, lightness = array[x]
        # Note that the colorsys library uses "hls" to refer to "hsl", instead of the usual name
        rgbcolors = colorsys.hls_to_rgb(hue, saturation, lightness)
        arraymod.append(rgbcolors)
        pass
    return arraymod


def sort_hsl(array):
    """This function sorts the array based on the HSL color model and a formula found on stack overflow:
    http://stackoverflow.com/questions/3014402/sorting-a-list-of-colors-in-one-dimension
    lightness * 5 + saturation * 2 + hue """
    sortarray = []
    for x in range(0, len(array)):
        hue, saturation, lightness = array[x][0]
        value = ((lightness * 5) + (saturation * 2) + hue)
        temparray = [value, array[x][1]]
        sortarray.append(temparray)
        pass
    sortarray.sort()
    finalarray = [x[1] for x in sortarray]
    return finalarray


def sort_firstvalue(array):
    """This function sorts the array simply based on the first value.
       Example: hue for the HSV format (hue, saturation, value), red for RGB and so on"""
    array.sort()
    return array


def sort_hsp(array):
    """This function sorts the array based on the HSP color model (RGB) of perceived brightness:
    0.299 * red^2 + 0.587 * green^2 + 0.114 * blue^2 """
    sortarray = []
    for x in range(0, len(array)):
        red, green, blue = array[x]
        brightness = ((0.299 * (red ** 2)) + (0.587 * (green ** 2)) + (0.114 * (blue ** 2)))
        temparray = [brightness, array[x]]
        sortarray.append(temparray)
        pass
    sortarray.sort()
    finalarray = [x[1] for x in sortarray]
    return finalarray


def sort_rellum(array):
    """This function sorts the array based on the relative luminance (standard for certain colour spaces).
    0.2126 * red + 0.7152 * green + 0.0722 * blue
    It is based on the photometric definition of luminance with the values normalized to 1 or 100
    for a reference white"""
    sortarray = []
    # for x in range(0, len(array)):
    for x in range(0, len(array)):
        red, green, blue = array[x]
        brightness = ((0.2126 * red) + (0.7152 * green) + (0.0722 * blue))
        temparray = [brightness, array[x]]
        sortarray.append(temparray)
        pass
    sortarray.sort()
    finalarray = [x[1] for x in sortarray]
    return finalarray


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
        sortedvalues = sort_hsp(pixvalues)
    # HSL sorting - We have to convert the values from RGB to HSL and then sort
    if userchoice == "hsl":
        pixvalues = rgbtohsl(pixvalues)
        sortedvalues = sort_hsl(pixvalues)
    # HSV sorting - We have to convert the values from RGB to HSV and then sort
    if userchoice == "hsv":
        pixvalues = rgbtohsv(pixvalues)
        sortedvalues = sort_hsv(pixvalues)
    if userchoice == "red":
        sortedvalues = sort_firstvalue(pixvalues)
    if userchoice == "rellum":
        sortedvalues = sort_rellum(pixvalues)  # print(pixvalues)
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
