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
            msg = player.name + " has been killed by " + self.name
        else:
            msg = "You are a crewmate, you cannot kill"
        return msg

    def win(self):
        msg = ""
        if self.role == "imposter":
            self.score += 10
            msg = self.name + " wins the game with a total of " + \
                str(self.score) + " points"
        else:
            self.score += 5
            msg = self.name + " wins the game with a total of " + \
                str(self.score) + " points"
        return msg

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
