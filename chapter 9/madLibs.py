from pathlib import Path
import pyinputplus as pyip
def literature(file):
    madL = open(file)
    content = madL.read()
    madL.close()
    ask = pyip.inputStr('Would you like to play madLibs?')
    if ask == 'yes':
        p = Path('new_Libs.txt')
        p.write_text(content)
        options(file)

def options(file):
    with open(file) as f:
        if 'adjective' in f.read():
            print('found')




#def options():


literature('libs.txt')
options('libs.txt')
