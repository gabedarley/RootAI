from Clearing import Clearing
#from Card import Card

class Cat:

    def __init__(self):
        self.warriorReserve = 25
        self.woodReserve = 8
        self.sawmillReserve = 6
        self.workshopReserve = 6
        self.recruiterReserve = 6

        #Lists to store locations of buildings, type Clearing
        self.sawmillLoc = []
        self.workshoplLoc = []
        self.recruiterLoc = []

        #type Card
        self.handCards = []
        self.craftedCards = []
