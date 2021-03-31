import random
class Clearing:

    def __init__(self, id, slots, suit):
        self.id = id
        self.adjacent = []
        self.birdWarriors = 0
        self.catWarriors = 0
        self.Buildings = []
        self.catTokens = []
        self.slots = slots
        self.suit = suit

    def AddAdjacent(self,adjacentClear):
        #adjacentClear must be clearing object
        self.adjacent.append(adjacentClear)

    def GetAdjacent(self):
        return self.adjancent

    def AddWarrior(self,warriorType):
        if warriorType == "bird":
            self.birdWarriors += 1
            #TODO: Update bird's warrior reserve
        if warriorType == "cat":
            self.catWarriors += 1
            #TODO: Update cat's warrior reserve

    def RemoveWarrior(self,warriorType):
        if warriorType == "bird":
            self.birdWarriors -= 1
            #TODO: Update bird's warrior reserve
        if warriorType == "cat":
            self.catWarriors -= 1
            #TODO: Update cat's warrior reserve

    def AddBuilding(self,buildingType):
        #buildingType must be roost, sawmill, workshop, or recruiter
        self.Buildings.append(buildingType)
        self.slots -= 1
        #TODO: Update Bird's roost reserve
        #TODO: Update Cat's score
        #TODO: Update Cat's building reserve
    def AddToken(self, tokenType):
        if tokenType == "keep":
            self.catTokens.append("keep")
        elif tokenType == "wood":
            self.catTokens.append("wood")
            #TODO: Update Cat's token reserve
    def RemoveWood(self):
        self.catTokens.remove("wood")
        #TODO: Update Cat's token reserve

    def RemoveBuilding(self,buildingType):
        #buildingType must be roost, sawmill, workshop, or recruiter
        self.Buildings.remove(buildingType)
        self.slots += 1
        #TODO: Update Bird's roost reserve
        #TODO: Update Cat's building reserve

    def GetNumWarrior(self,warriorType):
        if warriorType == "bird":
            return self.birdWarriors
        if warriorType == "cat":
            return self.catWarriors
    def HasKeep(self):
        if "keep" in self.catTokens:
            return True
    def GetNumWood(self):
        temp = self.catTokens
        if "keep" in temp:
            temp.remove("keep")
        return len(temp)

    def Battle(self,attacker):
        #TODO: Prompt for ambush card ?
        #attacker must be a string
        rolls = [random.randint(0,3), random.randint(0,3)]
        roll1 = max(rolls)
        roll2 = min(rolls)
        print("Roll 1: %d" % roll1)
        print("Roll 2: %d\n" % roll2)

        '''CAT ATTACKS'''
        if attacker == "cat":
            #Find max attack power for attacker and defender
            attackMax = self.catWarriors
            defendMax = self.birdWarriors

            #Check if rolled number exceeds available warriors
            if roll1 > self.catWarriors:
                roll1 = self.catWarriors
            if roll2 > self.birdWarriors:
                roll2 = self.birdWarriors

            #Check which bird pieces to remove
            if self.birdWarriors >= roll1:
                self.birdWarriors -= roll1
                #TODO: Update Bird's warrior reserve
            elif self.birdWarriors == 0:
                if "roost" in self.Buildings:
                    self.Buildings.remove("roost")
                    #TODO: Update Bird's building reserve
            else:
                warriorDiff = roll1 - self.birdWarriors
                self.birdWarriors = 0
                if "roost" in self.Buildings:
                    self.Buildings.remove("roost")
                    #TODO: Update Bird's building reserve
                    #TODO: Update Bird's warrior reserve

            #Check which cat pieces to remove
            if self.catWarriors >= roll2:
                self.catWarriors -= roll2
                #TODO Update Cat's warrior reserve
            elif self.catWarriors == 0:
                numRemoved = 0
                while numRemoved != roll2:
                    if "wood" in self.catTokens:
                        self.catTokens.remove("wood")
                    elif "workshop" in self.Buildings:
                        self.Buildings.remove("workshop")
                    elif "recruiter" in self.Buildings:
                        self.Buildings.remove("recruiter")
                    elif "sawmill" in self.Buildings:
                        self.Buildings.remove("sawmill")
                    elif "keep" in self.catTokens:
                        self.catTokens.remove("keep")
                    numRemoved += 1
            else:
                warriorDiff = roll2 - self.catWarriors
                self.catWarriors = 0
                while numRemoved != warriorDiff:
                    if "wood" in self.catTokens:
                        self.catTokens.remove("wood")
                    elif "workshop" in self.Buildings:
                        self.Buildings.remove("workshop")
                    elif "recruiter" in self.Buildings:
                        self.Buildings.remove("recruiter")
                    elif "sawmill" in self.Buildings:
                        self.Buildings.remove("sawmill")
                    elif "keep" in self.catTokens:
                        self.catTokens.remove("keep")
                    numRemoved += 1


        '''BIRD ATTACKS'''
        if attacker == "bird":
            #Find max attack power for attacker and defender
            attackMax = self.birdWarriors
            defendMax = self.catWarriors

            #Check if rolled number exceeds available warriors
            if roll1 > self.birdWarriors:
                roll1 = self.birdWarriors
            if roll2 > self.catWarriors:
                roll2 = self.catWarriors

            #Check which bird pieces to remove
            if self.birdWarriors >= roll2:
                self.birdWarriors -= roll2
                #TODO: Update Bird's warrior reserve
            elif self.birdWarriors == 0:
                if "roost" in self.Buildings:
                    self.Buildings.remove("roost")
                #TODO: Update Bird's building reserve
            else:
                self.birdWarriors = 0
                if "roost" in self.Buildings:
                    self.Buildings.remove("roost")
                    #TODO: Update Bird's building reserve
                    #TODO: Update Bird's warrior reserve

            #Check which cat pieces to remove
            if self.catWarriors >= roll1:
                self.catWarriors -= roll1
                #TODO Update Cat's warrior reserve
            elif self.catWarriors == 0:
                numRemoved = 0
                while numRemoved != roll1:
                    if "wood" in self.catTokens:
                        self.catTokens.remove("wood")
                    elif "workshop" in self.Buildings:
                        self.Buildings.remove("workshop")
                    elif "recruiter" in self.Buildings:
                        self.Buildings.remove("recruiter")
                    elif "sawmill" in self.Buildings:
                        self.Buildings.remove("sawmill")
                    elif "keep" in self.catTokens:
                        self.catTokens.remove("keep")
                    numRemoved += 1
            else:
                warriorDiff = roll1 - self.catWarriors
                self.catWarriors = 0
                while numRemoved != warriorDiff:
                    if "wood" in self.catTokens:
                        self.catTokens.remove("wood")
                    elif "workshop" in self.Buildings:
                        self.Buildings.remove("workshop")
                    elif "recruiter" in self.Buildings:
                        self.Buildings.remove("recruiter")
                    elif "sawmill" in self.Buildings:
                        self.Buildings.remove("sawmill")
                    elif "keep" in self.catTokens:
                        self.catTokens.remove("keep")
                    numRemoved += 1
