import random
from AVLTree import *
from Game import *
from Player import *

Tournament = AVLTree()
Ranking = None
listPlayers = [Player(f"P{_}") for _ in range(100)]

for count in range(3):
    random.shuffle(listPlayers)
    AllGames = [Game(listPlayers[i: i+10])
                for i in range(0, len(listPlayers), 10)]
    for _ in AllGames:
        _.RandomizeScore()


# Playing games and withdrawing players until 10 remain
while(len(listPlayers) > 10):
    AllGames = [Game(listPlayers[i: i+10])
                for i in range(0, len(listPlayers), 10)]
    for _ in AllGames:
        _.RandomizeScore()

    root = AVLfromPlayers(
        [player for game in AllGames for player in game.players], Tournament)
    listPlayers = Tournament.getInOrder(root)[10:len(listPlayers)]


# Reset scores to start the final
for _ in listPlayers:
    _.previous_scores = [].copy()
    _.score = 0


FinalGame = Game(listPlayers)
for _ in range(5):
    FinalGame.RandomizeScore()
Ranking = None
Ranking = AVLfromPlayers(FinalGame.players, Tournament)

RankingFinal = Tournament.getInOrder(Ranking)
RankingFinal.reverse()
for count, _ in enumerate(RankingFinal):
    print(f"{count+1} - {_.name} : {_.score}")
