import random

class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def adjacentes(self, jeu):
        cases_adjacentes = []
        for case in jeu.listeDesCases:
            if self != case and abs(self.x - case.x) <= 1 and abs(self.y - case.y) <= 1:
                cases_adjacentes.append(case)
        return cases_adjacentes

class Creature:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position

    def __str__(self):
        return f"{self.nom} - Position : {self.position}"

    def choisirCible(self, jeu):
        cases_adjacentes = self.position.adjacentes(jeu)
        cases_occupees = [case for case in cases_adjacentes if jeu.est_occupee(case)]
        if cases_occupees:
            return random.choice(cases_occupees)
        else:
            return random.choice(cases_adjacentes)

class Jeu:
    def __init__(self, taille):
        self.listeDesCases = [Case(x, y) for x in range(taille) for y in range(taille)]
        self.listeDesCreatures = []
        self.tour = 0
        self.actif = None

    def __str__(self):
        return f"Tour : {self.tour}, Actif : {self.actif}\n{', '.join(str(creature) for creature in self.listeDesCreatures)}"

    def est_occupee(self, case):
        return any(creature.position.x == case.x and creature.position.y == case.y for creature in self.listeDesCreatures)

    def creer_creature(self, nom, position):
        creature = Creature(nom, position)
        self.listeDesCreatures.append(creature)

    def deplacer(self, creature, case):
        if creature in self.listeDesCreatures:
            if case in creature.position.adjacentes(self):
                if self.est_occupee
import random

class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def adjacentes(self, jeu):
        cases_adjacentes = []
        for case in jeu.listeDesCases:
            if self != case and abs(self.x - case.x) <= 1 and abs(self.y - case.y) <= 1:
                cases_adjacentes.append(case)
        return cases_adjacentes

class Creature:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position

    def __str__(self):
        return f"{self.nom} - Position : {self.position}"

    def choisirCible(self, jeu):
        cases_adjacentes = self.position.adjacentes(jeu)
        cases_occupees = [case for case in cases_adjacentes if jeu.est_occupee(case)]
        if cases_occupees:
            return random.choice(cases_occupees)
        else:
            return random.choice(cases_adjacentes)

class Jeu:
    def __init__(self, taille):
        self.listeDesCases = [Case(x, y) for x in range(taille) for y in range(taille)]
        self.listeDesCreatures = []
        self.tour = 0
        self.actif = None

    def __str__(self):
        return f"Tour : {self.tour}, Actif : {self.actif}\n{', '.join(str(creature) for creature in self.listeDesCreatures)}"

    def est_occupee(self, case):
        return any(creature.position.x == case.x and creature.position.y == case.y for creature in self.listeDesCreatures)

    def creer_creature(self, nom, position):
        creature = Creature(nom, position)
        self.listeDesCreatures.append(creature)

    def deplacer(self, creature, case):
        if creature in self.listeDesCreatures:
            if case in creature.position.adjacentes(self):
                if self.est_occupee(case):
                    print(f"{creature.nom} a capturé une créature ! {creature.nom} a gagné !")
                    self.listeDesCreatures.remove(creature)
                else:
                    creature.position = case
                    self.tour += 1
                    self.actif = self.listeDesCreatures[(self.tour % len(self.listeDesCreatures))]
                    print(f"{creature.nom} s'est déplacé vers {case}")
            else:
                print("Déplacement non autorisé.")
        else:
            print("Cette créature n'existe pas dans le jeu.")


jeu = Jeu(4)

jeu.creer_creature("Creature1", jeu.listeDesCases[0])
jeu.creer_creature("Creature2", jeu.listeDesCases[-1])

while len(jeu.listeDesCreatures) > 1:
    for creature in jeu.listeDesCreatures:
        cible = creature.choisirCible(jeu)
        jeu.deplacer(creature, cible)

print("Fin du jeu.")
