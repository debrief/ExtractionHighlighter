from data_highlight.highlighter import HighlightedFile

# NORMAL FILE
dataFile = HighlightedFile('data_highlight/file.txt')

# get the set of self-describing lines
lines = dataFile.lines()

for thisLine in lines:
    tokens = thisLine.tokens()

    # check the type
    firstToken = tokens[0]

    if firstToken.token_text() == "//":
        # event marker
        eventImporter = "Simple Event importer"
        dateToken = tokens[2]
        dateToken.record(eventImporter, "Date", dateToken.token_text())
        timeToken = tokens[3]
        timeToken.record(eventImporter, "Time", timeToken.token_text())
        eventToken = tokens[4]
        eventToken.record(eventImporter, "Event", timeToken.token_text())


        # and the whole=line record
        thisLine.record(eventImporter, "Whole line")

# output to file, display

for i in dataFile.chars_debug():
    print(i)

dataFile.export("out4.html")

# CSV FILE

dataFileCSV = HighlightedFile('data_highlight/file_comma.txt')

# get the set of self-describing lines
lines = dataFileCSV.lines()

CSV_DELIM = "(?:,\"|^\")(\"\"|[\w\W]*?)(?=\",|\"$)|(?:,(?!\")|^(?!\"))([^,]*?)(?=$|,)|(\r\n|\n)"

for thisLine in lines:

    tokens = thisLine.tokens(CSV_DELIM, ",")  # note we specify delimiter

    # check the type
    firstToken = tokens[0]

    if firstToken.token_text()== "//":
        # event marker
        eventImporter = "Simple CSV Event importer"
        dateToken = tokens[2]
        dateToken.record(eventImporter, "Date", dateToken.token_text(), "n/a")
        timeToken = tokens[3]
        timeToken.record(eventImporter, "Time", timeToken.token_text(), "n/a")
        eventToken = tokens[4]
        eventToken.record(eventImporter, "Event", timeToken.token_text(), "n/a")

        # and the whole=line record
        thisLine.record(eventImporter, "Whole line")

# output to file, display
dataFileCSV.export("out5.html")
print("done")
