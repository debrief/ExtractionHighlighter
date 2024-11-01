import random
import colorsys


def color_for(hash_code, color_dict, total_colors):
    """
    Get a color for a specific 'hash code' by either taking one we've already recorded for this hash code,
    or generating a new one at regular intervals in the HSV color model.
    """
    # do we have it already?
    if hash_code in color_dict:
        # yes, job done
        return color_dict[hash_code]
    else:
        # no, generate one
        hue = (len(color_dict) / total_colors) % 1.0
        sat = 0.9
        val = 0.9
        rgb = colorsys.hsv_to_rgb(hue, sat, val)
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        new_col = (r, g, b)
        # store the new color
        color_dict[hash_code] = new_col
        return new_col


def hex_color_for(rgb):
    """
    Convert a 3-element rgb structure to a HTML color definition
    """
    opacity_shade = 0.3
    return "rgba(%d,%d,%d,%f)" % (rgb[0], rgb[1], rgb[2], opacity_shade)


def mean_color_for(color_arr):
    """
    find the mean of the provided colors

    Args:
        color_arr: three-element list of R, G and B components of color
    """
    r = 0
    g = 0
    b = 0
    for color in color_arr:
        r += color[0]
        g += color[1]
        b += color[2]

    arr_len = len(color_arr)
    return int(r / arr_len), int(g / arr_len), int(b / arr_len)
