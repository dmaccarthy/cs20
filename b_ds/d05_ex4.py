"""
CSE 2120: Data Structures
List Comprehensions
Example 4

"""

suits = "Hearts", "Diamonds", "Clubs", "Spades"
values = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]
deck = [(suit, val) for suit in suits for val in values]
for card in deck:
    print(card)
