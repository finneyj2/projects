from pathlib import Path
from PyDictionary import PyDictionary
dict = PyDictionary()

def literature(file):
    madL = open(file)
    content = madL.read()
    madL.close()
    with open(file) as f:
        if 'adjective' in f.read():
            print('found')
            p = Path('new_Libs.txt')
            p.write_text(content)



#def options():


literature('libs.txt')
