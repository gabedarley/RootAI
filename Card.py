class Card:

    def __init__(self, id, suit, crafting):
        #Name (e.g. "Foxfolk Steel"), type String
        self.id = id

        #Suit (fox, mouse, bunny, bird), type String
        self.suit = suit

        #Crafting cost ({fox: 1, mouse: 0, bunny: 0}), type Dictionary
        self.crafting = crafting

    def CheckCraft(self, player):
        if(player.crafting["fox"] < self.crafting["fox"]):
            return False
        elif(player.crafting["bunny"] < self.crafting["bunny"]):
             return False
        elif(player.crafting["mouse"] < self.crafting["mouse"]):
             return False
        else:
            return True

    def WoodlandRunners(self, board, player):
        if self.CheckCraft(player):
            if board.items["boot"] > 0:
                board.items["boot"] += 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Woodland Runners"))


            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")
from Board import Board
