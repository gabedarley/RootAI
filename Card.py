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
    
    #Woodland Runners action
    def WoodlandRunners(self, board, player):
        if self.CheckCraft(player):
            if board.items["boot"] > 0:
                board.items["boot"] -= 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Woodland Runners"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Birdy Bindle action
    def BirdyBindle(self, board, player):
        if self.CheckCraft(player):
            if board.items["bag"] > 0:
                board.items["bag"] -= 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Birdy Bindle"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Arms Trader Action
    def ArmsTrader(self, board, player):
        if self.CheckCraft(player):
            if board.items["sword"] > 0:
                board.items["sword"] -= 1
                board.scores[player.id] += 2
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Arms Trader"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Crossbow Action
    def Crossbow(self, board, player):
        if self.CheckCraft(player):
            if board.items["crossbow"] > 0:
                board.items["crossbow"] -= 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                if self.suit == "mouse":
                    board.discard.append(player.handCards.pop("Crossbow Mouse"))
                else:
                    board.discard.append(player.handCards.pop("Crossbow Bird"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")
    #Anvil Action
    def Anvil(self, board, player):
        if self.CheckCraft(player):
            if board.items["hammer"] > 0:
                board.items["hammer"] -= 1
                board.scores[player.id] += 2
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Anvil"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Gently Used Knapsack Action
    def GentlyUsedKnapsack(self, board, player):
        if self.CheckCraft(player):
            if board.items["bag"] > 0:
                board.items["bag"] -= 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Gently Used Knapsack"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")


    #Foxfolk Steel Action
    def FoxfolkSteel(self, board, player):
        if self.CheckCraft(player):
            if board.items["sword"] > 0:
                board.items["sword"] -= 1
                board.scores[player.id] += 2
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Foxfolk Steel"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Travel Gear Action
    def TravelGear(self, board, player):
        if self.CheckCraft(player):
            if board.items["boot"] > 0:
                board.items["boot"] -= 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                if self.suit == "mouse":
                    board.discard.append(player.handCards.pop("Travel Gear Mouse"))
                else:
                    board.discard.append(player.handCards.pop("Travel Gear Fox"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Root Tea Action
    def RootTea(self, board, player):
        if self.CheckCraft(player):
            if board.items["tea"] > 0:
                board.items["tea"] -= 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                if self.suit == "mouse":
                    board.discard.append(player.handCards.pop("Root Tea Mouse"))
                elif self.suit == "fox":
                    board.discard.append(player.handCards.pop("Root Tea Fox"))
                else:
                    board.discard.append(player.handCards.pop("Root Tea Bunny"))

            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Protection Racket Action
    def ProtectionRacket(self, board, player):
        if self.CheckCraft(player):
            if board.items["coin"] > 0:
                board.items["coin"] -= 1
                board.scores[player.id] += 3
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Protection Racket"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")
        
    #Smuggler's Trail Action
    def SmugglersTrail(self, board, player):
        if self.CheckCraft(player):
            if board.items["bag"] > 0:
                board.items["bag"] -= 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Smuggler's Trail"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Bake Sale Action
    def BakeSale(self, board, player):
        if self.CheckCraft(player):
            if board.items["coin"] > 0:
                board.items["coin"] -= 1
                board.scores[player.id] += 3
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Bake Sale"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Investments Action
    def Investments(self, board, player):
        if self.CheckCraft(player):
            if board.items["coin"] > 0:
                board.items["coin"] -= 1
                board.scores[player.id] += 3
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Investments"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Sword Action
    def Sword(self, board, player):
        if self.CheckCraft(player):
            if board.items["sword"] > 0:
                board.items["sword"] -= 1
                board.scores[player.id] += 2
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Sword"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    #Mouse-in-a-Sack Action
    def MouseinaSack(self, board, player):
        if self.CheckCraft(player):
            if board.items["bag"] > 0:
                board.items["bag"] -= 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("Mouse-in-a-Sack"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    # A Visit to Friends Action
    def AVisittoFriends(self, board, player):
        if self.CheckCraft(player):
            if board.items["boot"] > 0:
                board.items["boot"] -= 1
                board.scores[player.id] += 1
                print("Card crafted")
                print("Cat's Score: " + str(board.GetScore("cat")) + "\n")
                print("Bird's Score: " + str(board.GetScore("bird")) + "\n")
                board.discard.append(player.handCards.pop("A Visit to Friends"))
            else:
                print("Not enough items")
        else:
            print("Crafting requirement not met")

    cardActions = {"Woodland Runners":WoodlandRunners,"Birdy Bindle":BirdyBindle,"Arms Trader":ArmsTrader,"Crossbow":Crossbow,
    "Anvil":Anvil,"Gently Used Knapsack": GentlyUsedKnapsack,"Foxfolk Steel":FoxfolkSteel,"Travel Gear": TravelGear,"Root Tea": RootTea,
    "Protection Racket":ProtectionRacket,"Smuggler's Trail":SmugglersTrail,"Bake Sale":BakeSale,"Investments":Investments,
    "Sword":Sword,"Mouse-in-a-Sack":MouseinaSack,"A Visit to Friends":AVisittoFriends}

    def Action(self, cardName, board, player):
        actions =  getattr(self, "cardActions")
        actions[cardName](self,board,player)
    
    from Board import Board
