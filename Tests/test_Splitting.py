import os, sys
import unittest
from data_highlighter.highlighter import  HighlightedFile

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
TEST_FILE = os.path.join(dir_path, "reptest1.rep")
ERROR_TEST_FILE = os.path.join(dir_path, "reptest2.rep")

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

    def test_SplitLines(self):
        #NORMAL FILE
        dataFile = HighlightedFile('data_highlighter/file.txt')

        # get the set of self-describing lines
        lines = dataFile.lines()

        for thisLine in lines:
            tokens = thisLine.tokens()

   
if __name__ == "__main__":
    unittest.main()
