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
            currentStreak.append('H')
            maintainH+= 1
            return maintainH

        elif cointoss == 1:
            currentStreak.append('T')
            maintainT+= 1
            return maintainT
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
