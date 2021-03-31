from Clearing import Clearing
class Board:
    #Initializer to construct a board object
    def __init__(self):
        self.scores = {"cat":0,"bird":0} #Dictionary of the score of each faction as an int
        self.items = {"sword":2,"tea":2,"boot":2,"coin":2,"crossbow":1,"hammer":1} #Dictionary to keep track of item availibility
        self.cards = ["bunny ambush", "bird ambush"]#List to keep track of available cards
        self.clearingList = []
    #This method will return the score of the faction it is used on.
    def GetScore(self,faction):
        return self.scores[faction]
    def ItemExists(self,item):
        return self.items[item] > 0
    def AddScore(self,faction, number):
        self.scores[faction] = self.scores[faction] + number
    def SubtractScore(self,faction, number):
        self.scores[faction] = self.scores[faction] - number
    def SetUp(self,keepClear):
        self.clearingList.append(Clearing(0, 1, "fox"))
        self.clearingList.append(Clearing(1, 2, "bunny"))
        self.clearingList.append(Clearing(2, 2, "mouse"))
        self.clearingList.append(Clearing(3, 2, "bunny"))
        self.clearingList.append(Clearing(4, 1, "mouse"))
        self.clearingList.append(Clearing(5, 1, "fox"))
        self.clearingList.append(Clearing(6, 2, "mouse"))
        self.clearingList.append(Clearing(7, 1, "fox"))
        self.clearingList.append(Clearing(8, 1, "bunny"))
        self.clearingList.append(Clearing(9, 2, "fox"))
        self.clearingList.append(Clearing(10, 2, "mouse"))
        self.clearingList.append(Clearing(11, 1, "bunny"))
        #Clearing 0
        self.clearingList[0].AddAdjacent(self.clearingList[1])
        self.clearingList[0].AddAdjacent(self.clearingList[3])
        self.clearingList[0].AddAdjacent(self.clearingList[4])
        #Clearing 1
        self.clearingList[1].AddAdjacent(self.clearingList[0])
        self.clearingList[1].AddAdjacent(self.clearingList[2])
        #Clearing 2
        self.clearingList[2].AddAdjacent(self.clearingList[1])
        self.clearingList[2].AddAdjacent(self.clearingList[3])
        self.clearingList[2].AddAdjacent(self.clearingList[7])
        #Clearing 3
        self.clearingList[3].AddAdjacent(self.clearingList[0])
        self.clearingList[3].AddAdjacent(self.clearingList[2])
        self.clearingList[3].AddAdjacent(self.clearingList[5])
        #Clearing 4
        self.clearingList[4].AddAdjacent(self.clearingList[0])
        self.clearingList[4].AddAdjacent(self.clearingList[5])
        self.clearingList[4].AddAdjacent(self.clearingList[8])
        #Clearing 5
        self.clearingList[5].AddAdjacent(self.clearingList[4])
        self.clearingList[5].AddAdjacent(self.clearingList[3])
        self.clearingList[5].AddAdjacent(self.clearingList[6])
        self.clearingList[5].AddAdjacent(self.clearingList[8])
        self.clearingList[5].AddAdjacent(self.clearingList[10])
        #Clearing 6
        self.clearingList[6].AddAdjacent(self.clearingList[5])
        self.clearingList[6].AddAdjacent(self.clearingList[7])
        self.clearingList[6].AddAdjacent(self.clearingList[11])
        #Clearing 7
        self.clearingList[7].AddAdjacent(self.clearingList[2])
        self.clearingList[7].AddAdjacent(self.clearingList[6])
        self.clearingList[7].AddAdjacent(self.clearingList[11])
        #Clearing 8
        self.clearingList[8].AddAdjacent(self.clearingList[4])
        self.clearingList[8].AddAdjacent(self.clearingList[5])
        self.clearingList[8].AddAdjacent(self.clearingList[9])
        #Clearing 9
        self.clearingList[9].AddAdjacent(self.clearingList[8])
        self.clearingList[9].AddAdjacent(self.clearingList[10])
        #Clearing 10
        self.clearingList[10].AddAdjacent(self.clearingList[5])
        self.clearingList[10].AddAdjacent(self.clearingList[9])
        self.clearingList[10].AddAdjacent(self.clearingList[11])
        #Clearing 11
        self.clearingList[11].AddAdjacent(self.clearingList[6])
        self.clearingList[11].AddAdjacent(self.clearingList[7])
        self.clearingList[11].AddAdjacent(self.clearingList[10])
        #Adding pieces to the board
        for i in range(12):
            self.clearingList[i].AddWarrior("cat")
        self.clearingList[keepClear].AddToken("keep")
        print("Board set up is complete.\n")
