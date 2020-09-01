import pyinputplus as pyip


print('What is your preferred sandwich bread?')
response = pyip.inputMenu(['Wheat', 'Sourdough', 'White'])

decision = pyip.inputYesNo('Do you want protein?')
if decision == 'yes':
    pyip.inputMenu(['Ham', 'Chicken', 'Tuna', 'Bacon'])
else:
    print("Okay!")

decision2 = pyip.inputYesNo('Do you want cheese?')
if decision2 == 'yes':
    pyip.inputMenu(['Swiss', 'Cheddar', 'Mozarella'])
