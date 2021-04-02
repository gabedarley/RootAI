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

    def AddAdjacent(self, adjacentClear):
        #adjacentClear must be clearing object
        self.adjacent.append(adjacentClear)

    def GetAdjacent(self):
        return self.adjancent

    def AddWarrior(self, player):
        #player is type Bird or Cat
        if player.id == "bird":
            self.birdWarriors += 1
            player.warriorReserve -= 1
        if player.id == "cat":
            self.catWarriors += 1
            player.warriorReserve -= 1

    def RemoveWarrior(self, player):
        #player is type Bird or Cat
        if player.id == "bird":
            self.birdWarriors -= 1
            player.warriorReserve += 1
        if player.id == "cat":
            self.catWarriors -= 1
            player.warriorReserve += 1

    def AddBuilding(self, buildingType, player):
        #buildingType must be roost, sawmill, workshop, or recruiter
        self.Buildings.append(buildingType)
        self.slots -= 1

        if player.id == "bird":
            player.roostReserve -= 1
        elif player.id == "cat":
            if buildingType == "sawmill":
                player.sawmillReserve -= 1
            elif buildType == "workshop":
                player.workshopReserve -= 1
            else:
                player.recruiterReserve -= 1

    def AddToken(self, tokenType, player):
        if tokenType == "keep":
            self.catTokens.append("keep")
        elif tokenType == "wood":
            self.catTokens.append("wood")
            player.woodReserve -= 1

    def RemoveWood(self, player):
        self.catTokens.remove("wood")
        player.woodReserve += 1

    def RemoveBuilding(self, buildingType):
        #buildingType must be roost, sawmill, workshop, or recruiter
        self.Buildings.remove(buildingType)
        self.slots += 1
        if player.id == "bird":
            player.roostReserve += 1
        elif player.id == "cat":
            if buildingType == "sawmill":
                player.sawmillReserve += 1
            elif buildType == "workshop":
                player.workshopReserve += 1
            else:
                player.recruiterReserve += 1

    def GetNumWarrior(self, warriorType):
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

    def Battle(self, attacker, defender):
        #TODO: Prompt for ambush card ?
        #attacker must be a string
        rolls = [random.randint(0,3), random.randint(0,3)]
        roll1 = max(rolls)
        roll2 = min(rolls)
        print("Roll 1: %d" % roll1)
        print("Roll 2: %d\n" % roll2)

        '''CAT ATTACKS'''
        if attacker.id == "cat":
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
                defender.warriorReserve += roll1
            elif self.birdWarriors == 0:
                if "roost" in self.Buildings:
                    self.Buildings.remove("roost")
                    defender.roostReserve += 1
            else:
                warriorDiff = roll1 - self.birdWarriors
                self.birdWarriors = 0
                if "roost" in self.Buildings:
                    self.Buildings.remove("roost")
                    defender.roostReserve += 1
                    defender.warriorReserve += warriorDiff

            #Check which cat pieces to remove
            if self.catWarriors >= roll2:
                self.catWarriors -= roll2
                #TODO Update Cat's warrior reserve
            elif self.catWarriors == 0:
                numRemoved = 0
                while numRemoved != roll2:
                    if "wood" in self.catTokens:
                        self.catTokens.remove("wood")
                        attacker.woodReserve += 1
                    elif "workshop" in self.Buildings:
                        self.Buildings.remove("workshop")
                        attacker.workshopReserve += 1
                    elif "recruiter" in self.Buildings:
                        self.Buildings.remove("recruiter")
                        attacker.recruiterReserve += 1
                    elif "sawmill" in self.Buildings:
                        self.Buildings.remove("sawmill")
                        attacker.sawmillReserve += 1
                    elif "keep" in self.catTokens:
                        self.catTokens.remove("keep")
                    numRemoved += 1
            else:
                warriorDiff = roll2 - self.catWarriors
                self.catWarriors = 0
                while numRemoved != warriorDiff:
                    if "wood" in self.catTokens:
                        self.catTokens.remove("wood")
                        attacker.woodReserve += 1
                    elif "workshop" in self.Buildings:
                        self.Buildings.remove("workshop")
                        attacker.workshopReserve += 1
                    elif "recruiter" in self.Buildings:
                        self.Buildings.remove("recruiter")
                        attacker.recruiterReserve += 1
                    elif "sawmill" in self.Buildings:
                        self.Buildings.remove("sawmill")
                        attacker.sawmillReserve += 1
                    elif "keep" in self.catTokens:
                        self.catTokens.remove("keep")
                    numRemoved += 1


        '''BIRD ATTACKS'''
        if attacker.id == "bird":
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
                attacker.warriorReserve += roll2
            elif self.birdWarriors == 0:
                if "roost" in self.Buildings:
                    self.Buildings.remove("roost")
                    attacker.roostReserve += 1
            else:
                warriorDiff = roll1 - self.birdWarriors
                self.birdWarriors = 0
                if "roost" in self.Buildings:
                    self.Buildings.remove("roost")
                    attacker.roostReserve += 1
                    attacker.warriorReserve += warriorDiff

            #Check which cat pieces to remove
            if self.catWarriors >= roll1:
                self.catWarriors -= roll1
                defender.warriorReserve += roll1
            elif self.catWarriors == 0:
                numRemoved = 0
                while numRemoved != roll1:
                    if "wood" in self.catTokens:
                        self.catTokens.remove("wood")
                        defender.woodReserve += 1
                    elif "workshop" in self.Buildings:
                        self.Buildings.remove("workshop")
                        defender.workshopReserve += 1
                    elif "recruiter" in self.Buildings:
                        self.Buildings.remove("recruiter")
                        defender.recruiterReserve += 1
                    elif "sawmill" in self.Buildings:
                        self.Buildings.remove("sawmill")
                        defender.sawmillReserve += 1
                    elif "keep" in self.catTokens:
                        self.catTokens.remove("keep")
                    numRemoved += 1
            else:
                warriorDiff = roll1 - self.catWarriors
                self.catWarriors = 0
                defender.warriorReserve += warriorDiff
                while numRemoved != warriorDiff:
                    if "wood" in self.catTokens:
                        self.catTokens.remove("wood")
                        defender.woodReserve += 1
                    elif "workshop" in self.Buildings:
                        self.Buildings.remove("workshop")
                        defender.workshopReserve += 1
                    elif "recruiter" in self.Buildings:
                        self.Buildings.remove("recruiter")
                        defender.recruiterReserve += 1
                    elif "sawmill" in self.Buildings:
                        self.Buildings.remove("sawmill")
                        defender.sawmillReserve += 1
                    elif "keep" in self.catTokens:
                        self.catTokens.remove("keep")
                    numRemoved += 1

import random
from Cat import Cat
from Bird import Bird
