import random
numberOfStreaks = 0
currentStreak[]
def cointoss():
    for experimentNumber in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        cointoss = random.randint(0,1)
        if cointoss == 0:
            currentStreak.append('H')
            if heads == 6 or 6 * experimentNumber:
                numberOfStreaks += 1

        elif cointoss == 1:
            currentStreak.append('H')
            if tails == 6 or 6 * experimentNumber:
                numberOfStreaks += 1
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
