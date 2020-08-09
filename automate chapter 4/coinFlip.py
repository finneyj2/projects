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
    streak(currentStreak)

def streak(currentStreak):
    count = 0
    current_Streak_Len = len(currentStreak)
    for coin in range(0, current_Streak_Len - 1):
        numberOfStreaks = 0
        currentCoin = currentStreak[coin]
        if currentCoin == 0:
            count+=1
            if currentCoin != currentStreak[coin + 1]:
                count = 0
            elif currentCoin == currentStreak[coin + 1]:
                count+=1
                if count == 6:
                    numberOfStreaks+=1
        elif currentCoin == 1:
            count+=1
            if currentCoin != currentStreak[coin + 1]:
                count = 0
            elif currentCoin == currentStreak[coin + 1]:
                count+=1
                if count == 6:
                    numberOfStreaks+=1
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))
    return numberOfStreaks

run()
