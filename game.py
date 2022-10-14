# Create your Game class logic in here.
from phrase import Phrase
import random

class Game:

    #init game using phrase object
    def __init__(self):
        self.phrases = ['Im going to make him an offer he cant refuse',
                        'Go ahead make my day',
                        'May the Force be with you',
                        'You talking to me?',
                        'Ill be back',
                        'You cant handle the truth', 
                        'I want to play a game']
        self.active_phrase = Phrase(self.phrases[random.randint(0, len(self.phrases) - 1)])
        self.guesses = [' '] #needed so that spaces show in phrase
        self.game_continues = True
        self.missed = 0

    #start the game
    def start(self):
        print("Welcome to the Phrase Hunter - Movie Edition!")
        print("Try to guess the phrase before you run out of guesses.")
        print("You have 5 guesses to guess the phrase.")
        print("You dont have to include punctuation (!, ? etc) in your guesses.")
        print('But Capitals Are Required!')

        self.active_phrase.show_phrase(self.guesses)

        while self.missed != 5 and self.game_continues:
            self.attempt = input("\nGuess a letter of the phrase: ")
            if self.active_phrase.check_Attempt(self.attempt):
                self.guesses.append(self.attempt)
            else: 
                self.missed += 1
                print(f'Incorrect! You have {5 - self.missed} out of 5 guesses left.')
            self.active_phrase.show_phrase(self.guesses)
            if Phrase.check_for_win(self, self.active_phrase.chosenPhrase, self.guesses):
                print('\nYou win!')
                self.game_continues = False
        if self.missed == 5:
            print('\nGame Over!')