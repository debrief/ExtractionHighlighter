import re


class HashObjectOfToken():
    def __init__(self,name,speed,token):
        self.name=name
        self.speed=speed
        self.token=token

class Letter():
    def __init__(self,char,color,toolTip):
        self.char=char
        self.color=color
        self.toolTip=toolTip

    def __str__(self):
        return "["+self.char+"] "+"["+self.color+"] "+" ["+self.toolTip+"]"

class Line():

    def __init__(self,line):
        self.line=line

    def tokenize(self):
        return self.line.split(" ")




class HighLight():
    mainArrOfChars=[]
    hashRecord={}
    def __init__(self,inputName,nameOfData):
        self.inputName=inputName
        self.nameOfData=nameOfData

    def lines(self):
        arr=[]
        arrFile = open(self.inputName, 'r')
        for i in arrFile:
            text = i.rsplit("\n")[0]
            text = re.sub(' +', ' ', text)
            text=text.strip()
            arr.append(Line(text))
        return  arr




    def record(self,name,miles,token,color):

        hash=self.hashRecord.copy()

        if 'empty' in self.hashRecord:
            smallHash= {}
            smallHash = hash.get('empty').copy()
            smallHash.update({token:{'name':name,
                                     'attr':miles,
                                     'color' :color}})
            hash.update({'empty':smallHash})
        else:
            smallHash={}
            smallHash.update({token:{'name':name,
                                     'attr':miles,
                                     'color':color}
                              })
            hash.update({'empty': smallHash})

        self.hashRecord = hash

        #import  json
        #print(json.dumps(self.hashRecord))

    def create(self,nameOfFile):
        line = self.lines()
        for i in line:
            token = i.tokenize()
            data=self.hashRecord.get('empty')
            for key in data.keys():
                dataFromToken=token[key]
                hashMapOfAttrivutes=data.get(key)

                for letter in dataFromToken:
                    color=hashMapOfAttrivutes.get('color')

                    toolTip=self.nameOfData+', Type:'+hashMapOfAttrivutes.get('name')+', Units:'+hashMapOfAttrivutes.get('attr')+', Value: `'+dataFromToken+'`'
                    letterObjec = Letter(letter,color,toolTip)
                    self.mainArrOfChars.append(letterObjec)

                self.mainArrOfChars.append(Letter('empty','empty','empty'))
            self.mainArrOfChars.append(Letter('nextLine','nextLine','nextLine'))

        self.runMainCharArray(nameOfFile)



    def runMainCharArray(self,nameOffile):
        fileout = open(nameOffile,'w+')
        span = ""
        stringtoWrite = ""
        for index in range(0, len(self.mainArrOfChars) - 1):
            print(self.mainArrOfChars[index])
            if self.mainArrOfChars[index].char == 'empty':
                if self.mainArrOfChars[index-1].color ==  self.mainArrOfChars[index+1].color:
                    createSpan='<span title = "'+self.mainArrOfChars[index-1].toolTip+'"  style="background-color: '+self.mainArrOfChars[index-1].color+'"> '+span+' </span>'
                else:
                    createSpan = '<span title = "' + self.mainArrOfChars[
                        index - 1].toolTip + '"  style="background-color: ' + self.mainArrOfChars[
                                     index - 1].color + '"> ' + span + '</span>'

                stringtoWrite = stringtoWrite +createSpan + ' '
                span = ""

            elif self.mainArrOfChars[index].char == 'nextLine':
                fileout.write(stringtoWrite + ' <br> <br> \n')
                stringtoWrite = ""
            else:
                span = span + self.mainArrOfChars[index].char
        fileout.write(stringtoWrite + ' <br> <br> \n')

        fileout.close()