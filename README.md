# Card Game

Working on my own card game, and working on making a Python Pygame program to run the game

### Modules
pygame_test.py is a python module in which I use the Copyrighted E-Card cards from Kaiji: Ultimate Survivor by Nobuyuki Fukumoto to test various functionality for the card game.

## Card Game Rules

The card game in question is still in development, but the basic idea will be that there are 5 "Unit" cards, and the game is played by picking 2 cards out of your 5 card hand to form an "act of war" against your opponents pair. The game can be played either with an order of cards determined by rank and suit, or an order of cards determined by order in the pair (ie: left card plays first)

The deck consists of "King", "General", "Platoon", "Squad", and "Commando" cards. The "King" can defeat any card EXCEPT for the "Commando", and any other card besides the "King" can defeat the "Commando". The "Commando" is the only card which defeats the "King", unless there is a "Commando" of a higher suit in the opponent's pair. 

In the case of a duplicate tie (ie: "General" vs "General"), the suit of the card determines the tie-breaker.

Any card that is defeated in a round must be taken out of the player's hand and remain out of the player's hand until a win-condition is reached.

A player must "Surrender" if they can no longer form a pair to play: thus the win-condition is to force your opponent to "Surrender"

If the player chooses to play with order determined by card rank, then the order is this:
1. "Commando" or Ace
2. "King"
3. "General" or Jack
4. "Platoon" or 4
5. "Squad" or 2

Ties are determined with this suit order:
1. Spades
2. Clubs
3. Diamonds
4. Hearts

If the player chooses to play with order by card rank, then there are 10 possible pairs; but if the player chooses to play with left-to-right order then there are 20 possible pairs.

The deck, consisting of 4 of each "Unit", will be shuffled before play, randomizing the suits of each player's hand

If the player chooses to play with left-to-right order, the order of which hand goes first will be determined by coin flip before the round.
