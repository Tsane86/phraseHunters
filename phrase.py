# Create your Phrase class logic here.
# Create Phrase class

import random

class Phrase():
    # create an init method that initialises a phrase object
    def __init__(self, phraseList):
        self.phrases = phraseList
        self.chosenPhrase = self.phrases[random.randint(
            0, len(self.phrases)-1)]

    def show_phrase(self, attempts):
        for letter in self.chosenPhrase:
            print(f'{letter}', end=' ') if letter in attempts else print('_', end=' ')
    
    def check_Attempt(self, attempt):
        return attempt in self.chosenPhrase

    def check_for_win(self, chosenPhrase, attempts):
        return set(chosenPhrase) == set(attempts)
