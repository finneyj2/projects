from pathlib import Path
import pyinputplus as pyip, re

def search():
    p = Path('C:/Users/jahli/Practice/chapter 9')
    txtList = list(p.glob('*.txt'))
    txtlistStr = str(txtList)
    ask = pyip.inputStr("What file are you looking for?")
    for x in txtList:
        x.read_text()
        mo = re.search(ask, txtlistStr)
        if mo.group() != null:
            print("Found")
        else:
            "Not found."

search()
