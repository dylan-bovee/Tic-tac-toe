# Grille initiale (vide)
grille = [[' ' for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def grille_jeu():
    for i, case in enumerate(grille):
        print(' | '.join(case))
        if i < len(grille) - 1:
            print('---------')

# Fonction pour déterminer si la grille est pleine
def grille_pleine():
    for case in grille:
        if ' ' in case:
            return False
    return True

# Fonction qui va nous permettre de sélectionner une case
# Fonction qui va nous permettre de sélectionner une case via un numéro entre 1 et 9
def jouer(joueur, symbole_joueur):
    while True:
        try:
            
            # Demander à l'utilisateur de choisir une case (1-9)
            case = int(input(f"Joueur {joueur}, choisissez un numéro de case (1-9) : "))

            # Vérifier si le numéro de la case est valide
            if case < 1 or case > 9:
                print("Numéro de case invalide. Veuillez choisir un numéro entre 1 et 9.")
                continue

            # Convertir le numéro de la case en indices de ligne et colonne
            rangé = (case - 1) // 3  # Détermine la ligne
            colonne = (case - 1) % 3  # Détermine la colonne

            # Vérifier si la case est déjà occupée
            if grille[rangé][colonne] != ' ':
                print("Cette case est déjà occupée. Choisissez-en une autre.")
                continue

            # Placer le symbole du joueur dans la case choisie
            grille[rangé][colonne] = symbole_joueur
            break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre pour la case.")


# Vérification des conditions de victoire
def victoire():
    # Vérification des lignes et colonnes
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] and grille[i][0] != ' ':
            return True
        if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] != ' ':
            return True

    # Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != ' ':
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] != ' ':
        return True

    return False

# Fonction pour réinitialiser la grille
def grille_vierge():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Fonction pour demander si on veut relancer la partie
def relancer_partie():
    while True:
        reponse = input("Voulez-vous relancer une partie ? (oui/non) : ").strip().lower()
        if reponse in ['oui', 'o']:
            return True
        elif reponse in ['non', 'n']:
            print("Merci d'avoir joué ! À bientôt.")
            return False
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")

# Fonction principale pour dérouler le jeu
def jeu():
    while True:
        grille = grille_vierge()  # Réinitialiser la grille
        joueur = 1
        symbole_joueur_1 = 'X'
        symbole_joueur_2 = 'O'
        
        while True:
            # Affichage de la grille avant chaque tour
            grille_jeu()

            # Sélection du symbole du joueur
            if joueur == 1:
                symbole_joueur = symbole_joueur_1
            else:
                symbole_joueur = symbole_joueur_2

            # Le joueur fait son coup
            jouer(joueur, symbole_joueur)

            # Vérification des conditions de victoire
            if victoire():
                grille_jeu()  # Afficher la grille après un coup gagnant
                print(f"Joueur {joueur} a gagné !")
                break

            # Vérification de l'égalité (grille pleine)
            if grille_pleine():
                grille_jeu()  # Afficher la grille après un match nul
                print("La partie est terminée, il y a égalité !")
                break
            
            # Changer de joueur
            joueur = 2 if joueur == 1 else 1  # Alterner entre joueur 1 et joueur 2

        # Demander si on veut relancer la partie
        if not relancer_partie():
            break

# Appel de la fonction pour commencer la partie
jeu()
