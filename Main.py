from Board import Board

boardOne = Board()
boardOne.SetUp(0)
print("Cat's Score: " + str(boardOne.GetScore("cat")) + "\n")
print("Bird's Score: " + str(boardOne.GetScore("bird")) + "\n")
boardOne.clearingList[0].AddToken("wood")
boardOne.clearingList[0].AddToken("wood")
boardOne.clearingList[0].AddToken("wood")
boardOne.clearingList[0].AddToken("wood")
boardOne.clearingList[0].AddToken("wood")
for i in range(12):
    print("----- CLEARING " + str(i) + " -----\n")
    print("Cat: " + str(boardOne.clearingList[i].GetNumWarrior("cat")) + " Warriors "+ str(boardOne.clearingList[i].GetNumWood()) + " Wood" + "\n")
    print("Bird: " + str(boardOne.clearingList[i].GetNumWarrior("bird")) + " Warriors" +  "\n")
    
