#Currency Converter v2
import urllib.request
import json

class GetInfo:
    def __init__(self):
            self.get_curr_info()
	
    def get_curr_info(self):
        baseCurr = input("Enter the symbol for your base currency: \n")
        with urllib.request.urlopen('http://api.fixer.io/latest?base={}'.format(baseCurr)) as url:
            data = url.read()
            print(data.__class__)
            
            dataDict = json.loads(data.decode("utf-8"))  #turns json to python dict
            print(dataDict.__class__)
            
            self.currValDict = dataDict['rates'] #creates dict of key:value pairs from datadict['rates'] key
            print(self.currValDict.__class__)
            print(self.currValDict)

    def get_input(self):
        currChoice = input("What's your desired currency?: \n")
        currAmount = input("And how much would you like to convert?: \n")
        
        print(currCoice)
        print(currCoice.__class__)
        print(currAmunt)
        print(currAmunt.__class__)


class Converter:
    def __init__(self):
            self.convert()

    def convert(self):
        print('convert method working so far')


if __name__ == "__main__":
    GetInfo()
    #Converter()








##        try:
##            temp = open('ex_rate_info.txt', 'r+')
##            print(temp)
##            ex_rate_info.close()
