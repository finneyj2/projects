import pyinputplus as pyip
cost = 0
test = {'a':1, 'b': 2, 'c': 3, 'd': 4}
cat = pyip.inputMenu(['a','b', 'c'])
if cat in test:
    print('found')
    cost+=int(test.get(cat))
    print(cost)
