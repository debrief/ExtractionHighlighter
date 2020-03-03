from re import finditer
from .token import Token, SmallToken
from .char_array import SingleUsage


class Line:
    """
    a line from the file
    """

    WHITESPACE_DELIM = "\\S+"

    def __init__(self, array_of_tokens):
        """
        Create a new line
        """
        self.children = array_of_tokens
        self.tokens_array = []

    def __repr__(self):
        res = "Line: "
        for child in self.children:
            res += (
                "("
                + str(child.line_start)
                + "+"
                + repr(child.span)
                + ", "
                + child.text
                + ")"
            )
        return res

    def tokens(self, reg_exp=WHITESPACE_DELIM, strip_char=""):
        self.tokens_array = []

        for child in self.children:
            for match in finditer(reg_exp, child.text):
                token_str = match.group()
                # special handling, we may need to strip a leading delimiter
                if strip_char != "":
                    char_index = token_str.find(strip_char)
                    if char_index == 0:
                        token_str = token_str[1:]
                        # and ditch any new whitespace
                    token_str = token_str.strip()

                token = SmallToken(
                    match.span(), token_str, int(child.line_start), child.chars
                )

                # the token object expects an array of tokens,
                # since it could be a composite object
                arr_of_tokens = [token]

                self.tokens_array.append(Token(arr_of_tokens))

        return self.tokens_array

    def record(self, tool, message):
        for child in self.children:
            for i in range(int(child.start()), int(child.end())):
                usage = SingleUsage(tool, message)
                child.chars[i].usages.append(usage)
