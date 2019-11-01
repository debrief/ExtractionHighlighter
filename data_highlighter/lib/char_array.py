class CharIndex:
    """
    storage structure used to describe the activity on a single character
    """

    def __init__(self, letter):
        self.letter = letter
        self.usages = []

    def __str__(self):
        message = "[" + self.letter + "]"
        for usage in self.usages:
            message += "(T/F:" + usage.toolField + ", msg:" + usage.message + ")"
        return message


class SingleUsage:
    """
    storage of a single activity
    """

    def __init__(self, toolField, message):
        self.toolField = toolField

        self.message = message
