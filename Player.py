import random
from enum import Enum


class Role(Enum):
    IMPOSTER = "imposter"
    CREWMATE = "crewmate"


# Player

class Player:

    def __init__(self, name, role=None, score=0, previous_scores=[]):
        self.name = name
        self.role = role.value if role else None
        self.score = score
        self.previous_scores = previous_scores.copy()

    def kill(self, player):
        msg = ""
        if self.role == "imposter":
            self.score += 1
            return f"{player.name} has been killed by {self.name}"
        else:
            return "You are a crewmate, you cannot kill"

    def win(self):
        msg = ""
        self.score += 10 if self.role == "imposter" else 5
        return f"{self.name} wins the game with a total of {self.score} points"

    def __str__(self):
        # return f"My name is {self.name}  { f'and I am a {self.role}' if self.role else ''} \n\rMy actual score is : {self.score}"
        return f"{self.score}"

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score
