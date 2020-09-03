import pyinputplus as pyip


def decision():
    responseY = pyip.inputYesNo("Would you like a sandwich?")
    print("test")
    if responseY:
        SandwichBuilder()


def SandwichBuilder():
    breadCost = {'Wheat': 5, 'Sourdough': 6, 'White': 7}
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

    decision3 = pyipYesNo('Do you want mayo?')

decision()
