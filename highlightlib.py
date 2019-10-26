import  re
import random

def getColor():
    r = lambda: random.randint(0, 255)
    color = '#%02X%02X%02X' % (r(), r(), r())
    return color

def combine(token,*args):
    oneString=""
    for i in args:
        oneString=oneString+token[i]+" ";

    for i in range(1,len(args)):
        token.pop(args[i])
    token[args[0]]=oneString
    return token



class Line:
    record=[]
    token=""
    def __init__(self,text):
        text=re.sub(' +', ' ',text)
        self.text=text

    def updateToken(self,token):
        self.token=token

    def tokens(self):
        return  self.text.split(" ")

    def addRecord(self,*args):
        arr=[]
        for i in args:
            arr.append(i)
        self.record=arr

    def showToken(self):
        return  self.token

    def showRecord(self):
        return self.record

class HighlightedDatafile:
    arraOfColors=[]
    arrayFordata = []
    name=""
    max=0
    def __init__(self,nameOfFile):
        self.nameOfFile=nameOfFile

    def lines(self):
        arr=[]
        arrFile= open(self.nameOfFile,'r')
        for i in arrFile:
            text=i.rsplit("\n")[0]
            objectLine = Line(text)
            arr.append(objectLine)
        return arr
    def addToList(self,obj):
        self.arrayFordata.append(obj)


    def setName(self,name):
        self.name=name
    def show(self):
        for i in self.arrayFordata:
            print(i.showToken())
            print(i.showRecord())


    def create(self):
        file=open("out.txt",'w+')
        for i in self.arrayFordata:
            num=len(i.showRecord())
            if self.max <=num :
                self.max=num


        for i in range(0,self.max):
            self.arraOfColors.append(getColor())


        for i in self.arrayFordata:
            stringBegging=""
            count=0
            arrayOfWords= i.showToken()
            for j in  i.showRecord():
                stringBegging=stringBegging+' <span style="background-color:'+str(self.arraOfColors[count])+'">'+arrayOfWords[int(j)]+' </span>&#160 '
                count=count+1
            count=0
            stringBegging=stringBegging+" <br>"
            file.write(stringBegging+'\n')
            stringBegging=""

        file.close()