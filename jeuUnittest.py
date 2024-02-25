

import unittest
from random import shuffle
from Jeu import Carte, Joueur, Jeu

class TestCarte(unittest.TestCase):
    def test_creation_carte(self):
        carte = Carte(10, 0)
        self.assertEqual(carte.valeur, 10)
        self.assertEqual(carte.couleur, 0)

    def test_piocher(self):
        deck = [Carte(2, 0), Carte(3, 1), Carte(4, 2)]
        joueur = Joueur(deck)
        carte_piochee = joueur.piocher()
        self.assertEqual(carte_piochee.valeur, 4)
        self.assertEqual(carte_piochee.couleur, 2)

    def test_ajouter_cartes(self):
        deck = [Carte(2, 0), Carte(3, 1)]
        joueur = Joueur(deck)
        joueur.ajouterCartes([Carte(4, 2), Carte(5, 3)])
        self.assertEqual(joueur.defausse[0].valeur, 4)
        self.assertEqual(joueur.defausse[0].couleur, 2)
        self.assertEqual(joueur.defausse[1].valeur, 5)
        self.assertEqual(joueur.defausse[1].couleur, 3)


class TestJeu(unittest.TestCase):
    def test_comparerCartes(self):
        j1 = Joueur([])
        j2 = Joueur([])
        jeu = Jeu(j1, j2, [], [])

        c1 = Carte(10, 0)
        c2 = Carte(5, 1)

        jeu.comparerCartes(c1, c2)
        self.assertIn(c1, j1.defausse)
        self.assertIn(c2, j1.defausse)

    def test_estPartieTerminee(self):
        j1 = Joueur([])
        j2 = Joueur([])
        jeu = Jeu(j1, j2, [], [])

        self.assertTrue(jeu.estPartieTerminee())

if __name__ == "__main__":
    unittest.main()
