import random


def somme(liste):
    _somme = 0
    for i in liste:
        _somme = _somme + i
    return _somme


def moyenne(liste):
    return somme(liste) / len(liste)


class Game:
    def __init__(self, players, nb_impostor=2):
        self.players = players
        self.nb_impostor = nb_impostor

    def __str__(self):
        return " ".join([f"{_.name} : {_.score}" for _ in self.players])

    def RandomizeScore(self):
        for _ in self.players:
            _.previous_scores.append(random.randint(0, 12))
            _.score = moyenne(_.previous_scores)
