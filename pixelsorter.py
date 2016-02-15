# The time library is needed to measure execution time
# PIL library to manipulate images
# colorsys library to manipulate colors
# operator library to sort the values of the array in the fastest way
import sys
import time
from sorter import *
from painter import *
from explorer import *

start_time = time.time()


def run(fileinput, userchoice):
    """
    This is the main function calling all the other methods.
    :param fileinput: the file to be taken as input
    :param userchoice: the algorithm that has to be executed
    :return:
    """

    explorer = Explorer()
    painter = Painter()
    sorter = Sorter()

    print("\nExecuting {0} algorithm\n".format(userchoice))

    # Open the file, get the content and the size
    oldimg, oldimgcontent = explorer.imgopen(fileinput)
    size = painter.getsize(oldimg)
    width = size[1]
    height = size[2]

    # We store the pixel values of the original image in an array
    pixvalues = painter.getpixels(oldimgcontent, width, height)

    algostarttime = time.time()

    if userchoice == "hsp":
        sortedvalues = sorter.sort_hsp(pixvalues)
    # HSL sorting - We have to convert the values from RGB to HSL and then sort
    elif userchoice == "hsl":
        pixvalues = sorter.rgbtohsl(pixvalues)
        sortedvalues = sorter.sort_hsl(pixvalues)
    # HSV sorting - We have to convert the values from RGB to HSV and then sort
    elif userchoice == "hsv":
        pixvalues = sorter.rgbtohsv(pixvalues)
        sortedvalues = sorter.sort_hsv(pixvalues)
    elif userchoice == "red":
        sortedvalues = sorter.sort_firstvalue(pixvalues)
    elif userchoice == "rellum":
        sortedvalues = sorter.sort_rellum(pixvalues)  # print(pixvalues)
        # print(sortedvalues)
    else:
        print("Invalid algorithm choice, the program will now exit.")
        sys.exit()

    print("--- algorithm execution time: %s s--" % (time.time() - algostarttime))

    newimg, newimgcontent = explorer.imgcreate(width, height)

    # Write the content of the image
    painter.writepixels(sortedvalues, newimgcontent, width, height)

    # Save the image
    explorer.saveimg(newimg, "output/img-output-" + userchoice + ".jpg")

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
