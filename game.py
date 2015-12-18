"""
The Game class
"""
from properties.property import Property

class Game(Property):
    """
    Game class, instantiated w/ each new game,
    you need at least two players to play
    """
    def __init__(self, players):
        playersType = type(players).__name__
        if playersType != 'list' or not len(players) <= 2:
            raise ValueError('You need to pass in a list of 2 or more players')
        self.players = tuple(players)

    def start(self):
        self.active = True

    def restart(self):
        self.active = True
        print('Restarting game...')
        self.active = True

    def end(self):
        self.active = False


if __name__ == '__main__':
    Game(['mark', 'bob'])