# Image color sorter

### What does this program do?

Basically, it gets an image as input, then outputs the same image with his pixels sorted by color. There are gonna be more informations about the algorithms used at the end of this page.

### Why did you decide to develop this (in)utility?

I wanted to learn Python development and I just kinda leaned towards this little idea that I had in mind for a long time.

### How do I get this stuff running?

Assuming you don't have Python already installed (especially if you're on windows), go grab it at [Python official site][Python_download].

Go ahead with the installation, then open a prompt window and type
    
    $ python

This will get you in a Python shell. Now type
    
    $ pip install Pillow

This will install [Pillow][Pillow_link] (Python Imaging Library), which is the library I'm currently using to work on images.

Looks like you're set!

Now go to the folder where you downloaded my software using your prompt window/terminal and type:

    $ python pixelsorter.py

Have fun!

### Your code sucks, bro.

Yes, I already know that. It's gonna be full of errors and poor-optimized code, but this is my first Python project, so take it easy.

## Algorithms used

#### Hue sorting
Based on the [HSV color representation][HSV_link] where the color are expressed by cylindrical-coordinates. The three values of HSV are hue, saturation and value. This algorithm sorts the colors by ordering the pixels based on their *hue* values. Read the linked Wikipedia article to get to know more.

#### Perceived brightness - HSP color model
Based on the [HSP color model][HSP_link], which is an alternative to HSV. The red, green and blue values from the RGB model are multiplied by three costants which represent the different degrees to which each of the primary (RGB) colors affects human perception of the overall brightness of a color. The linked article is a very interesting read on the subject.

#### Relative luminance
The [relative luminance][rellum_link] is a value to get the luminance of a color. Again, we get the RGB values and multiply them by three costants. Note that the three constants are, like in the HSP model, based on the luminosity function: the green value is more important because contributes the most to how the intensity is perceived by the human eye (then red and blue).


#### Red scale - RGB model
This is a very simple algorithm (which is not really effective, but I originally wrote it for testing purposes then decided to leave it there as a simple demonstration) sorting the colors based on the first value of the RGB model (red intensity).

[Python_download]: <https://www.python.org/downloads/>
[Pillow_link]: <https://pillow.readthedocs.org/en/3.1.x/>
[HSV_link]: <https://en.wikipedia.org/wiki/HSL_and_HSV>
[HSP_link]: <http://alienryderflex.com/hsp.html>
[rellum_link]: <https://en.wikipedia.org/wiki/Relative_luminance>