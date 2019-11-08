import os
import unittest
from re import finditer
from datetime import datetime
from data_highlight.highlighter import HighlightedFile
from data_highlight.support.combine import combine
from data_highlight.highlighter_functionality.export import export


path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
TEST_FILE = os.path.join(dir_path, "reptest1.rep")
NMEA_FILE = os.path.join(dir_path, "NMEA_out.log")

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

    def parse_location(self, lat, lat_hem, lon, long_hem):
        latDegs = float(lat[0:2])
        latMins = float(lat[2:4])
        latSecs = float(lat[4:])
        latDegs = latDegs + latMins / 60 + latSecs / 60 / 60

        lonDegs = float(lon[0:3])
        lonMins = float(lon[3:5])
        lonSecs = float(lon[5:])
        lonDegs = lonDegs + lonMins / 60 + lonSecs / 60 / 60

        if lat_hem == "S":
            latDegs = -1 * latDegs

        if lat_hem == "W":
            lonDegs = -1 * lonDegs

        return (latDegs, lonDegs)



    def test_CombineSingleLine(self):
        dataFile = HighlightedFile(DATA_FILE,1)

        # get the set of self-describing lines
        lines = dataFile.lines()

        tokens = lines[0].tokens()

        self.assertEqual(7, len(tokens))

        dateToken = tokens[0]
        timeToken = tokens[1]
        dateTimeToken = combine(dateToken, timeToken)

        date_time = self.parse_timestamp(dateToken.text(), timeToken.text())

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
        dataFile = HighlightedFile(NMEA_FILE)

        # get the set of self-describing lines
        lines = dataFile.lines()

        nmea_delim = "([^,]+|(?<=,)(?=,)|^(?=,)|(?<=,)$)"

        lat_tok = None
        lat_hem_tok = None
        long_tok = None
        long_hem_tok = None
        date_tok = None
        time_tok = None
        hdg_tok = None
        spd_tok = None

        for line in lines:
            """   print("=====")
            print(time_tok)
            print(hdg_tok)
            print(spd_tok)
            print(lat_tok) """

            tokens = line.tokens(nmea_delim, ",")
            if len(tokens) > 0:

                msg_type = tokens[1].text()
                if msg_type == "DZA":
                    date_tok = tokens[2]
                    time_tok = tokens[3]
                elif msg_type == "VEL":
                    spd_tok = tokens[6]
                elif msg_type == "HDG":
                    hdg_tok = tokens[2]
                elif msg_type == "POS":
                    lat_tok = tokens[3]
                    lat_hem_tok = tokens[4]
                    long_tok = tokens[5]
                    long_hem_tok = tokens[6]

                # do we have all we need?
                if date_tok and spd_tok and hdg_tok and lat_tok:

                    date_time = self.parse_timestamp(date_tok.text(), time_tok.text())

                    loc = self.parse_location(lat_tok.text(), lat_hem_tok.text(), 
                                    long_tok.text(), long_hem_tok.text())
                    spd = float(spd_tok.text())
                    hdg = float(hdg_tok.text())

                    fStr = "{:8.2f}"

                    msg = "Date:" + str(date_time) + ", Loc:()" + fStr.format(loc[0]) + ", " \
                        + fStr.format(loc[1]) + "), Spd:" +  \
                        fStr.format(spd) + ", Hdg:" + fStr.format(hdg)


                    big_token = combine(lat_tok, lat_hem_tok, long_tok, long_hem_tok, spd_tok, hdg_tok, date_tok, time_tok)
                    big_token.record("NMEA Import", "Date:" + str(date_time), msg, "N/A")

                    date_tok = None
                    spd_tok = None
                    hdg_tok = None
                    lat_tok = None

        dataFile.export("nmea.html")

if __name__ == "__main__":
    unittest.main()
