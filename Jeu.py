from random import randint
from random import shuffle


class Carte(object):
    def __init__(self, valeur, couleur):
        # Initialise une carte avec une valeur et une couleur
        self.__valeur = valeur
        self.__couleur = couleur

    @property
    def valeur(self):
        # Getter pour la valeur de la carte
        return self.__valeur

    @property
    def couleur(self):
        # Getter pour la couleur de la carte
        return self.__couleur
    

class Joueur(object):
    def __init__(self, deck):
        # Initialise un joueur avec un deck et une défausse
        self.deck = deck
        self.defausse = []

    def piocher(self):
        # Pioche une carte du deck du joueur
        if not self.deck:
            shuffle(self.defausse)          # Mélange la défausse avant de piocher dedans
            return self.piocherDefausse()  # Pioche dans la défausse si le deck est vide
        if self.deck:
            return self.deck.pop()
        else:
            return None

    def piocherDefausse(self):
        # Pioche une carte de la défausse du joueur
        if self.defausse:
            return self.defausse.pop()
        else:
            return None

    def ajouterCartes(self, cartes):
        # Ajoute des cartes à la défausse du joueur
        self.defausse.extend(cartes)


    def __str__(self):
        # Affiche le contenu du deck du joueur sous forme de chaîne de caractères
        return "\n".join([f"{carte.valeur} de {carte.couleur}" for carte in self.deck])


class Jeu(object):
    def __init__(self, j1, j2, deck1, deck2):
        # Initialise le jeu avec deux joueurs et leurs decks respectifs
        self.j1 = j1
        self.j2 = j2
        self.deck1 = deck1
        self.deck2 = deck2

    def lancerTour(self):
        # Lance un tour de jeu en faisant piocher une carte à chaque joueur et en comparant ces cartes
        carte_j1 = self.j1.piocher()
        carte_j2 = self.j2.piocher()

        #Verfiie que les cartes ne sont pas nulles avant de lancer la comparaison
        if carte_j1 is not None and carte_j2 is not None:
            self.comparerCartes(carte_j1, carte_j2)

    def comparerCartes(self, c1, c2):
        # Compare les cartes jouées par les deux joueurs et met à jour les decks en conséquence
        couleurs = {0: "coeur", 1: "carreau", 2: "trefle", 3: "pique"}
        c1_couleur = couleurs[c1.couleur]
        c2_couleur = couleurs[c2.couleur]

        print(f"{c1.valeur} de {c1_couleur} vs {c2.valeur} de {c2_couleur}")

        if c1.valeur > c2.valeur:
            # Ajout des 2 cartes à la defausse du gagnant à l'issue du tour
            self.j1.ajouterCartes([c1, c2])
            print(f"-> Gagnant : j1 {len(self.j1.deck)}/{len(self.j1.defausse)}")
            print(f"-> Perdant : j2 {len(self.j2.deck)}/{len(self.j2.defausse)}")

        elif c2.valeur > c1.valeur:
            # Ajout des 2 cartes à la defausse du gagnant à l'issue du tour
            self.j2.ajouterCartes([c1, c2])
            print(f"-> Gagnant : j2 {len(self.j2.deck)}/{len(self.j2.defausse)}")
            print(f"-> Perdant : j1 {len(self.j1.deck)}/{len(self.j1.defausse)}")

        else:
            # Lance une bataille en cas d'égalité
            print("-> Bataille")
            cartes_sur_table = [c1, c2]
            self.bataille(cartes_sur_table)

    def bataille(self, cartes_sur_table):
        # Déclenche une bataille si les cartes des joueurs sont égales
        couleurs = {0: "coeur", 1: "carreau", 2: "trefle", 3: "pique"}

        while True:
            # Pioche des deux nouvelles cartes qui seront cachées
            nouvelle_carte_j1 = self.j1.piocher()
            nouvelle_carte_j2 = self.j2.piocher()

            if nouvelle_carte_j1 is None or nouvelle_carte_j2 is None:
                print("Fin de la partie : un joueur n'a plus de cartes.")
                return

            cartes_sur_table.extend([nouvelle_carte_j1, nouvelle_carte_j2])

            if nouvelle_carte_j1 is not None:
                print(f"[cartes cachées] {nouvelle_carte_j1.valeur} de {couleurs[nouvelle_carte_j1.couleur]}")
            if nouvelle_carte_j2 is not None:
                print(f"[cartes cachées] {nouvelle_carte_j2.valeur} de {couleurs[nouvelle_carte_j2.couleur]}")

            # Pioche des deux nouvelles cartes de bataille
            nouvelle_carte_j1 = self.j1.piocher()
            nouvelle_carte_j2 = self.j2.piocher()

            if nouvelle_carte_j1 is None or nouvelle_carte_j2 is None:
                print("Fin de la partie : un joueur n'a plus de cartes.")
                return

            cartes_sur_table.extend([nouvelle_carte_j1, nouvelle_carte_j2])

            if nouvelle_carte_j1 is not None:
                print(f"[nouvelles cartes de bataille] {nouvelle_carte_j1.valeur} de {couleurs[nouvelle_carte_j1.couleur]}")
            if nouvelle_carte_j2 is not None:
                print(f"[nouvelles cartes de bataille] {nouvelle_carte_j2.valeur} de {couleurs[nouvelle_carte_j2.couleur]}")

            if nouvelle_carte_j1.valeur != nouvelle_carte_j2.valeur:
                if nouvelle_carte_j1.valeur > nouvelle_carte_j2.valeur:
                    # Ajout de toutes les cartes accumulées à la defausse du gagnant à la fin de la bataille
                    self.j1.ajouterCartes(cartes_sur_table)
                    print(f"-> Gagnant : j1 {len(self.j1.deck)}/{len(self.j1.defausse)}")
                    print(f"-> Perdant : j2 {len(self.j2.deck)}/{len(self.j2.defausse)}")
                else:
                    # Ajout de toutes les cartes accumulées à la defausse du gagnant à la fin de la bataille
                    self.j2.ajouterCartes(cartes_sur_table)
                    print(f"-> Gagnant : j2 {len(self.j2.deck)}/{len(self.j2.defausse)}")
                    print(f"-> Perdant : j1 {len(self.j1.deck)}/{len(self.j1.defausse)}")
                break

    def estPartieTerminee(self):
        # Vérifie si la partie est terminée en regardant si les deux joueurs n'ont plus de cartes
        return (not self.j1.deck and not self.j1.defausse) or (not self.j2.deck and not self.j2.defausse)
