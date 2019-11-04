import os, sys
import unittest
from data_highlight.highlighter import  HighlightedFile
from data_highlight.lib.char_array import CharIndex

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
TEST_FILE = os.path.join(dir_path, "reptest1.rep")
ERROR_TEST_FILE = os.path.join(dir_path, "reptest2.rep")

DATA_FILE = 'data_highlight/file.txt'
COMMA_FILE = 'data_highlight/file_comma.txt'

class SimpleTests(unittest.TestCase):

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

    def test_SplitLoadFile(self):
        dataFile = HighlightedFile(DATA_FILE)
        assert dataFile is not None

    def test_SplitLines(self):
        dataFile = HighlightedFile('data_highlight/file.txt')

        # get the set of self-describing lines
        lines = dataFile.lines()
        
        self.assertEqual(7, len(lines))

    def test_SplitCommaTokens(self):

        dataFile = HighlightedFile(COMMA_FILE)

        # get the set of self-describing lines
        lines = dataFile.lines()

        firstLine = lines[0]
        assert firstLine is not None

        #FixMe - this next constant should be declared in class module
        CSV_DELIM = "(?:,\"|^\")(\"\"|[\w\W]*?)(?=\",|\"$)|(?:,(?!\")|^(?!\"))([^,]*?)(?=$|,)|(\r\n|\n)"

        tokens = firstLine.tokens(CSV_DELIM, ",")
        self.assertEqual(7, len(tokens))

        self.assertEqual("951212", tokens[0].text)
        print(tokens[1])

    def test_SplitCharIndex(self):
        c_index = CharIndex("Z")
        print(c_index)

    def test_SplitTokens(self):

        dataFile = HighlightedFile('data_highlight/file.txt')

        # get the set of self-describing lines
        lines = dataFile.lines()

        firstLine = lines[0]
        assert firstLine is not None

        tokens = firstLine.tokens()
        self.assertEqual(7, len(tokens))

        firstToken = tokens[0]
        assert firstToken is not None

        self.assertEqual("951212", tokens[0].text)
        self.assertEqual("050000.000", tokens[1].text)
        self.assertEqual("MONDEO_44", tokens[2].text)
        self.assertEqual("@C", tokens[3].text)
        self.assertEqual("269.7", tokens[4].text)
        self.assertEqual("2.0", tokens[5].text)
        self.assertEqual("10", tokens[6].text)

        secondLine = lines[1]
        assert secondLine is not None

        tokens = secondLine.tokens()
        self.assertEqual(5, len(tokens))

        self.assertEqual("//", tokens[0].text)
        self.assertEqual("EVENT", tokens[1].text)
        self.assertEqual("951212", tokens[2].text)
        self.assertEqual("050300.000", tokens[3].text)
        self.assertEqual("BRAVO", tokens[4].text)


if __name__ == "__main__":
    unittest.main()
