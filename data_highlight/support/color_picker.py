import random
import colorsys


def color_for(hash_code, color_dict):
    # do we have it already?
    if hash_code in color_dict:
        # yes, job done
        return color_dict[hash_code]
    else:
        # no, generate one
        hue = random.random()
        sat = random.random()
        rgb = colorsys.hsv_to_rgb(hue, sat, 0.9)
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        new_col = (r, g, b)
        # store the new color
        color_dict[hash_code] = new_col
        return new_col


# convert a 3-element rgb structure to a HTML color definition
def hex_color_for(rgb):
    opacity_shade = 0.3
    return 'rgba(%d,%d,%d,%f)' % (rgb[0], rgb[1], rgb[2], opacity_shade)


# find the mean of the provided colors
def mean_color_for(color_arr):
    r = 0
    g = 0
    b = 0
    for color in color_arr:
        r += color[0]
        g += color[1]
        b += color[2]

    arr_len = len(color_arr)
    return int(r / arr_len), int(g / arr_len), int(b / arr_len)
