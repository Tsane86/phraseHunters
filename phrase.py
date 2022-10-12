# Create your Phrase class logic here.
# Create Phrase class

import random

class Phrase():
    # create an init method that initialises a phrase object
    def __init__(self):
        self.phrases = ['Frankly, my dear, I dont give a damn',
                        'Toto, Ive a feeling were not in Kansas anymore',
                        'Im going to make him an offer he cant refuse',
                        'Go ahead make my day', 
                        'May the Force be with you', 
                        'You talking to me?', 
                        'Ill be back',
                        'You cant handle the truth', 'I want to play a game']
        self.chosenPhrase = self.phrases[random.randint(0, len(self.phrases)-1)]

    def show_phrase(self, attempts):
        for letter in self.chosenPhrase:
            print(f'{letter}', end=' ') if letter in attempts else print('_', end=' ')
    
    def check_Attempt(self, attempt):
        return attempt in self.chosenPhrase

    def check_for_win(self, chosenPhrase, attempts):
        return set(chosenPhrase) == set(attempts)


#p1 = Phrase()
#print(p1.chosenPhrase)
#print(p1.lettersInChosenPhrase)
#print(p1.check_Attempt('a'))
#print(p1.show_phrase(['a', ' ']))
#print(p1.check_for_win('Ill be back'))
