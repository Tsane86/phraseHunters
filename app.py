# Import your Game class
from game import Game


# Create your Dunder Main statement.
# dunder main
if __name__ == "__main__":
    # Create an instance of your Game class
    game = Game()
    # Start your game by calling the instance method that starts the game loop
    game.start()
