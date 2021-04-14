class Bird:

    def __init__(self):
        self.warriorReserve = 20
        self.roostReserve = 7

        #List to store locations of roosts, type Clearing
        self.roostLoc = []
        self.crafting = {"fox": 0, "bunny": 0, "mouse": 0}

        self.id = "bird"

        #Leader, type String
        self.leader = ""

        #type Card
        self.handCards = {}

        #Suit only, type String
        self.recruitCards = []
        self.moveCards = []
        self.battleCards = []
        self.buildCards = []

    def DrawCard(self,board,cardName):
        self.handCards[cardName] = board.deck.pop(cardName)

    def AddDecree(self,cardName,type):
        suit = self.handCards[cardName].suit
        board.discard.append(self.handCards.pop(cardName))
        if type == "recruit":
            self.recruitCards.append(suit)
        elif type == "move":
            self.moveCards.append(suit)
        elif type == "battle":
            self.battleCards.append(suit)
        elif type == "buildCards":
            self.buildCards.append(suit)

    def Craft(self,cardname,board,player):
        self.handCards[cardName].Action(cardName,board,player)

    def Recruit(self, clearing):
        self.warriorReserve -= 1
        clearing.birdWarriors += 1
    
    def Move(self,clearingFrom,clearingTo):
        if clearingFrom.isRuling(self.id) or clearingTo.isRuling(self.id):
            clearingFrom.birdWarriors -= 1
            clearingTo.birdWarriors += 1
        else:
            print("Not ruling in either clearing.")

    def Battle(self,clearing):
        clearing.battle("bird","cat")

    def Build(self, clearing):
        bird = Bird()
        clearing.AddBuilding("roost",bird)




import random
from Clearing import Clearing
from Card import Card
from Board import Board
