"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    '''reads from file and outputs number of words initially
    Attributes
    -------------------
    filepath: str 
              file name for file to be read.  Must be txt file
    '''

    def __init__(self, filepath):
        self.filepath = filepath
        self.wordlist()
        self.countwords(self.words)

    def countwords(self, words):
        'returns count of words in file on initialization'
        file = open(self.filepath, 'r')
        print(f"{len(words)} words read")
        file.close()
        return

    def wordlist(self):
        'creates word list for pulling random'
        file = open(self.filepath, "r")
        self.words = [line.strip('\n') for line in file]
        file.close()
        return

    def random(self):
        'returns a random word from word list supplied'
        return choice(self.words)
