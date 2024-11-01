import unittest
from data_highlight.support.color_picker import color_for, hex_color_for, mean_color_for


class ColorTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #####################
    #### color tests ####
    #####################

    def test_ColorFor(self):
        color_dict = {}
        color1 = color_for("aaa", color_dict, 10)
        assert color1 is not None
        self.assertEqual(1, len(color_dict))

        color2 = color_for("bbb", color_dict, 10)
        assert color2 is not None
        self.assertEqual(2, len(color_dict))
        self.assertNotEqual(color1, color2)

        color3 = color_for("aaa", color_dict, 10)
        self.assertEqual(2, len(color_dict), "Should not have created new dict entry")
        self.assertEqual(color1, color3)

    def test_HexConversion(self):
        red = (255, 0, 0)
        self.assertEqual("rgba(255,0,0,0.300000)", hex_color_for(red))

    def test_MeanColor(self):
        color1 = (100, 50, 200)
        color2 = (50, 0, 150)
        color3 = (150, 100, 250)

        self.assertEqual((75, 25, 175), mean_color_for((color1, color2)))
        self.assertEqual((100, 50, 200), mean_color_for((color3, color2)))
        self.assertEqual((100, 50, 200), mean_color_for((color1, color2, color3)))

    def test_UniformColorDistribution(self):
        color_dict = {}
        total_colors = 10
        colors = [color_for(str(i), color_dict, total_colors) for i in range(total_colors)]
        self.assertEqual(total_colors, len(set(colors)), "Colors are not uniformly distributed")

        for i in range(total_colors - 1):
            color1 = colors[i]
            color2 = colors[i + 1]
            contrast = abs(color1[0] - color2[0]) + abs(color1[1] - color2[1]) + abs(color1[2] - color2[2])
            self.assertGreater(contrast, 50, "Adjacent colors do not have sufficient contrast")


if __name__ == "__main__":
    unittest.main()
