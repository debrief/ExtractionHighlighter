from .support.char_array import CharIndex
from .support.line import Line
from .support.color_picker import hexColorFor, meanColorFor, colorFor


class HighlightedFile:
    """
    class that can load/tokenize a datafile, record changes to the file,
    then export a highlighted version of the file that indicates extraction
    """

    def __init__(self, filename: str, number_of_lines=None):
        """
        Constructor for this object
        Args:
            filename (str): The name of the file to be parsed/reported upon
            number_of_lines(int) Number of lines that should be showed
                   to the output, or all line if omitted
        """
        self.filename = filename
        self.dict_color = {}
        self.number_of_lines = number_of_lines

    #
    def charsDebug(self):
        """
        Debug method, to check contents of chars
        """
        return self.chars

    def lines(self):
        """
        slice the file into single lines
        """
        if self.number_of_lines is None:
            return self.not_limited_lines()
        elif self.number_of_lines <= 0:
            print("Non-positive number of lines. Please provide positive number")
            exit(1)
        else:
            return self.limited_lines()

    def export(self, filename: str):
        """
        Provide highlighter summary for this file
        Args:
            filename (str): The name of the destination for the HTML output
        """
        fOut = open(filename, "w")

        lastHash = ""

        for char_index in self.chars:
            letter = char_index.letter
            thisHash = ""
            thisMessage = ""
            colors = []
            for usage in char_index.usages:
                thisHash += usage.tool_field
                needsNewLine = thisMessage != ""
                colors.append(colorFor(usage.tool_field, self.dict_color))
                if needsNewLine:
                    thisMessage += " // "
                thisMessage += usage.tool_field + ", " + usage.message

            # do we have anything to shade?
            if thisHash != "":
                # generate/retrieve a color for this hash
                new_color = meanColorFor(colors)
                hex_color = hexColorFor(new_color)

                # are we already in hash?
                if lastHash != "":
                    # is it the different to this one?
                    if lastHash != thisHash:
                        # ok, close the span
                        fOut.write("</span>")

                        # start a new span
                        fOut.write("<span title='" + thisMessage + "' style=\"background-color:" + hex_color + "\"a>")
                else:
                    fOut.write("<span title='" + thisMessage + "' style=\"background-color:" + hex_color + "\">")
            elif lastHash != "":
                fOut.write("</span>")

            # just check if it's newline
            if letter == "\n":
                fOut.write("<br>")
            else:
                fOut.write(letter)

            lastHash = thisHash

        if lastHash != "":
            fOut.write("</span>")

        fOut.close()

    def limited_lines(self):
        """
            If  numberOfLines were limited
        :return:
        """

        with open(self.filename, 'r') as file:
            sample_lines = file.read()

        str_lines = sample_lines.splitlines()

        str_lines = str_lines[0:self.number_of_lines]
        str_to_char = '\n'.join(str(e) for e in str_lines)

        lines = self.fill_char_array(str_to_char, str_lines)
        return lines

    def not_limited_lines(self):
        with open(self.filename, 'r') as file:
            sample_lines = file.read()

        str_lines = sample_lines.splitlines()
        lines = self.fill_char_array(sample_lines, str_lines)
        return lines

    def fill_char_array(self, string_to_char, array_to_lines):
        line_ctr = 0
        lines = []
        # make the char index the correct length
        self.chars = [None] * len(string_to_char)

        # initialise the char index
        charCtr = 0
        for char in string_to_char:
            # put letter into a struct
            charInd = CharIndex(char)
            self.chars[charCtr] = charInd
            charCtr += 1

        for this_line in array_to_lines:
            line_length = len(this_line)
            newL = Line(str(line_ctr), str(line_ctr + line_length), this_line, self.chars)
            lines.append(newL)
            line_ctr += line_length + 1

        return lines
