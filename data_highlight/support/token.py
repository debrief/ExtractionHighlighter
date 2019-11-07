from .char_array import SingleUsage


class SmallToken:
    def __init__(self, span, text, line_start, chars):
        self.span = span
        self.text = text
        self.line_start = line_start
        self.chars = chars

    def start(self):
        return self.line_start + self.span[0]

    def end(self):
        return self.line_start + self.span[1]


class Token:
    """
    a single token
    """

    def __init__(self, array_of_tokens):
        """
        :param array_of_tokens:  Arrays Of token
        """
        self.children = array_of_tokens

    def token_text(self):
        return self.children[0].text

    def record(self, tool: str, field: str, value: str, units: str = "n/a"):
        """
        Report on the usage of this token
        Args:
            tool(str):  name of the module handling the import
            field(str): what the token is being interpreted as
            value(str): what value the token provided
            units(str): the units of the token
        """
        tool_field = tool + "/" + field
        message = "Value:" + str(value) + " Units:" + str(units)

        for token in self.children:
            start = token.start()
            end = token.end()
            for i in range(start, end):
                usage = SingleUsage(tool_field, message)
                token.chars[i].usages.append(usage)
