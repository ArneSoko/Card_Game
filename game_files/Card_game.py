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


class CPU(Player):
    def play(self) -> list:
        card1 = random.randint(0, 4)
        while self.cards[card1] == 0:
            card1 = random.randint(0, 4)
        card2 = card1
        while self.cards[card2] == 0 or card2 == card1:
            card2 = random.randint(0, 4)
        return [card1, card2]


def generate_hand(player1: Player, player2: Player):
    for i in range(5):
        c1 = random.randint(0, 3)
        player1.cards[i] = c1
        c2 = c1
        while c2 == 1:
            c2 = random.randint(0, 3)
        player2.cards[i] = c2


def card_game():
    selections = ['k', 'j', 4, 2, 'a']
    player = Player()
    comp = CPU()
    generate_hand(player, comp)
    x, y = -1
    print("Welcome to the card game, card selections are 'k', 'j', '4', '2',"\
          + " and 'a'")
    while x not in selections:
        x = input("Please select your first card")
        if x.isalpha():
            x.lower()

    while y not in selections or y == x:
        y = input("Please select your second card")
        if y.isalpha():
            y.lower()


