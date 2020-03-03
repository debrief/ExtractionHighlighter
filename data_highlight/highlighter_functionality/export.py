from ..support.color_picker import hex_color_for, mean_color_for, color_for


def export_report(filename, chars, dict_colors, include_key=False):
    """
    To outsource method from high class and make it more readable
    :param filename:  Name of f_out
    :param chars:  pointer of char array
    :param dict_colors: pointer of dict colors
    :return:
    """

    f_out = open(filename, "w")

    last_hash = ""

    for char_index in chars:
        letter = char_index.letter
        this_hash = ""
        this_message = ""
        colors = []
        multi_usages = len(char_index.usages) > 1
        for usage in char_index.usages:
            this_hash += usage.tool_field
            needs_new_line = this_message != ""
            colors.append(color_for(usage.tool_field, dict_colors))
            if needs_new_line:
                this_message += "&#013;"
            if multi_usages:
                this_message += "-"
            this_message += usage.tool_field + ", " + usage.message

        # do we have anything to shade?
        if this_hash != "":
            # generate/retrieve a color for this hash
            new_color = mean_color_for(colors)
            hex_color = hex_color_for(new_color)

            # are we already in hash?
            if last_hash != "":
                # is it the different to this one?
                if last_hash != this_hash:
                    # ok, close the span
                    f_out.write("</span>")

                    # start a new span
                    f_out.write(
                        "<span title='"
                        + this_message
                        + "' style=\"background-color:"
                        + hex_color
                        + '"a>'
                    )
            else:
                f_out.write(
                    "<span title='"
                    + this_message
                    + "' style=\"background-color:"
                    + hex_color
                    + '">'
                )
        elif last_hash != "":
            f_out.write("</span>")

        # just check if it's newline
        if letter == "\n":
            f_out.write("<br>")
        else:
            f_out.write(letter)

        last_hash = this_hash

    if last_hash != "":
        f_out.write("</span>")

    # also provide a key
    if include_key:
        f_out.write("<hr/><h3>Color Key</h3><ul>")
        for key in dict_colors:
            color = dict_colors[key]
            hex_color = hex_color_for(color)
            f_out.write(
                '<li><span style="background-color:'
                + hex_color
                + '">'
                + key
                + "</span></li>"
            )
        f_out.write("</ul>")

    f_out.close()
