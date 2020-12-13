class Game:
    def __init__(self, players, nbImpostor=2):
        self.players = players
        self.nbImpostor = nbImpostor

    def __str__(self):
        return " ".join([f"{_.name} : {_.score}" for _ in self.players])

    def RandomizeScore(self):
        for _ in self.players:
            _.score = moyenne(_.previous_scores)


def somme(liste):
    _somme = 0
    for i in liste:
        _somme = _somme + i
    return _somme


def moyenne(liste):
    return somme(liste) / len(liste)
