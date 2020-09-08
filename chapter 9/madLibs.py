from pathlib import Path
import pyinputplus as pyip
def literature(file):
    madL = open(file)
    content = madL.read()
    madL.close()
    ask = pyip.inputStr('Would you like to play madLibs?')
    if ask == 'yes':
        lit = " "
        with open(file, 'r') as file:
            for line in file:
                lit += str(line).rstrip("\n")+" "
    return lit


def options():
    lit = literature('libs.txt')
    for line in lit:
        if "adjective" in lit:
            ask = pyip.inputStr('Pick your adjective!')
            lit.replace("adjective", ask)
            print(lit)
        else:
            print("Not found")




#def options():


literature('libs.txt')
options()
