# Create your Game class logic in here.
from phrase import Phrase

class Game:

    #init game using phrase object
    def __init__(self):
        self.phrase = Phrase()
        self.attempts = [' '] #needed so that spaces show in phrase
        self.game_continues = True
        self.turns = 5

    #start the game
    def start(self):
        print("Welcome to the Phrase Hunter - Movie Edition!")
        print("Try to guess the phrase before you run out of attempts.")
        print("You have 5 attempts to guess the phrase.")
        print("You dont have to include punctuation (!, ? etc) in your guesses.")
        print('But Capitals Are Required!')

        self.phrase.show_phrase(self.attempts)

        while self.turns != 0 and self.game_continues:
            self.attempt = input("\nGuess a letter of the phrase: ")
            if self.phrase.check_Attempt(self.attempt):
                self.attempts.append(self.attempt)
            else: 
                self.turns -= 1
                print(f'Incorrect! You have {self.turns} attempts left.')
            self.phrase.show_phrase(self.attempts)
            if Phrase.check_for_win(self, self.phrase.chosenPhrase, self.attempts):
                print('\nYou win!')
                self.game_continues = False
        if self.turns == 0:
            print('\nGame Over!')
    
    #guess a character
