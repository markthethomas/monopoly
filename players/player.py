"""
Player class
"""
import random

class Player(object):
    """docstring for Player"""
    def __init__(self, balance=2000):
        self.balance = balance
    def roll(self):
        return random.randint(0,6)
