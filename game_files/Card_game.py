import random

"""
Below are the classes to be used in the game. Player is the basic class.
The child class, CPU, features a function to produce a tuple containing the
cards a CPU would play. As of January 18th 2021 I have not yet considered any
strategies for the game, so the CPU currently plays a random pair from its hand.


== Attributes ==

cards:
    -A list of 5 ints, representing the Player's hand, and the suit of each card
    represented by a number from 1 to 4. A 0 for the suit means the card has
    been defeated.
    
== Methods == 

generate_cards:
    #TODO

play:
    -A CPU controlled Player currently plays a hand by randomly selecting a pair
    of valid cards from its hand. It does this by making a random selection from
    0 to 4 (the bounds of the list), and then checking that the index is valid.
"""
class Player:
    def __init__(self):
        self.cards = [0, 0, 0, 0, 0]
    #TODO: generate_cards program

class CPU(Player):
    def play(self) -> tuple:
        card1 = 0
        card2 = 0
        while self.cards[card1] == 0:
            card1 = random.randint(0, 4)
        while self.cards[card2] == 0 or card2 == card1:
            card2 = random.randint(0, 4)
        return tuple((card1, card2))


def card_game:

