class Board:
    #Initializer to construct a board object
    def __init__(self, score = {}, items = {}, cards = []):
        self.score = score #Dictionary of the score of each faction as an int
        self.items = items #Dictionary to keep track of item availibility
        self.cards = cards #List to keep track of available cards
    #This method checks if an item exists
    def ItemExists(item):
        return items[item] > 0
    #This method adds to a specific faction's score
    def AddScore(faction, number):
        scores[faction] = scores[faction] + number
    #This method subtracts from a specific faction's score
    def SubtractScore(faction, number):
        scores[faction] = scores[faction] - number
    #def SetUp():
