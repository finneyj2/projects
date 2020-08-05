import random
currentStreak = []


def cointoss():
    for experimentNumber in range(10000):
        cointoss = random.randint(0,1)
        currentStreak.append(cointoss)
        # Code that checks if there is a streak of 6 heads or tails in a row.
    return currentStreak

def run():
    result = cointoss()
    streak()

def streak():
    count = 0
    numberOfStreaks = 0
    for x in currentStreak:
        if x == 0:
            count+= 1
            if count == 6:
                numberOfStreaks+= 1
                return numberOfStreaks

        if x == 1:
            count+= 1
            if count == 6:
                numberOfStreaks+= 1
                return numberOfStreaks



run()
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
