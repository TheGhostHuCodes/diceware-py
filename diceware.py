import argparse
import random

wordlist = open("diceware.wordlist", 'r').readlines()
wordlist = wordlist[2:7778]
dictionary = {}
for line in wordlist:
    entry = line.strip().split("\t")
    dictionary[int(entry[0])] = entry[1]

def get_word(key):
    return dictionary[key]

def get_key():
    key = ""
    for i in range(5):
        key += str(random.randint(1,6))
    return int(key)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-n', action="store", dest="words", type=int)

    args = parser.parse_args()
    passphrase = []
    for i in range(args.words):
        passphrase.append(get_word(get_key()))
    print(" ".join(passphrase))
