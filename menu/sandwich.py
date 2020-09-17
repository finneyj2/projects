import pyinputplus as pyip


def decision():
    responseY = pyip.inputYesNo("Would you like a sandwich?")
    print("test")
    if responseY:
        SandwichBuilder()


def SandwichBuilder():
    breadCost = {'Wheat': '1', 'Sourdough': '3', 'White': '1'}
    proteinCost = {'Ham': '5', 'Chicken': '2', 'Tuna': '4', 'Bacon': '5'}
    cost = 0
    print('What is your preferred sandwich bread?' + str(breadCost))
    response = pyip.inputMenu(['Wheat', 'Sourdough', 'White'])
    if response in breadCost:
        cost+= int(breadCost.get(response))
        print('Your current cost is' + str(cost))

    decision = pyip.inputYesNo('Do you want protein?')
    if decision == 'yes':
        print("Your meat choices are " + str(proteinCost))
        p = pyip.inputMenu(['Ham', 'Chicken', 'Tuna', 'Bacon'])
        if p in proteinCost:
            cost+= int(proteinCost.get(p))
            print('Your current cost is ' + str(cost))

    else:
        print("Okay!")

    decision2 = pyip.inputYesNo('Do you want cheese?')
    if decision2 == 'yes':
        c = pyip.inputMenu(['Swiss', 'Cheddar', 'Mozarella'])
        cost+= 2

    decision3 = pyip.inputYesNo('Do you want mayo?')
    if decision3 == 'Yes':
        print('Your sandwich will cost ' + str(cost))
        print('Have a nice day')
    else:
        print('Your total cost is ' + str(cost))


decision()
