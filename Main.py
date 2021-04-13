import time
from Board import Board

boardOne = Board()
boardOne.SetUp(0)
boardOne.boardState()
boardOne.bird.DrawCard(boardOne)
boardOne.bird.handCards["Woodland Runners"].WoodlandRunners(boardOne, boardOne.bird)
