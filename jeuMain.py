from Jeu import *
from random import shuffle



def main():
    deck_complet = [Carte(v, c) for v in range(2, 15) for c in range(4)]
    shuffle(deck_complet)
    
    deck1 = deck_complet[:26]
    deck2 = deck_complet[26:]

    j1 = Joueur(deck1)
    j2 = Joueur(deck2)

    jeu = Jeu(j1, j2, deck1, deck2)

    while not jeu.estPartieTerminee():
        jeu.lancerTour()
        print("\n")
    
    if (not j1.deck and not j1.defausse):
        print("Le joueur 2 a gagné !")
    elif (not j2.deck  and not j2.defausse):
        print("Le joueur 1 a gagné !")
    else:
        print("Match nul !")


if __name__ == "__main__":
    main()
