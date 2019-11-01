from .char_array import  SingleUsage
class Token():
    """
    a single token
    """

    def __init__(self, span, text, lineStart, chars):
        self.span = span
        self.text = text
        self.lineStart = lineStart
        self.chars = chars

    def __str__(self):
        return "[(" + str(self.start()) + "-" + str(self.end()) + ")" + ":\"" + self.text + "\"]"

    def start(self):
        return self.lineStart + self.span[0]

    def end(self):
        return self.lineStart + self.span[1]

    def record(self, tool: str, field: str, value: str, units: str = "n/a"):
        """
        Report on the usage of this token
        Args:
            tool(str):  name of the module handling the import
            field(str): what the token is being interpreted as
            value(str): what value the token provided
            units(str): the units of the token
        """
        toolField = tool + "/" + field
        message = "Value:" + str(value) + " Units:" + str(units)
        for i in range(self.start(), self.end()):
            usage = SingleUsage(toolField, message)
            self.chars[i].usages.append(usage)
