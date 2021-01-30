from count_syllables import count_syllables
from nltk.corpus import cmudict
import PyInputPlus as pyip
from random_word import RandomWords
import sys

def main():
    quest = pyip.inputNum("How many words do you want to test?")
    if quest == ' ':
        print("Please enter a number.")
    if quest > 0:
        load_dict_and_search(dict_online, quest)
    else:
        sys.exit("Number not given")


def test_count(counted_syllables, dictionary):
"""Test function that compares syllable count with a dictionary"""
    

def load_dict_and_search(dict_online, word_num):
    """loads dictionary for program"""
    with open(dict_online) as in_file:
        loaded_txt = in_file.read().strip().split('\n')
        str_load = " "
        for x in loaded_txt:
            str_load += str(x).rstrip("\n")+ " "
