from Clearing import Clearing
#from Card import Card

class Bird:

    def __init__(self):
        self.warriorReserve = 20
        self.roostReserve = 7

        #List to store locations of roosts, type Clearing
        self.roostLoc = []

        #Leader, type String
        self.leader = ""

        #type Card
        self.handCards = []
        self.craftedCards = []

        #Suit only, type String
        self.recruitCards = []
        self.moveCards = []
        self.battleCards = []
        self.buildCards = []
