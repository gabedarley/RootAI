
class Board:
    #Initializer to construct a board object
    def __init__(self):
        self.scores = {"cat":0,"bird":0} #Dictionary of the score of each faction as an int
        self.items = {"sword":2,"tea":2,"boot":2,"coin":2,"crossbow":1,"hammer":1,"bag":2} #Dictionary to keep track of item availibility
        self.deck = {} #Dictionary to keep track of available cards
        self.discard = [] #List for the discard
        self.clearingList = []
        #Initializing the players
        self.bird = Bird()
        self.cat = Cat()
    #This method will return the score of the faction it is used on.
    def GetScore(self,faction):
        return self.scores[faction]
    def ItemExists(self,item):
        return self.items[item] > 0
    def AddScore(self,faction, number):
        self.scores[faction] = self.scores[faction] + number
    def SubtractScore(self,faction, number):
        self.scores[faction] = self.scores[faction] - number
    def ClearingState(self,i):
        sawmills = 0;
        workshops = 0;
        recruiters = 0;
        roosts = 0;
        hasKeep = False;
        print("Cat's Score: " + str(self.GetScore("cat")) + "\n")
        print("Bird's Score: " + str(self.GetScore("bird")) + "\n")
        hasKeep = self.clearingList[i].HasKeep()
        for j in self.clearingList[i].Buildings:
            print(j)
            if j == "sawmill":
                sawmills += 1;
            elif j == "workshop":
                workshops += 1;
            elif j == "recruiter":
                recruiters += 1;
            elif j == "roost":
                roosts += 1;
        print("----- CLEARING " + str(i) + " -----\n")
        if hasKeep:
            print("**KEEP**")
        print("Cat: " + str(self.clearingList[i].GetNumWarrior("cat")) + " Warriors "+ str(self.clearingList[i].GetNumWood()) + " Wood")
        print("Bird: " + str(self.clearingList[i].GetNumWarrior("bird")) + " Warriors " +  str(roosts) + " Roosts\n")

    def boardState(self):

        print("Cat's Score: " + str(self.GetScore("cat")) + "\n")
        print("Bird's Score: " + str(self.GetScore("bird")) + "\n")
        for i in range(12):
            sawmills = 0;
            workshops = 0;
            recruiters = 0;
            roosts = 0;
            hasKeep = False;

            hasKeep = self.clearingList[i].HasKeep()

            for j in self.clearingList[i].Buildings:
                print(j)
                if j == "sawmill":
                    sawmills += 1;
                elif j == "workshop":
                    workshops += 1;
                elif j == "recruiter":
                    recruiters += 1;
                elif j == "roost":
                    roosts += 1;
            print("----- CLEARING " + str(i) + " -----\n")
            if hasKeep:
                print("**KEEP**")
            print("Cat: " + str(self.clearingList[i].GetNumWarrior("cat")) + " Warriors "+ str(self.clearingList[i].GetNumWood()) + " Wood")
            print("Bird: " + str(self.clearingList[i].GetNumWarrior("bird")) + " Warriors " +  str(roosts) + " Roosts\n")

    def SetUp(self,keepClear):
        #Making all of the clearing objects
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
            self.clearingList[i].AddWarrior(self.cat)
        self.clearingList[keepClear].AddToken("keep")
        checkKeep = [0,2,8,11]
        if keepClear not in checkKeep:
            print("The keep must be in a corner clearing.\nSet up again.\n")
        if keepClear == 8:
            self.clearingList[2].AddBuilding("roost",self.bird)
            self.clearingList[2].RemoveWarrior(self.cat)
            for i in range(6):
                self.clearingList[2].AddWarrior(self.bird)
        elif keepClear == 11:
            self.clearingList[0].AddBuilding("roost",bird)
            self.clearingList[0].RemoveWarrior(self.cat)
            for i in range(6):
                self.clearingList[0].AddWarrior(self.bird)
        elif keepClear == 2:
            self.clearingList[8].AddBuilding("roost",self.bird)
            self.clearingList[8].RemoveWarrior(self.cat)
            for i in range(6):
                self.clearingList[8].AddWarrior(self.bird)
        elif keepClear == 0:
            self.clearingList[11].AddBuilding("roost",self.bird)
            self.clearingList[11].RemoveWarrior(self.cat)
            for i in range(6):
                self.clearingList[11].AddWarrior(self.bird)
        #Making all of the cards
        #BIRD CARDS
        self.deck["Woodland Runners"] = Card("Woodland Runners","bird",{"fox":0,"bunny":1,"mouse":0})
        self.deck["Birdy Bindle"] = Card("Birdy Bindle","bird",{"fox":0,"bunny":0,"mouse":1})
        self.deck["Arms Trader"] = Card("Arms Trader","bird",{"fox":2,"bunny":0,"mouse":0})
        self.deck["Crossbow Bird"] = Card("Crossbow","bird",{"fox":1,"bunny":0,"mouse":0})
        self.deck["Brutal Tactics"] = Card("Brutal Tactics","bird",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Brutal Tactics Two"] = Card("Brutal Tactics Two","bird",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Royal Claim"] = Card("Royal Claim","bird",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Sappers"] = Card("Sappers","bird",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Sappers Two"] = Card("Sappers Two","bird",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Armorers"] = Card("Armorers","bird",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Armorers Two"] = Card("Armorers Two","bird",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Dominance"] = Card("Dominance","bird",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Ambush!"] = Card("Ambush!","bird",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Ambush! Two"] = Card("Ambush! Two","bird",{"fox":0,"bunny":0,"mouse":0})
        #FOX CARDS
        self.deck["Protection Racket"] = Card("Protection Racket","fox",{"fox":0,"bunny":2,"mouse":0})
        self.deck["Root Tea Fox"] = Card("Root Tea","fox",{"fox":0,"bunny":0,"mouse":1})
        self.deck["Travel Gear Fox"] = Card("Travel Gear","fox",{"fox":0,"bunny":1,"mouse":0})
        self.deck["Foxfolk Steel"] = Card("Foxfolk Steel","fox",{"fox":2,"bunny":2,"mouse":0})
        self.deck["Gently Used Knapsack"] = Card("Gently Used Knapsack","fox",{"fox":0,"bunny":0,"mouse":1})
        self.deck["Anvil"] = Card("Anvil","fox",{"fox":1,"bunny":0,"mouse":0})
        self.deck["Tax Collector"] = Card("Tax Collector","fox",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Tax Collector Two"] = Card("Tax Collector Two","fox",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Stand and Deliver!"] = Card("Stand and Deliver!","fox",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Tax Collector Three"] = Card("Tax Collector Three","fox",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Stand and Deliver! Two"] = Card("Stand and Deliver! Two","fox",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Dominance"] = Card("Dominance","fox",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Favor of the Foxes"] = Card("Favor of the Foxes","fox",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Ambush!"] = Card("Ambush!","fox",{"fox":0,"bunny":0,"mouse":0})
        #BUNNY CARDS
        self.deck["Summgler's Trail"] = Card("Smuggler's Trail","bunny",{"fox":0,"bunny":0,"mouse":1})
        self.deck["A Visit to Friends"] = Card("A Visit to Friends","bunny",{"fox":0,"bunny":1,"mouse":0})
        self.deck["Root Tea Bunny"] = Card("Root Tea","bunny",{"fox":0,"bunny":0,"mouse":1})
        self.deck["Bake Sale"] = Card("Bake Sale","bunny",{"fox":0,"bunny":2,"mouse":0})
        self.deck["Better Burrow Bank"] = Card("Better Burrow Bank","bunny",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Cobbler"] = Card("Cobbler","bunny",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Dominance"] = Card("Dominance","bunny",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Cobbler Two"] = Card("Cobbler Two","bunny",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Favor of the Rabbits"] = Card("Favor of the Rabbits","bunny",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Command Warren"] = Card("Command Warren","bunny",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Command Warren Two"] = Card("Command Warren Two","bunny",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Better Burrow Bank Two"] = Card("Better Burrow Bank Two","bunny",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Ambush!"] = Card("Ambush!","bunny",{"fox":0,"bunny":0,"mouse":0})
        #MOUSE CARDS
        self.deck["Root Tea Mouse"] = Card("Root Tea","mouse",{"fox":0,"bunny":0,"mouse":1})
        self.deck["Crossbow Mouse"] = Card("Crossbow","mouse",{"fox":1,"bunny":0,"mouse":0})
        self.deck["Travel Gear Mouse"] = Card("Travel Gear","mouse",{"fox":0,"bunny":1,"mouse":0})
        self.deck["Sword"] = Card("Sword","mouse",{"fox":2,"bunny":0,"mouse":0})
        self.deck["Investments"] = Card("Investments","mouse",{"fox":0,"bunny":2,"mouse":0})
        self.deck["Mouse-in-a-Sack"] = Card("Mouse-in-a-Sack","mouse",{"fox":0,"bunny":0,"mouse":1})
        self.deck["Scouting Party"] = Card("Scouting Party","mouse",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Dominance"] = Card("Dominance","mouse",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Scouting Party Two"] = Card("Scouting Party Two","mouse",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Codebreakers"] = Card("Codebreakers","mouse",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Codebreakers Two"] = Card("Codebreakers Two","mouse",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Favor of the Mice"] = Card("Favor of the Mice","mouse",{"fox":0,"bunny":0,"mouse":0})
        self.deck["Ambush!"] = Card("Ambush!","mouse",{"fox":0,"bunny":0,"mouse":0})




        

        print("Board set up is complete.\n")

from Clearing import Clearing
from Cat import Cat
from Bird import Bird
from Card import Card
