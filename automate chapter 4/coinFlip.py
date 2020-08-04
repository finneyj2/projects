import random
tossedCoins = []


def cointoss(tossedCoins):
    for experimentNumber in range(10000):
        cointoss = random.randint(0,1)
        tossedCoins.append(cointoss)
        # Code that checks if there is a streak of 6 heads or tails in a row.
    return tossedCoins

def run():
    result = cointoss(tossedCoins)
    streak(tossedCoins)

def streak(tossedCoins):
    streak_Count = 0
    numberOfStreaks = 0
    for x in currentStreak:
        if x == 0 and streak_Count < 6
            streak_Count+= 1
            if streak_Count == 6:
                numberOfStreaks+= 1

        else:
            streak_Count += 1
            if x == 0:
                streak_Count = 0
            elif streak_Count == 6:
                numberOfStreaks+= 1
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))
    return tossedCoins


run()
