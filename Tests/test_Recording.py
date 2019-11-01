import os, sys
import unittest
from data_highlighter.highlighter import  HighlightedFile

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
TEST_FILE = os.path.join(dir_path, "reptest1.rep")
ERROR_TEST_FILE = os.path.join(dir_path, "reptest2.rep")

DATA_FILE = 'data_highlighter/file.txt'

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

        dataFile = HighlightedFile('data_highlighter/file.txt')

        # get the set of self-describing lines
        lines = dataFile.lines()

        chars = dataFile.charsDebug()
        assert chars is not None

        self.assertEqual(319, len(chars))

        self.assertEqual("9", chars[0].letter)
        self.assertEqual("5", chars[1].letter)

        usages = chars[0].usages
        self.assertTrue(usages is not None, "usages should be declared")
        self.assertEqual(0, len(usages), "usages should start empty")

    def test_RecordTokens(self):

        dataFile = HighlightedFile('data_highlighter/file.txt')

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

        chars = dataFile.charsDebug()
        assert chars is not None

        firstEntry = chars[0]
        self.assertEqual("9", firstEntry.letter)
        self.assertEqual(1, len(firstEntry.usages))

        firstUsage = firstEntry.usages[0]
        self.assertTrue(firstUsage is not None, "should have a usage")
        self.assertEqual("TOOL/FIELD", firstUsage.toolField)
        self.assertEqual("Value:VALUE Units:UNITS", firstUsage.message)

        # make another recordd
        firstLine.record(field, value)
        self.assertEqual(2, len(firstEntry.usages))
        secondUsage = firstEntry.usages[1]
        self.assertTrue(secondUsage is not None, "should have a usage")
        self.assertEqual("FIELD", secondUsage.toolField)
        self.assertEqual("VALUE", secondUsage.message)

        print(firstEntry)


if __name__ == "__main__":
    unittest.main()