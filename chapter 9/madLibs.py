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
            lit = lit.replace("adjective", ask)
        if "noun" in lit:
            askN = pyip.inputStr('Pick your noun!')
            lit = lit.replace("noun", askN)
        if "verb" in lit:
            askV = pyip.inputStr('Pick your verb!')
            lit = lit.replace("verb", askV)




#def options():


literature('libs.txt')
options()
