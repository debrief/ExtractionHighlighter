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
    coverHashMap={}
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

    def cover(self,key,value):
        hash=self.coverHashMap.copy()
        d={key:value}
        hash.update(d)
        self.coverHashMap=hash

    def showHash(self):
        return self.coverHashMap


    def updateHash(self,dict):
        hash=dict.copy()
        self.coverHashMap=hash

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
        file=open("out.html",'w+')
        for i in self.arrayFordata:
            num=len(i.showRecord())
            if self.max <=num :
                self.max=num


        for i in range(0,self.max):
            self.arraOfColors.append(getColor())


        for i in self.arrayFordata:
            size = len(i.showToken())
            hash = i.showHash().copy()
            record = i.showRecord()
            for k, v in hash.items():
                for valueOfArray in v :
                    try:
                        record.remove(valueOfArray)
                    except Exception as e:
                        print(e)
            for j in record:
                if j not in hash :
                    hash.update({j:-1})
            set={'test'}

            for key , value in hash.items():
                if value == -1:
                    set.add(key)
                else:
                    set.add(key)
                    for number in value:
                        set.add(number)
            set.remove('test')

            for numberOf in range(0,size):
                if numberOf not in set:
                    hash.update({numberOf:-2})


            i.updateHash(hash)


        for i in self.arrayFordata:

            hashMap = i.showHash()
            arrToProcess = i.showToken()
            count = 0
            string=""
            l = sorted(hashMap.keys())
            for key in l:
                date=hashMap.get(key)
                if date != -1 and date != -2:
                    bigSente=arrToProcess[key]
                    stringToReady='<span style="background-color:'+self.arraOfColors[count]+'">'+str(bigSente)+'&#160 '
                    for valuesInSmallArray in date:
                        count = count + 1
                        smallString='<mark style="opacity : 0.75;font-size:12.5px;background-color:'+self.arraOfColors[count]+'" >'+arrToProcess[valuesInSmallArray]+'</mark> &#160 '
                        stringToReady=stringToReady+smallString
                    stringToReady=stringToReady+'</span> &#160 '
                    string=string+stringToReady
                elif date == -1 :
                    bigSente=arrToProcess[key]
                    stringToReady='<span style="background-color:'+self.arraOfColors[count]+'">'+str(bigSente)+''
                    stringToReady = stringToReady + '</span> &#160 '
                    string = string + stringToReady
                    count = count + 1
                elif date == -2:
                    bigSente = arrToProcess[key]
                    stringToReady = '<span>' + str(bigSente) + ''
                    stringToReady = stringToReady + '</span> &#160 '
                    string = string + stringToReady

            string=string+" <br> \n"
            print(string)
        #for i in self.arrayFordata:
        #    arrOfcells=i.showRecord()
        #    arrToProcess=i.showToken()
        #    count=0
        #    string=""
        #    for j in arrOfcells:
        #        data=arrToProcess[j]
        #        newdata = ' <span style="background-color:' + str(self.arraOfColors[count]) + '">'+data + ' </span>&#160 '
        #        count=count+1
        ##        arrToProcess[j]=newdata
        #
        #    for j in arrToProcess:
        #        string=string+str(j)
        #
        #
        #    string=string+" <br> "
        #    file.write(string+'\n')

        file.close()