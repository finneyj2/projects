import random
numberOfStreaks = 0
currentStreak = []
maintainT = 0
maintainH = 0
def cointoss():
    for experimentNumber in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        cointoss = random.randint(0,1)
        if cointoss == 0:
            return 'H'

        elif cointoss == 1:
            return 'T'
    # Code that checks if there is a streak of 6 heads or tails in a row.

def run():
    result = cointoss()
    print(result)
    currentStreak.append(result)
    streak()

def streak():
    count = 0
    if len(currentStreak) == 0:
        print("Empty list")
        return numberOfStreaks
    else:
        print(currentStreak)
        #for index in currentStreak:
            #if index - 1 == index and count <= 6:
                #count=+ 1
                #if count == 6:
                    #numberOfStreaksStreak =+ 1
                #return numberOfStreaks

run()
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
