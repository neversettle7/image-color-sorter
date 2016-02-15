import colorsys


class Sorter:
    """
    This class is used to sort the values by various algorithms
    """

    def __init__(self):
        #print("~~ Sorter started ~~")
        return

    @staticmethod
    def rgbtohsv(array):
        """
        This function converts RGB values to HSV
        :param array: the array of the values to be converted
        :return: the array of converted values
        """
        arraymod = []
        for x in range(0, len(array)):
            red, green, blue = array[x]
            red, green, blue = [x / 255.0 for x in (red, green, blue)]
            hsvcolors = colorsys.rgb_to_hsv(red, green, blue)
            temparray = [hsvcolors, array[x]]
            arraymod.append(temparray)
            pass
        return arraymod

    @staticmethod
    def hsvtorgb(array):
        """
        This function converts HSV values to RGB
        :param array: the array of values to be converted
        :return: the array of converted values
        """
        arraymod = []
        for x in range(0, len(array)):
            hue, saturation, value = array[x]
            rgbcolors = colorsys.hsv_to_rgb(hue, saturation, value)
            arraymod.append(rgbcolors)
            pass
        return arraymod

    @staticmethod
    def sort_hsv(array):
        """
        This function sorts the HSV values by hue
        :param array: the array to be sorted
        :return: the sorted array
        """
        array.sort()
        arraydef = [x[1] for x in array]
        return arraydef

    @staticmethod
    def rgbtohsl(array):
        """
        This function converts RGB values to HLS
        :param array: the array to be converted
        :return: the converted array
        """
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

    @staticmethod
    def hsltorgb(array):
        """
        This function converts HLS values to RGB
        :param array: the array to be converted
        :return: the converted array
        """
        arraymod = []
        for x in range(0, len(array)):
            hue, saturation, lightness = array[x]
            # Note that the colorsys library uses "hls" to refer to "hsl", instead of the usual name
            rgbcolors = colorsys.hls_to_rgb(hue, saturation, lightness)
            arraymod.append(rgbcolors)
            pass
        return arraymod

    @staticmethod
    def sort_hsl(array):
        """
        This function sorts the array based on the HSL color model and a formula found on stack overflow:
        http://stackoverflow.com/questions/3014402/sorting-a-list-of-colors-in-one-dimension
        lightness * 5 + saturation * 2 + hue
        :param array: the array to be sorted
        :return: sorted array
        """
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

    @staticmethod
    def sort_firstvalue(array):
        """
        This function sorts the array simply based on the first value.
        Example: hue for the HSV format (hue, saturation, value), red for RGB and so on
        :param array: the array to be sorted
        :return: sorted array
        """
        array.sort()
        return array

    @staticmethod
    def sort_hsp(array):
        """
        This function sorts the array based on the HSP color model (RGB) of perceived brightness:
        0.299 * red^2 + 0.587 * green^2 + 0.114 * blue^2
        :param array: array to be sorted
        :return: sorted array
        """
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

    @staticmethod
    def sort_rellum(array):
        """
        This function sorts the array based on the relative luminance (standard for certain colour spaces).
        0.2126 * red + 0.7152 * green + 0.0722 * blue
        It is based on the photometric definition of luminance with the values normalized to 1 or 100
        as a reference white
        :param array: array to be sorted
        :return: sorted array
        """
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
