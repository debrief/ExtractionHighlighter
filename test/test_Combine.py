import os
import unittest
from datetime import datetime
from data_highlight.highlighter import HighlightedFile
from data_highlight.support.combine import combine
from data_highlight.highlighter_functionality.export import export


path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
TEST_FILE = os.path.join(dir_path, "reptest1.rep")

DATA_FILE = 'files/file.txt'


class CombineTokenTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    def setUp(self):
        pass

    def tearDown(self):
        pass

    ####################
    #### file tests ####
    ####################

    
    def parse_timestamp(self, date, time):
        if len(date) == 6:
            formatStr = "%y%m%d"
        else:
            formatStr = "%Y%m%d"

        if len(time) == 6:
            formatStr += "%H%M%S"
        else:
            formatStr += "%H%M%S.%f"

        return datetime.strptime(date + time, formatStr)

    def test_CombineSingleLine(self):
        dataFile = HighlightedFile(DATA_FILE,1)

        # get the set of self-describing lines
        lines = dataFile.lines()

        tokens = lines[0].tokens()

        self.assertEqual(7, len(tokens))

        dateToken = tokens[0]
        timeToken = tokens[1]
        dateTimeToken = combine(dateToken, timeToken)

        date_time = self.parse_timestamp(dateToken.token_text(), timeToken.token_text())

        dateTimeToken.record("TOOL", "Date-Time", date_time, "N/A")

        chars = dataFile.chars_debug()
        assert chars is not None

        ctr = 0
        for char in chars:
            if ctr == 22:
                break
            ctr = ctr + 1

            if ctr > 0 and ctr <= 6:
                usages = char.usages
                self.assertEqual(1, len(usages))
                self.assertEqual("Value:1995-12-12 05:00:00 Units:N/A", usages[0].message)
            elif ctr > 7 and ctr <= 17:
                usages = char.usages
                self.assertEqual(1, len(usages))
                self.assertEqual("Value:1995-12-12 05:00:00 Units:N/A", usages[0].message)

    def test_CombineMultipleLines(self):
        dataFile = HighlightedFile(DATA_FILE,1)

        # get the set of self-describing lines
        lines = dataFile.lines()

        tokens = lines[0].tokens()

        self.assertEqual(7, len(tokens))

        dateToken = tokens[0]
        timeToken = tokens[1]
        dateTimeToken = combine(dateToken, timeToken)

        date_time = self.parse_timestamp(dateToken.token_text(), timeToken.token_text())

        dateTimeToken.record("TOOL", "Date-Time", date_time, "N/A")

        chars = dataFile.chars_debug()
        assert chars is not None

        ctr = 0
        for char in chars:
            if ctr == 22:
                break
            ctr = ctr + 1

            if ctr > 0 and ctr <= 6:
                usages = char.usages
                self.assertEqual(1, len(usages))
                self.assertEqual("Value:1995-12-12 05:00:00 Units:N/A", usages[0].message)
            elif ctr > 7 and ctr <= 17:
                usages = char.usages
                self.assertEqual(1, len(usages))
                self.assertEqual("Value:1995-12-12 05:00:00 Units:N/A", usages[0].message)



if __name__ == "__main__":
    unittest.main()
