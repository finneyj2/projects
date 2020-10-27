from collections import Counter
import re

"""A Program to find digrams(letter pairings to occur consecutive)"""
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
    di = {"tm":0, "mv":0, "vo":0, "or":0, "rd":0, "dl":0, "le":0}
    for let in di.keys():
        re.findall(str(let), Onl_D)
        if let in Onl_D:
            di[let]+= 1
    return di


main()


    #digram and frequency finder
