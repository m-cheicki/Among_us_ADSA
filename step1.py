import random
from AVLTree import *
from Game import *
from Player import *

tournament = AVLTree()
ranking = None
list_players = [Player(f"P{_}") for _ in range(100)]


# Create games of 10 players from a list of players.
def create_games(list_players):
    return [Game(list_players[i: i+10]) for i in range(0, len(list_players), 10)]


def randomize_score(games):
    for _ in all_games:
        _.RandomizeScore()


# Three random games
for count in range(3):
    random.shuffle(list_players)
    all_games = create_games(list_players)
    randomize_score(all_games)

# Playing games and withdrawing players based on ranking until it remains 10 players
while(len(list_players) > 10):
    all_games = create_games(list_players)
    randomize_score(all_games)

    # Build the AVL tree for the tournament
    root = AVLfromPlayers(
        [player for game in all_games for player in game.players], tournament)

    # Drop the 10 firsts players (10 lowest scores) and keep the others to continue the tournament
    list_players = tournament.getInOrder(root)[10:len(list_players)]


# Reset scores to start the final
for _ in list_players:
    _.previous_scores = [].copy()
    _.score = 0

final_game = Game(list_players)

# Playing 5 games with reinitiated ranking.
ranking = None
for _ in range(5):
    final_game.RandomizeScore()


ranking = AVLfromPlayers(final_game.players, tournament)

final_ranking = tournament.getInOrder(ranking)

# Because we want a decreasing order (max score to min score)
final_ranking.reverse()

# Display the TOP 10 Players
print("The top 10 players are : ")
for count, _ in enumerate(final_ranking):
    print(f"{count+1} - {_.name} : {_.score}")
