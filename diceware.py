import argparse
import random

class Diceware():
    def __init__(self):
        self.wordlist = open("diceware.wordlist", 'r').readlines()[2:7778]
        self.dictionary = {}
        #wordlist = wordlist[2:7778]
        for line in self.wordlist:
            entry = line.strip().split("\t")
            self.dictionary[int(entry[0])] = entry[1]

    def get_word(self, key):
        return self.dictionary[key]

    def get_key(self):
        key = ""
        for i in range(5):
            key += str(random.randint(1,6))
        return int(key)

    def get_passphrase(self, length):
        passphrase = []
        for i in range(length):
            passphrase.append(self.get_word(self.get_key()))
        return passphrase

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-n', action="store", dest="words", type=int)

    args = parser.parse_args()
    diceware = Diceware()
    print(" ".join(diceware.get_passphrase(args.words)))
