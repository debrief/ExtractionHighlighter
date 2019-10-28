import random

from highlightlib import  HighlightedDatafile
from highlightlib import  Line
from highlightlib import  combine
test =  HighlightedDatafile("file.txt")




lines = test.lines()

myName = "Date Extractor"
test.setName(myName)
for line in lines:
    toks = line.tokens()

    if (toks[0] == "//"):
        toks = combine(toks, 2, 3)
        line.addRecord(0,1,2,3)
        line.cover(0,[1,2])
        line.updateToken(toks)
        test.addToList(line)

    else:
        toks = combine(toks, 1, 2)
        line.addRecord(0,1, 3,4,5)
        line.updateToken(toks)
        test.addToList(line)


test.create()
#test.show()

