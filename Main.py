import time
from Board import Board
boardOne = Board()
boardOne.SetUp(0)
boardOne.boardState()
boardOne.bird.DrawCard(boardOne,"Sword")
name = input()
boardOne.bird.handCards[name].Action(name,boardOne,boardOne.bird)
boardOne.bird.Build(boardOne.clearingList[5])
boardOne.boardState()
