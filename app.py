# Import your Game class
from game import Game


# Create your Dunder Main statement.
# dunder main
if __name__ == "__main__":
    # Create an instance of your Game class
    game = Game(['Frankly, my dear, I dont give a damn',
                 'Toto, Ive a feeling were not in Kansas anymore',
                 'Im going to make him an offer he cant refuse',
                 'Go ahead make my day',
                 'May the Force be with you',
                 'You talking to me?',
                 'Ill be back',
                 'You cant handle the truth', 'I want to play a game'])
    # Start your game by calling the instance method that starts the game loop
    game.start()
