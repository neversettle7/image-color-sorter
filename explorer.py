from PIL import Image

class Explorer:
    """
    This class operates as file explorer (opening, saving, etc.)
    """
    def __init__(self):
        #print("~~ Explorer started ~~")
        return

    @staticmethod
    def imgopen(filename):
        """
        This function opens an image file
        :param filename: the name of the input image file
        """
        img = Image.open(filename)
        loadedimg = img.load()
        return img, loadedimg

    @staticmethod
    def imgcreate(width, height):
        """
        This function creates a new image file - IT IS NOT SAVING IT
        :param height: height of the image
        :param width: width of the image
        """
        img = Image.new("RGB", (width, height))
        newloaded = img.load()
        return img, newloaded

    @staticmethod
    def saveimg(image, filename):
        """This function saves the image file on the disk

        VERY IMPORTANT : do NOT disable delete the subsampling = 0 setting,
        otherwise any outputted jpg file will be red-shifted

        :param image: the image content
        :param filename: the name of the output image to be saved

        """
        image.save(filename, subsampling=0)
        return
