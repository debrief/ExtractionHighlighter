from re import finditer
from .token import Token, SmallToken
from .char_array import SingleUsage


class Line:
    """
    a line from the file
    """

    WHITESPACE_DELIM = "\\S+"

    def __init__(self, start, end, text, chars):
        self.start = start
        self.end = end
        self.text = text
        self.chars = chars
        self.tokens_array = []

    def tokens(self, reg_exp=WHITESPACE_DELIM, strip_char=""):

        for match in finditer(reg_exp, self.text):
            token_str = match.group()
            # special handling, we may need to strip a leading delimiter
            if strip_char != "":
                char_index = token_str.find(strip_char)
                if char_index == 0:
                    token_str = token_str[1:]
                    # and ditch any new whitespace
                token_str = token_str.strip()
            token = SmallToken(match.span(), token_str, int(self.start), self.chars)
            arr_of_tokens = [token]

            self.tokens_array.append(Token(arr_of_tokens))

        return self.tokens_array

    def record(self, tool, message):
        for i in range(int(self.start), int(self.end)):
            usage = SingleUsage(tool, message)
            self.chars[i].usages.append(usage)
