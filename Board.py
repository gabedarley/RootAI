from Clearing import Clearing
class Board:
    #Initializer to construct a board object
    def __init__(self, score = {}, items = {}, cards = [], clearingList = []):
        self.score = score #Dictionary of the score of each faction as an int
        self.items = items #Dictionary to keep track of item availibility
        self.cards = cards #List to keep track of available cards
    #This method will return the score of the faction it is used on.
    def GetScore(faction):
        return scores[faction]
    def ItemExists(item):
        return items[item] > 0
    def AddScore(faction, number):
        scores[faction] = scores[faction] + number
    def SubtractScore(faction, number):
        scores[faction] = scores[faction] - number
    def SetUp():
        clearingList = [];
        clearingList.append(Clearing(0, 1, "fox"))
        clearingList.append(Clearing(1, 2, "bunny"))
        clearingList.append(Clearing(2, 2, "mouse"))
        clearingList.append(Clearing(3, 2, "bunny"))
        clearingList.append(Clearing(4, 1, "mouse"))
        clearingList.append(Clearing(5, 1, "fox"))
        clearingList.append(Clearing(6, 2, "mouse"))
        clearingList.append(Clearing(7, 1, "fox"))
        clearingList.append(Clearing(8, 1, "bunny"))
        clearingList.append(Clearing(9, 2, "fox"))
        clearingList.append(Clearing(10, 2, "mouse"))
        clearingList.append(Clearing(11, 1, "bunny"))
        #Clearing 0
        clearingList[0].AddAdjacent(clearingList[1])
        clearingList[0].AddAdjacent(clearingList[3])
        clearingList[0].AddAdjacent(clearingList[4])
        #Clearing 1
        clearingList[1].AddAdjacent(clearingList[0])
        clearingList[1].AddAdjacent(clearingList[2])
        #Clearing 2
        clearingList[2].AddAdjacent(clearingList[1])
        clearingList[2].AddAdjacent(clearingList[3])
        clearingList[2].AddAdjacent(clearingList[7])
        #Clearing 3
        clearingList[3].AddAdjacent(clearingList[0])
        clearingList[3].AddAdjacent(clearingList[2])
        clearingList[3].AddAdjacent(clearingList[5])
        #Clearing 4
        clearingList[4].AddAdjacent(clearingList[0])
        clearingList[4].AddAdjacent(clearingList[5])
        clearingList[4].AddAdjacent(clearingList[8])
        #Clearing 5
        clearingList[5].AddAdjacent(clearingList[4])
        clearingList[5].AddAdjacent(clearingList[3])
        clearingList[5].AddAdjacent(clearingList[6])
        clearingList[5].AddAdjacent(clearingList[8])
        clearingList[5].AddAdjacent(clearingList[10])
        #Clearing 6
        clearingList[6].AddAdjacent(clearingList[5])
        clearingList[6].AddAdjacent(clearingList[7])
        clearingList[6].AddAdjacent(clearingList[11])
        #Clearing 7
        clearingList[7].AddAdjacent(clearingList[2])
        clearingList[7].AddAdjacent(clearingList[6])
        clearingList[7].AddAdjacent(clearingList[11])
        #Clearing 8
        clearingList[8].AddAdjacent(clearingList[4])
        clearingList[8].AddAdjacent(clearingList[5])
        clearingList[8].AddAdjacent(clearingList[9])
        #Clearing 9
        clearingList[9].AddAdjacent(clearingList[8])
        clearingList[9].AddAdjacent(clearingList[10])
        #Clearing 10
        clearingList[10].AddAdjacent(clearingList[5])
        clearingList[10].AddAdjacent(clearingList[9])
        clearingList[10].AddAdjacent(clearingList[11])
        #Clearing 11
        clearingList[11].AddAdjacent(clearingList[6])
        clearingList[11].AddAdjacent(clearingList[7])
        clearingList[11].AddAdjacent(clearingList[10])
        print("Board set up is complete.\n")
