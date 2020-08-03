import random
numberOfStreaks = 0
currentStreak = []
maintainT = 0
maintainH = 0
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
    if len(currentStreak) == 0:
        print("Empty list")
        return numberOfStreaks
    else:
        print(currentStreak)
        for index in currentStreak:
            if index - 1 == index and count <= 6:
                count=+ 1
                if count == 6:
                    numberOfStreaksStreak =+ 1
                return numberOfStreaks

run()
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
