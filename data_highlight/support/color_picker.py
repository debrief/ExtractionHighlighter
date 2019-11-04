import random
import colorsys

def colorFor(hashCode,colorDict):
    # do we have it already?
    if hashCode in colorDict:
        # yes, job done
        return colorDict[hashCode]
    else:
        # no, generate one
        hue = random.random()
        sat = random.random()
        rgb = colorsys.hsv_to_rgb(hue, sat, 0.9)
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        newCol = (r, g, b)
        # store the new color
        colorDict[hashCode] = newCol
        return newCol


# convert a 3-element rgb structure to a HTML color definition
def hexColorFor(rgb):
    opacityShade = 0.3
    return 'rgba(%d,%d,%d,%f)' % (rgb[0], rgb[1], rgb[2], opacityShade)


# find the mean of the provided colors
def meanColorFor(colorArr):
    r = 0
    g = 0
    b = 0
    for color in colorArr:
        r += color[0]
        g += color[1]
        b += color[2]

    arrLen = len(colorArr)
    return (int(r / arrLen), int(g / arrLen), int(b / arrLen))
