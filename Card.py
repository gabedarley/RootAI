class Card:

    def __init__(self, id, suit, crafting, cardType):
        #Name (e.g. "Foxfolk Steel"), type String
        self.id = id

        #Suit (Fox, Mouse, Bunny, Bird), type String
        self.suit = suit

        #Crafting cost ({Fox: 1, Mouse: 0, Bunny: 0, Bird: 0}), type Dictionary
        self.crafting = crafting

        #Card type (Ambush, Item, Immediate, Long)
        self.cardType = cardType
