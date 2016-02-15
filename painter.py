class Painter:
    """
    The painter class is assigned to getting size and pixel values from the input-image.
    Then it writes the pixel on the new image.
    """

    def __init__(self):
        #print("~~~ Filler started ~~~")
        return

    @staticmethod
    def getsize(image):
        """
        This function gets the size of the image
        :param image: the input-image loaded
        """
        width, height = image.size
        size = image.size
        print("\n-- Size of the image is: {0} ({1}x{2})\n".format(size, width, height))
        return size, width, height

    @staticmethod
    def getpixels(image, width, height):
        """This function gets the pixels of the image and stores them in an array
        :param image: the image to be measured
        :param width: width of the image
        :param height: height of the image
        """
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

    @staticmethod
    def writepixels(array, image, width, height):
        """
        This function writes the pixel values in the output image
        :param array: the array that contains the values of the pixel to be written
        :param image: the image that should be written on
        :param width: the width of the image
        :param height: the height of the image
        """
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
