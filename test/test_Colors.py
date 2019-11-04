import unittest
from data_highlight.support.color_picker import colorFor, hexColorFor, meanColorFor

class ColorTests(unittest.TestCase):

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

    def test_ColorFor(self):
        colorDict = {}
        color1 = colorFor("aaa", colorDict)
        assert color1 is not None
        self.assertEqual(1, len(colorDict))

        color2 = colorFor("bbb", colorDict)
        assert color2 is not None
        self.assertEqual(2, len(colorDict))
        self.assertNotEqual(color1, color2)

        color3 = colorFor("aaa", colorDict)
        self.assertEqual(2, len(colorDict), "Should not have created new dict entry")
        self.assertEqual(color1, color3)

    def test_HexConversion(self):
        red = (255, 0, 0)
        self.assertEqual("rgba(255,0,0,0.300000)", hexColorFor(red))

    def test_MeanColor(self):
        color1 = (100, 50, 200)
        color2 = (50, 0, 150)
        color3 = (150, 100, 250)

        self.assertEqual((75, 25, 175), meanColorFor((color1, color2)))
        self.assertEqual((100, 50, 200), meanColorFor((color3, color2)))
        self.assertEqual((100, 50, 200), meanColorFor((color1, color2, color3)))


if __name__ == "__main__":
    unittest.main()
