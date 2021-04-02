class Cat:

    def __init__(self):
        self.warriorReserve = 25
        self.woodReserve = 8
        self.sawmillReserve = 6
        self.workshopReserve = 6
        self.recruiterReserve = 6

        self.id = "cat"

        #Lists to store locations of buildings, type Clearing
        self.sawmillLoc = []
        self.workshoplLoc = []
        self.recruiterLoc = []
        self.crafting = {"fox": 0, "bunny": 0, "mouse": 0}

        #type Card
        self.handCards = []
        self.craftedCards = []

from Clearing import Clearing
from Card import Card
