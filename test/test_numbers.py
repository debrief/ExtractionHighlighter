import os
import unittest
from data_highlight.highlighter import  HighlightedFile

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
TEST_FILE = os.path.join(dir_path, "reptest1.rep")
ERROR_TEST_FILE = os.path.join(dir_path, "reptest2.rep")


DATA_FILE = 'data_highlight/file.txt'

class SimpleTest(unittest.TestCase):
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

    def test_number_of_lines(self):

        dataFile = HighlightedFile('data_highlight/file.txt',2)

        # get the set of self-describing lines
        lines = dataFile.lines()

        chars = dataFile.charsDebug()
        self.assertEqual(88, len(chars))
        self.assertEqual(2, len(lines))

        usages = chars[0].usages
        self.assertTrue(usages is not None, "usages should be declared")

    def test_negative_number_of_lines(self):

        with self.assertRaises(SystemExit) as cm:
            dataFile = HighlightedFile('data_highlight/file.txt', -5)
            lines = dataFile.lines()

        self.assertEqual(cm.exception.code, 1)


if __name__ == "__main__":
    unittest.main()