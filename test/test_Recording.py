import os
import unittest
from data_highlight.highlighter import HighlightedFile

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
TEST_FILE = os.path.join(dir_path, "reptest1.rep")
ERROR_TEST_FILE = os.path.join(dir_path, "reptest2.rep")

DATA_FILE = 'files/file.txt'


class UsageRecordingTests(unittest.TestCase):

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

    def test_CreateChars(self):
        dataFile = HighlightedFile(DATA_FILE)

        # get the set of self-describing lines
        lines = dataFile.lines()

        chars = dataFile.chars_debug()
        assert chars is not None

        self.assertEqual(323, len(chars))

        self.assertEqual("9", chars[0].letter)
        self.assertEqual("5", chars[1].letter)

        usages = chars[0].usages
        self.assertTrue(usages is not None, "usages should be declared")
        self.assertEqual(0, len(usages), "usages should start empty")

    def test_RecordTokens(self):
        dataFile = HighlightedFile(DATA_FILE)

        # get the set of self-describing lines
        lines = dataFile.lines()

        firstLine = lines[0]
        assert firstLine is not None

        tokens = firstLine.tokens()
        self.assertEqual(7, len(tokens))

        tool = "TOOL"
        field = "FIELD"
        value = "VALUE"
        units = "UNITS"

        tokens[0].record(tool, field, value, units)

        chars = dataFile.chars_debug()
        assert chars is not None

        first_entry = chars[0]
        self.assertEqual("9", first_entry.letter)
        self.assertEqual(1, len(first_entry.usages))

        first_usage = first_entry.usages[0]
        self.assertTrue(first_usage is not None, "should have a usage")
        self.assertEqual("TOOL/FIELD", first_usage.tool_field)
        self.assertEqual("Value:VALUE Units:UNITS", first_usage.message)

        # make another recordd
        firstLine.record(field, value)
        self.assertEqual(2, len(first_entry.usages))
        second_usage = first_entry.usages[1]
        self.assertTrue(second_usage is not None, "should have a usage")
        self.assertEqual("FIELD", second_usage.tool_field)
        self.assertEqual("VALUE", second_usage.message)

        print(first_entry)
        dataFile.export("test_out.html")


if __name__ == "__main__":
    unittest.main()
