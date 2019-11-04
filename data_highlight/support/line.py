from re import finditer
from .token import Token
from .char_array import  SingleUsage

class Line():
    """
    a line from the file
    """

    WHITESPACE_DELIM = "\\S+"
    def __init__(self, start, end, text, chars):
        self.start = start
        self.end = end
        self.text = text
        self.chars = chars

    def tokens(self, regExp=WHITESPACE_DELIM, stripChar=""):
        tokens = []
        for match in finditer(regExp, self.text):
            tokenStr = match.group()
            # special handling, we may need to strip a leading delimiter
            if stripChar != "":
                charIndex = tokenStr.find(stripChar)
                if charIndex == 0:
                    tokenStr = tokenStr[1:]
                    # and ditch any new whitespace
                tokenStr = tokenStr.strip()

            tokens.append(Token(match.span(), tokenStr, int(self.start), self.chars))
        return tokens

    def record(self, tool, message):
        for i in range(int(self.start), int(self.end)):
            usage = SingleUsage(tool, message)
            self.chars[i].usages.append(usage)
