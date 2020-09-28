from pathlib import Path
import pyinputplus as pyip, re

def search():
    p = Path('C:/Users/jahli/Practice/chapter 9')
    txtList = list(p.glob('*.txt'))
    txtlistStr = str(txtList)
    print(txtlistStr)
    ask = pyip.inputStr("What file are you looking for?")
    for x in txtlistStr:
        x.read_text()
        print(x)
        mo = re.search(ask, txtlistStr)
        k = mo.group()
        if  k != None:
            print("Found")
        else:
            "Not found."

search()
