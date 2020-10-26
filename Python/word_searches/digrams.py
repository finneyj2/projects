import Collections

"""A Program to find digrams(letter pairings to occur consecutive)"""
def main():
    #main function that will trigger the program
    dict("3esl.txt")
def dict(dictionary):
    with open(file) as in_file:
        loaded_txt = in_file.read().strip().split('\n')
        str_load = " "
        for x in loaded_txt:
            str_load += str(x).rstripe("\n")+ " "
        return str_load



def digram_and_freq_finder():
    di = ["tm", "mv", "vo", "or", "rd", "dl", "le"]
    D_count = Counter()



    #digram and frequency finder
