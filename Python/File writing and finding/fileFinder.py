from pathlib import Path
import pyinputplus as pyip, re, glob

def search():
    p = Path('C:/Users/jahli/Projects/Python/File writing and finding')
    txtList = list(glob.glob('*.txt'))
    txtlistStr = str(list(glob.glob('*.txt')))
    comp = re.compile(txtlistStr)
    ask = pyip.inputStr("What file are you looking for?")
    print(txtlistStr)
    for x in txtList:
        mo = comp.match(ask)
        print(mo)
        if  mo is not None:
            print("Found")
        else:
            "Not found."

search()
