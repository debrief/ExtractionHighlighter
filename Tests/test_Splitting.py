import os, sys
import unittest
from data_highlighter.highlighter import  HighlightedFile

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
TEST_FILE = os.path.join(dir_path, "reptest1.rep")
ERROR_TEST_FILE = os.path.join(dir_path, "reptest2.rep")

DATA_FILE = 'data_highlighter/file.txt'

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
        dataFile = HighlightedFile('data_highlighter/file.txt')

        # get the set of self-describing lines
        lines = dataFile.lines()
        
        self.assertEqual(7, len(lines))

    def test_SplitTokens(self):

        dataFile = HighlightedFile('data_highlighter/file.txt')

        # get the set of self-describing lines
        lines = dataFile.lines()

        firstLine = lines[0]
        assert firstLine is not None

        tokens = firstLine.tokens()
        self.assertEqual(7, len(tokens))

        firstToken = tokens[0]
        assert firstToken is not None

        self.assertEqual("951212", firstToken.text)

   
if __name__ == "__main__":
    unittest.main()
