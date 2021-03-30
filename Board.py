class Board:
    #Initializer to construct a board object
    def __init__(self, score = {}, items = {}, cards = []):
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
    #def SetUp():
