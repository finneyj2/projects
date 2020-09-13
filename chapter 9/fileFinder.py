from pathlib import Path

def search():
    p = Path('C:/Users/jahli/Practice/chapter 9')
    txtList = list(p.glob('*.txt'))
    for x in txtList:
        x.read_text()
