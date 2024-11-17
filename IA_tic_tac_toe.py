grille = [[' ' for _ in range(3)] for _ in range(3)]

def grille_jeu():
    for i, case in enumerate(grille):
        print(' | '.join(case))
        if i < len(grille) - 1:
            print('---------')

def grille_pleine():
    return all(case != ' ' for ligne in grille for case in ligne)

def victoire(symbole):
    for i in range(3):
        if all(grille[i][j] == symbole for j in range(3)) or all(grille[j][i] == symbole for j in range(3)):
            return True

    if grille[0][0] == grille[1][1] == grille[2][2] == symbole:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True

    return False

# Fonction Minimax
def minimax(grille, profondeur, maximiser, symbole):
    adversaire = 'O' if symbole == 'X' else 'X'

    if victoire(symbole):
        return 10 - profondeur
    if victoire(adversaire):
        return profondeur - 10
    if grille_pleine():
        return 0 

    if maximiser:
        meilleur_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if grille[i][j] == ' ':
                    grille[i][j] = symbole
                    score = minimax(grille, profondeur + 1, False, symbole)
                    grille[i][j] = ' '
                    meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        meilleur_score = float('inf')
        for i in range(3):
            for j in range(3):
                if grille[i][j] == ' ':
                    grille[i][j] = adversaire
                    score = minimax(grille, profondeur + 1, True, symbole)
                    grille[i][j] = ' '
                    meilleur_score = min(meilleur_score, score)
        return meilleur_score

# Fonction pour le coup du bot
def meilleur_coup(symbole):
    meilleur_score = -float('inf')
    coup = None

    for i in range(3):
        for j in range(3):
            if grille[i][j] == ' ':
                grille[i][j] = symbole
                score = minimax(grille, 1, False, symbole)
                grille[i][j] = ' '

                if score > meilleur_score:
                    meilleur_score = score
                    coup = (i, j)

    return coup

def jeu():
        joueur = 1  
        symbole_joueur = 'X'  
        symbole_bot = 'O'

        while True:
            grille_jeu()  
            
            if joueur == 1:
                while True:
                    try:
                        case = int(input(f"Choisissez un numéro de case (1-9) : "))
                        if case < 1 or case > 9:
                            print("Numéro de case invalide.")
                            continue
                        rangé = (case - 1) // 3
                        colonne = (case - 1) % 3
                        if grille[rangé][colonne] != ' ':
                            print("Cette case est déjà occupée.")
                            continue
                        grille[rangé][colonne] = symbole_joueur
                        break
                    except ValueError:
                        print("Entrée invalide.")
            else:
                print("Le bot joue...")
                coup = meilleur_coup(symbole_bot)
                grille[coup[0]][coup[1]] = symbole_bot

            
            if victoire(symbole_joueur):
                grille_jeu()
                print("Vous avez gagné !")
                break
            if victoire(symbole_bot):
                grille_jeu()
                print("Vous avez perdu !")  
                break
            if grille_pleine():
                grille_jeu()
                print("Match nul !")
                break

            
            joueur = 2 if joueur == 1 else 1
            symbole_joueur = 'X' if joueur == 1 else 'O'

jeu()