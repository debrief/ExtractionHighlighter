import unittest
from data_highlight.highlighter import  HighlightedFile

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

        dataFile = HighlightedFile(DATA_FILE,2)

        # get the set of self-describing lines
        lines = dataFile.lines()

        chars = dataFile.charsDebug()
        self.assertEqual(88, len(chars))
        self.assertEqual(2, len(lines))

        usages = chars[0].usages
        self.assertTrue(usages is not None, "usages should be declared")

    def test_all_lines(self):

        dataFile = HighlightedFile(DATA_FILE)

        # get the set of self-describing lines
        lines = dataFile.lines()

        chars = dataFile.charsDebug()
        self.assertEqual(323, len(chars))
        self.assertEqual(7, len(lines))

        usages = chars[0].usages
        self.assertTrue(usages is not None, "usages should be declared")

    def test_negative_number_of_lines(self):

        with self.assertRaises(SystemExit) as cm:
            dataFile = HighlightedFile(DATA_FILE, -5)
            lines = dataFile.lines()
            print(lines) # to avoid unused variable warning

        self.assertEqual(cm.exception.code, 1)

    def test_more_than_lines_number(self):
        dataFile = HighlightedFile(DATA_FILE, 200)

        lines = dataFile.lines()
        self.assertEqual(len(lines), 7)

    def test_zero_number(self):

        with self.assertRaises(SystemExit) as cm:
            dataFile = HighlightedFile(DATA_FILE, 0)
            lines = dataFile.lines()
            print(lines) # to avoid unused variable warning

        self.assertEqual(cm.exception.code, 1)


if __name__ == "__main__":
    unittest.main()