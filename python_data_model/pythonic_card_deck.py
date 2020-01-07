#  Dunder Methods / Special Methods / Underscore-underscore methods

#  not meant to be called by user, but by the Python interpreter
#  user: call the built-in functions (len, iter, str ...) instead

import collections

#  Named tuples assign meaning to each position in a tuple and
#  allow for more readable, self-documenting code.
#  They can be used wherever regular tuples are used,
#  and they add the ability to access fields by name instead of position index.

#  collections.namedtuple(typename, field_names[])
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        #  52 cards
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]


    #  Defines how FrenchDeck responds to the len() function
    def __len__(self):
        return len(self._cards)

    #  Defines how FrenchDeck responds to the [] operator
    #  automatically supporting slicing, iterable 
    def __getitem__(self, position):
        return self._cards[position]


#  define a way to rank those cards
#  toggling the sign of the key function can toggle the order of sort (ascending/descending)
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return -(rank_value * len(suit_values) + suit_values[card.suit])


def main():
    deck = FrenchDeck()

    print("size of the deck is %d"%len(deck))

    print("The 4th card in the deck is ", (deck[4])) 

    from random import choice
    print(choice(deck))


    #  Suppporting slicing
    print("The top three cards are ", deck[:3])

    #  Supporting in operator
    #  if __contains__ not defined, the inoperator scans the object sequentailly
    print("4 of spades in the deck is %s"%(Card('4', 'spades') in deck))
    print("4 of signature in the deck is %s"%(Card('4', 'signature') in deck))

    print("sorting also works with a defined key")
    for card in sorted(deck, key=spades_high):
        print(card)

    

if __name__ == "__main__":
    main()
