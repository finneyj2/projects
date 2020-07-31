

def collatz(number):
    if number % 2 == 0:
        print(number/2)
        return number
    else:
        print(3 * number + 1)
        return number

take = input("Give me a number.")
collatz(int(take))
