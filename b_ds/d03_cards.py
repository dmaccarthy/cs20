"""
CSE 2120: Data Structures
Dictionaries & Sets
"""

PLAYERS = 2
CARDS = 5

# Complete these functions only...

def makeDeck():
    "Create a list of 52 cards where each card is a dict"
    suits = {"Hearts", "Spades", "Diamonds", "Clubs"}
    return []

def deal(deck, cards, players):
    "Deal cards from the deck into players' hands"
    hands = []
    for player in range(players):
        hands.append([0] * cards)
    return hands

def prettyFormat(card):
    "Display a card in user-friendly fashion"
    return card


# DO NOT EDIT any of the code below.

from random import shuffle

def printHand(player, hand):
    print("\n{} has:".format(player))
    for card in hand:
        print(prettyFormat(card))

def main():
    deck = makeDeck()
    shuffle(deck)
    playerHands = deal(deck, CARDS, PLAYERS)
    for player, hand in enumerate(playerHands):
        printHand(f"Player {1+player}", hand)
    printHand("Deck", deck)

main()
