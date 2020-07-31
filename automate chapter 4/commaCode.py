words = ['Lincoln', 'eyelashes', 'cabinets','nails']

def take(words):
    if len(words) == 0:
        print("Empty list")
    else:
        words.insert(-1, 'and')
        print(words)

take(words)
