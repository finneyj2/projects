import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    cointoss = random.randint(0,1)
    if random.randint(0,1) == 0:
        heads = 0
        heads += 1
        if heads == 6 or 6 * experimentNumber:
            numberOfStreaks += 1

    elif random.randint(0,1) == 1:
        tails = 0
        tails += 1
        if tails == 6 or 6 * experimentNumber:
            numberOfStreaks += 1
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
