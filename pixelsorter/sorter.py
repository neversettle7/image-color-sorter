import colorsys

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
    return array


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
