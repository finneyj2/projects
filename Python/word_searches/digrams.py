from collections import Counter
import re

"""A Program to find digrams(letter pairings to occur consecutive) in dictionaries"""
def main():
    #main function that will trigger the program
    dir = dict("hm.txt")
    x = digram_and_freq_finder(dir)
    print(x)


def dict(Onl_D):
    with open(Onl_D) as in_file:
        loaded_txt = in_file.read().strip().split('\n')
        str_load = " "
        for x in loaded_txt:
            str_load += str(x).rstrip("\n")+ " "
        return str_load



def digram_and_freq_finder(Onl_D):
    di = ["tm", "mv", "vo", "or", "rd", "dl", "le"]
    for let in di:
        words = re.findall(str(let), Onl_D)
        D_count = Counter(words)
    return D_count


main()


    #digram and frequency finder
