from highlib import  HighLight


high=HighLight("file.txt",'RomanFile')



high.record("Date", "ToolTip", 0,'yellow')
high.record("Venicle", "n/a", 1,'blue')
high.record("Venicle", "n/a", 2,'blue')
high.record("Speed", 'mp/a', 3,'white')
high.record("Speed", 'mp/a', 4,'green')






high.create('out.html')





















#from highlightlib import  HighlightedDatafile
#from highlightlib import  combine

#test =  HighlightedDatafile("file.txt")

#lines = test.lines()

#myName = "Date Extractor"
#test.setName(myName)

#for line in lines:
#    toks = line.tokens()


#    if (toks[0] == "//"):
#        toks = combine(toks, 2, 3)
#        line.addRecord(0,1,2,3)
#        line.cover(0,[1,2,3])
#        line.updateToken(toks)
#        test.addToList(line)

#    else:
#        line.addRecord(0,1,2,4,5,6)
#        line.updateToken(toks)
#        test.addToList(line)


#test.create()
#test.show()

