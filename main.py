#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Bienvenue dans mon code ! Je vais essayer de vous expliquer pas à pas comment il fonctionne !
v1.4.3

PS : Attention, bug à signaler :
• Lorsque que le plateau est plein de pion, il se peut que l'IA se bloque
car elle ne peut pas ce déplacer naturellement !
Ce que je vous conseil si vous tester le code, c'est de commencer à jouer de C2 en C3,
normalement vous devriez pas avoir trop de souci !
'''

import os
from random import choice


# Cette fonction me permet d'actualiser le terminal dans le quel s'execute le jeu
# C'est ce qui donne cette impression de rafraichissement.
def clear() -> None:
    # Pour faire simple, quand on ouvre un terminal, on peut utiliser la commande CLS sous Windows ou clear sous
    # linux et MacOS pour supprimer l'affichage des anciennes commandes. Et c'est ce que je fais ici avec cette ligne
    # de code :
    os.system('cls' if os.name == 'nt' else 'clear')
    # Puis ici j'appelle ma Fonction banner(), qui affiche la petite bannière ACORES que vous voyez en haut du jeu.
    banner()


# Cette fonction là me permet juste d'améliorer l'affichage de mon jeu, en mettant le nombre d'espace que je veux en
# paramètre
def space(n: int) -> str:
    return ' ' * n


# Cete fonction me permet de tirer un coup aléatoire
def rand_coup() -> tuple:
    # Je récupère une lettre de manière aléatoire dans ma liste letter, qui se trouve dans mon dictionnaire en bas du
    # code.
    lettre = choice(Data['letter'])
    # Et je fais pareil ici pour les chiffres, sauf que la je mets directement la liste des chiffres ici.
    chiffre = choice(['1', '2', '3', '4', '5'])
    # Et je return l'emplacement ou ce trouve ma lettre et mon chiffre dans leur liste, par exemple :
    # Si je prends la lettre C, elle se trouve à la 2e place de ma liste (on commence à 0)
    # Et si je prend 3, il se trouve aussi à la 2e place, du coup je return (2, 2).
    return Data['letter'].index(lettre), Data['number'].index(chiffre)


# Et cette fonction me permet de savoir si un joueur veux jouer contre une IA ou pas
# J'ai fais cette fonction, dans le cas ou l'utilisateur rentre pas oui mais autre chose
# Du genre y, yes ou autre.
def getStart(answer: str) -> bool or None:
    # Ici je passe la chaine de caractère à l'entrée de ma fonction en majuscule ce qui me donne :
    # Admettons qu'en entrée de ma fonction j'ai le mot world, alors ça donnera WORLD.
    response = answer.upper()
    # Ici je crée 2 liste qui contiennent les mots clefs permettant de savoir
    # Si je joueur veux jouer contre une IA ou pas
    yes = ['OUI', 'YES', 'O', 'Y', 'U', 'I']
    no = ['NO', 'NON', 'N']

    # Et je return True or False en conséquence (Et None si la valeur n'est pas bonne).
    return True if response in yes else False if response in no else None


def getGrid(answer: str) -> int or bool:
    # Ici je fais pareil que précédement, sauf que je mets tout en minuscule (pour récupérer les accents).
    # Et je fais 3 listes, pour les grilles de début, milieu et fin.
    response = answer.lower()
    grid1 = ['start', 'début', 'debut', 'deb', 'begin', '1']
    grid2 = ['mid', 'middle', 'milieu', '2']
    grid3 = ['end', 'fin', 'last', 'derniere', 'dernière', '3']

    # Et je retourne les fonctions associé au grillen en fonction de ce que j'ai en entrée de ma fonction.
    return default() if response in grid1 else mid() if response in grid2 else end() if response in grid3 else False


def getDifficulty(answer: str) -> bool:
    # Encore une fois je fais pareil que précédement, sauf que la c'est pour la difficulté.
    response = answer.lower()
    lvl1 = ["1", "easy", "facile", "normal", "simple", "ia1", "ianaive", "ia naive"]
    lvl2 = ["2", "moyenne", "moyen", "difficile", "dur", "ia2", "iacomplexe", "ia complexe", "ia dur"]
    return True if response in lvl1 else False if response in lvl2 else None


# Ici c'est la fonction qui me permet d'afficher le mot Banner en ASCII ART
def banner() -> str:
    print("""\

   ,---.       _,.----.     _,.---._                    ,----.    ,-,--.  
 .--.'  \    .' .' -   \  ,-.' , -  `.   .-.,.---.   ,-.--` , \ ,-.'-  _\ 
 \==\-/\ \  /==/  ,  ,-' /==/_,  ,  - \ /==/  `   \ |==|-  _.-`/==/_ ,_.' 
 /==/-|_\ | |==|-   |  .|==|   .=.     |==|-, .=., ||==|   `.-.\==\  \    
 \==\,   - \|==|_   `-' \==|_ : ;=:  - |==|   '='  /==/_ ,    / \==\ -\   
 /==/ -   ,||==|   _  , |==| , '='     |==|- ,   .'|==|    .-'  _\==\ ,\  
/==/-  /\ - \==\.       /\==\ -    ,_ /|==|_  . ,'.|==|_  ,`-._/==/\/ _ | 
\==\ _.\=\.-'`-.`.___.-'  '.='. -   .' /==/  /\ ,  )==/ ,     /\==\ - , / 
 `--`                       `--`--''   `--`-`--`--'`--`-----``  `--`---'  

""")


# Cette fonction me permet d'afficher le jeu.
def load_grid(grille: list) -> None:
    # Ici je fais appel à ma fonction clear, qui me permet de supprimer tout ce qui a dans le terminal.
    clear()
    # Je crée une "mini" fonction, qui me permet de récupérer le pion associé à un joueur.
    pion_player = lambda p: Data["player"][p]['pion']
    # Et la 2 variables me permttant de récupérer les scores.
    player1 = f'Score : {Data["player"][0]["score"]}'
    player2 = f'Score : {Data["player"][1]["score"]}'

    # Ici je fais une boucle pour afficher toute la grille, en utilisant une variable d'incrémentation 'i',
    # Pour calculer à quel endroit va tomber le "scoreboard".
    print(f"\n{space(25)}1   2   3   4   5")
    for i, cases in enumerate(grille):
        print(f"{space(23)}┌───┬───┬───┬───┬───┐") if i == 0 else print(f"{space(23)}├───┼───┼───┼───┼───┤     "
                                                                        f"{'Joueur 1 : Bleu' if i == 1 else player2 if i == 3 else ''}")
        print(
            f"{space(20)}{Data['letter'][i]}  │ {cases[0]} │ {cases[1]} │ {cases[2]} │ {cases[3]} │ {cases[4]} │     "
            f"{player1 if i == 1 else 'Joueur 2 : Rouge' if i == 2 else ''}")
        print(f"{space(23)}└───┴───┴───┴───┴───┘") if i == 4 else None

    # Et ici tout simplement, j'affiche le nombre de pion restant sur le plateau, et le dernier coup jouer par l'IA (
    # Si y'en à un)
    print(
        f"\n{space(28)}Il reste :\n{space(31)}{pion_left(grille, pion_player(0))} {pion_player(0)}\n{space(31)}{pion_left(grille, pion_player(1))} {pion_player(1)}")
    if Data['iaAffichage']:
        print(
            f"\n\n{space(20)}Dernier coup joué par l'IA :\n{space(27)}{afficher_coordonnes(Data['lastSelec'])} -> {afficher_coordonnes(Data['lastTarget'])}")


#

# Cette fonction me permet d'initialiser la grille par défaut.
def default() -> list:
    # Ici tout simplement je fais du one-liner, pour remplir efficacement un Array
    # Pour faire un plateau de jeu par défaut.
    grille = [[Data['player'][0]['pion']] * 5 for _ in range(2)]
    [grille.append([Data['player'][0]['pion']] * 2 + [" "] + [Data['player'][1]['pion']] * 2)]
    [grille.append([Data['player'][1]['pion']] * 5) for _ in range(2)]

    # Et j'initialise les scoreboards
    for i in range(2):
        Data['player'][i]['score'] = 0

    return grille


# Ici je crée juste une grille de milieu de partie.
def mid() -> list:
    J1 = Data['player'][0]['pion']
    J2 = Data['player'][1]['pion']
    midGrid = [[J1, J1, ' ', ' ', J1],
               [' ', J2, J1, ' ', J2],
               [J2, ' ', J2, ' ', J2],
               [' ', J1, ' ', J1, ' '],
               [J2, ' ', ' ', J2, J1]]

    return midGrid


# Et la je fais une grille de fin de partie.
def end() -> list:
    J1 = Data['player'][0]['pion']
    J2 = Data['player'][1]['pion']
    endGrid = [[' ', ' ', J1, ' ', ' '],
               [' ', ' ', ' ', ' ', ' '],
               [J1, ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', J2, ' '],
               [' ', J2, ' ', ' ', ' ']]

    return endGrid


# Et cette fonction me permet de retourner l'enemy d'un joueur.
def enemy(player: str) -> int:
    return 1 if player == 0 else 0


# Cette fonction me permet de voir si une case est vide ou non.
def is_void(grille: list, coordinates: tuple) -> bool:
    # Pour ça, je récupère la ligne et la colonne de mon tuple en entrée de ma Fonction.
    line, column = coordinates
    # Et je retourne le booléen qui vérifie si grille à la ligne et la colonne si dessus
    # Est vide.
    return bool(grille[line][column] == " ")


# Comme son nom l'indique, elle me permet de savoir si le joueur passer en entrée
# Possède bien le pion qui est sur la case passer en entrée
def is_same_player(grille: list, player: int, coordinates: tuple) -> bool:
    # Pour ça je récupère la case (Ligne et colonne)
    line, column = coordinates
    # Je récupère le pion associé au player en entrée de ma fonction
    current = Data['player'][player]['pion']
    # Et je retourne le booléen associé à ceci;
    return current == grille[line][column]


# Cette fonction me permet de regarder si ce que l'utilisateur rentre est sous le bon format
def is_in_grid(response: str) -> bool:
    # Je vérifie que ce rentre l'utilisateur comporte bien 2 caractères
    if len(response) != 2:
        return False
    # Puis je regarde si ils sont dans mes deux listes, lettre et chiffres.
    return (response[0] in Data['letter'] or response[0] in Data['mini']) and response[1] in Data['number']


# Celle ci me permet de mettre du vide, à l'endroit ou c'est fais manger un pion
def add_void_catch(grille: list, coordinates: tuple, x: int, y: int) -> list:
    # Ici je supprime juste un pion, cette fonction me permet en réalité
    # De supprimer un pion qui se fait manger
    line, column = coordinates
    # Pour celà je récupère les coordonnées d'orine du pion qui va être déplacer.
    grille[line + x][column + y] = " "
    # Je récupère le delta (x et y ) associé, et j'addtione le tout pour le supprimer
    # Et retourner la grille, cette explication et un peu compliquer. Mais elle est détailler
    # Plus en bas, vous comprendez juste en dessous.
    return grille


# CEtte fonction me permet de voir si un pion peu être manger ou pas
def catch_pion(grille: list, enemy: int, fromCoordinates: tuple, toCoordinates: tuple) -> int:
    # Ici je crée une variable d'incrémentation, qui me permet de savoir dans quel direction un pion peut être manger,
    # Diagonale, horizontal, vertical, gauche, droite etc..
    i = 0
    # Je récupère les x et y de la coordonnées de début et d'arrivée.
    fromLine, fromColumn = fromCoordinates
    toLine, toColumn = toCoordinates
    # Et je récupère la taille max de ma grille, ça me sert pour l'encadrement de mes coups.
    tailleMax = len(grille)

    # Enfin je récupère le pion enemie.
    opponent = Data['player'][enemy]['pion']

    # Ici, je récupère ma liste de delta, pour faire simple, dans ma DB (Base de Données, ici représenté par un
    # dictionnaire), je crée des couples (delta) qui me permettent d'étudier chaque direction, La diagonale en bas à
    # droite (++) la diagonale en bas à gauche (-+), la diag en haut à gauche (--) la diagonale en haut à droite( +-)
    # et pareil pour vertical et horizontal. Ces couples me permettent, en fonction des coordonnées de départ,
    # d'aller vérifier, si en fonction des coordonnées de départ plus le delta, si il y a une case vide ou pas,
    # et ensuite je récupère une deuxième couple de delta, qui me permet de voir autour de mon pion initial voir
    # si je peux il y a quelqu'un à manger Démonstration :
    for dx, dy in Data['deltaCatch']:
        # Je récupère le premier couple de deltas
        Line, Column = (fromLine + dx), (fromColumn + dy)
        # Je crée 2 variables au quel j'additionne, la ligne et la colonne de départ, avec le delta.
        LineInf, ColumnInf = (fromLine + Data['deltas'][i][0]), (fromColumn + Data['deltas'][i][1])
        # Et la je fais pareil avec l'autre couple de delta (le précédent étant un delta de 2 et ici un delta de 1)

        # Je fais un encadrement, pour être sur que le déplacement se situe bien dans la grille
        if (0 <= Line < tailleMax) and (0 <= Column < tailleMax) and (0 <= LineInf < tailleMax) and (
                0 <= ColumnInf < tailleMax):
            # Je regarde avec le delta de 1, si le pion autour de moi est bien un enemy
            if grille[LineInf][ColumnInf] == opponent:
                # Si c'est le cas, je regarde derrière si il y a du vide
                if grille[Line][Column] == " ":
                    # Et si c'est le cas, je vérifie si ma ligne et ma colonne de départ au quel j'ai ajouté mon
                    # delta de 2, correspondent à ma ligne et colonne d'arrive, sinon ça fait une erreur et je ne
                    # sais toujours pas pourquoi x)
                    if Line == toLine and Column == toColumn:
                        # Dans ce cas là, je retourne le i associé au coups (si c'est une diagonale, vertical etc...)
                        return i + 1
        i += 1
    # Et si aucun déplacement n'est possible, je retourne -1 pour dire que rien n'est possible.
    return -1


# Cette fonction me permet simplement de pouvoir voir si il y a une case libre autour d'un pion donné
def est_jouable(fromCoordinates: tuple, toCoordinates: tuple) -> bool:
    # Ici je récupère la ligne et colonne de départ et d'arrivé
    fromLine, fromColumn = fromCoordinates
    toLine, toColumn = toCoordinates

    # Et je fais un calcul, je calcul la valeur absolue de la ligne de départ - la ligne d'arrivée Et si la réponse
    # est <= à 1 ça veut bien dire que la case est autour de moi, et ensuite je fais pareil avec la colonne Et je
    # regarde si les deux sont vraie et je retourne le booléen en conséquence.
    return bool(True if abs(fromLine - toLine) <= 1 and abs(fromColumn - toColumn) <= 1 else False)


# Et la c'est la même chose, sauf que c'est pour l'IA
def case_void_arround_ia(grille: list, coordinates: tuple) -> bool:
    # Ici je récupère encore une fois la ligne et colonne de départ
    line, column = coordinates
    for _ in range(len(Data['deltas'])):
        # Et pour tout les deslta de 1, je regarde si la case est vide.
        x, y = Data['deltas'][_]
        a = line + x
        b = column + y
        if 0 <= a <= 4 and 0 <= b <= 4:
            if grille[a][b] == " ":
                return True

    return False


# Ici c'te fonction demande à l'utilisateur de saisir une coordonnée
def saisir_coordonnees(grille: list, player: int, action: str) -> tuple:
    # J'affiche en premier temps la grille
    load_grid(grille)
    # Ici simple vérification pour voir si le player en entrée et bon (sinon j'ai fais une erreur)
    # Et je récupère les messages correspondants
    message = Data['message'].get(action, lambda x: "No message found")(player)

    # Je demande au joueur de saisir les coordonnées
    answer = input(message)
    # Je regarde si elle est valide
    valide = is_in_grid(answer)
    while not valide:
        load_grid(grille)

        answer = input(Data['message']['error'](player))
        valide = is_in_grid(answer)

    # Et enfin je retourne les coordonnées sous la forme de 2 entier (j'ai expliqué le fonctionnement de la fonction
    # index plus haut
    return (Data['letter'] if answer[0] in Data['letter'] else Data['mini']).index(answer[0]), Data['number'].index(
        answer[1])


def afficher_coordonnes(coordonnee: tuple) -> str or None:
    # Cette fonction me permet juste de convertir les 2 entier en coordonnées sous la forme 'A1'
    x, y = coordonnee
    if x is None or y is None:
        return None
    valX = Data['letter'][x]
    valY = Data['number'][y]
    return f"{valX}{valY}"


# Cette fonction me permet d'augmenter le score
def update_score(player: int, add: int) -> bool:
    # Ici je récupère le player, et j'incrémente son score
    Data['player'][player]['score'] += add
    return True


# Et ici voilà la fonction principale qui gère le tour de chaque joueur
def tour_joueur(grille: list, player: int, IA: bool = False) -> list:
    # C'est ici que ce joue le gros du code, par défaut, j'ai initialise ma variable IA à false
    # Donc quand j'appelle ma fonction, si il n'y a pas d'IA, je l'appelle comme ça : tour_joueur(grille, player)
    # Mais s'il ya  une IA, je l'appelle comme ça : tour_joueur(grille, player, True)
    # Et je vérifie si il y a une IA
    if IA:
        # Alors je génère un coup aléatoire et je vérifie qu'il est correct
        fromCoordinates = rand_coup()
        isPossibleFrom = is_same_player(grille, player, fromCoordinates) and case_void_arround_ia(grille,
                                                                                                  fromCoordinates)

        while not isPossibleFrom:
            fromCoordinates = rand_coup()
            isPossibleFrom = is_same_player(grille, player, fromCoordinates) and case_void_arround_ia(grille,
                                                                                                      fromCoordinates)
        # J'update mon dico, en mettant à jour le dernier coup jouer par l'IA
        Data['lastSelec'] = fromCoordinates
    else:
        # Sinon je demande ou joueur de saisir un pion et je vérifie s'il est coorect
        fromCoordinates = saisir_coordonnees(grille, player, 'get')
        isPossibleFrom = is_same_player(grille, player, fromCoordinates)

        while not isPossibleFrom:
            fromCoordinates = saisir_coordonnees(grille, player, 'error')
            isPossibleFrom = is_same_player(grille, player, fromCoordinates)

    fromLine, fromColumn = fromCoordinates
    # Et la je change la couleur du pion jouer par le player, pour une meilleur visibilité
    grille[fromLine][fromColumn] = "○"

    if IA:
        # Ensuite, je génère le coup aléatoire, en fonction de ce que joue l'IA et je regarde que ça reste valide
        toCoordinates = rand_coup()
        catchPionValue = catch_pion(grille, enemy(player), fromCoordinates, toCoordinates)
        isPossibleTo = is_void(grille, toCoordinates) and case_void_arround_ia(grille, fromCoordinates) and (
                est_jouable(fromCoordinates, toCoordinates) or catchPionValue != -1)
        while not isPossibleTo:
            toCoordinates = rand_coup()
            catchPionValue = catch_pion(grille, enemy(player), fromCoordinates, toCoordinates)
            isPossibleTo = is_void(grille, toCoordinates) and case_void_arround_ia(grille, fromCoordinates) and (
                    est_jouable(fromCoordinates, toCoordinates) or catchPionValue != -1)
        # et encore une fois je mets à jour le dernier coup qu'elle à jouer
        Data['lastTarget'] = toCoordinates
    else:
        # Et je fais pareil pour le player
        toCoordinates = saisir_coordonnees(grille, player, 'to')
        catchPionValue = catch_pion(grille, enemy(player), fromCoordinates, toCoordinates)
        isPossibleTo = is_void(grille, toCoordinates) and (
                est_jouable(fromCoordinates, toCoordinates) or catchPionValue != -1)
        while not isPossibleTo:
            toCoordinates = saisir_coordonnees(grille, player, 'to')
            catchPionValue = catch_pion(grille, enemy(player), fromCoordinates, toCoordinates)
            isPossibleTo = is_void(grille, toCoordinates) and (
                    est_jouable(fromCoordinates, toCoordinates) or catchPionValue != -1)

    toLine, toColumn = toCoordinates

    # Et ici je regarde simplement si la case choisie par l'utilisateur, peut être manger, et si c'est le cas
    # Je mange,
    if catchPionValue != -1:
        dx, dy = Data['deltas'][catchPionValue - 1]
        # print(dx, dy)
        if 0 <= fromLine + dx <= 5 and 0 <= fromColumn + dy <= 5:
            add_void_catch(grille, fromCoordinates, dx, dy)
            grille[toLine][toColumn] = Data['player'][player]['pion']
            grille[fromLine][fromColumn] = " "
            update_score(player, 1)

    # Sinon je fais un déplacement simple
    else:
        grille[fromLine][fromColumn] = " "
        grille[toLine][toColumn] = Data['player'][player]['pion']

    return grille


# Cette fonction me per met de retourner le nombre de pion sur le plateau !
def pion_left(grille: list, player: str) -> int:
    compt = 0
    # Ici je fais une boucle pour récupérer le nombre de pion sur le plateau
    for x in range(len(grille)):

        for y in range(len(grille[0])):

            if grille[x][y] == player:
                compt += 1

    return compt


# Et cette fonction me permet de savoir si le jeu est fini
def gameFinished(grille: list) -> bool:
    # Et ici j'utilise la fonction précédent pour voir si le jeu est fini
    pion1 = pion_left(grille, Data['player'][0]['pion'])
    pion2 = pion_left(grille, Data['player'][1]['pion'])

    if pion1 >= 1 and pion2 >= 1:
        return False
    return True


# Et c'te fonction me permet d'afficher le gagnant !
def load_end_game(winner: int) -> None:
    # La je fais un petit affichage sympa pour le gagnant.
    clear()
    print(f"""               ┌──────────────────────────────────┐
               │   {f"Joueur {winner + 1} {Data['player'][winner]['pion']} vous avez gagné !"}   │
               └──────────────────────────────────┘
    """)


# Et voilà la fonction qui permet de dérouler le jeu
def game(game, IA: bool = False) -> None:
    # Et voilà comment ce déroule la partie.
    player = 0

    while not (gameFinished(game)):
        if IA and player == 1:
            tour_joueur(game, player, True)
        else:
            tour_joueur(game, player)
        player = enemy(player)
    player = enemy(player)
    load_end_game(player)


# Voilà ma "BD", mon petit dictionnaire que j'utilise tout au long du code.
Data = {
    "letter": ["A", "B", "C", "D", "E"],
    "mini": ["a", "b", "c", "d", "e"],
    "number": ["1", "2", "3", "4", "5"],
    "deltas": [(+1, +1), (-1, -1), (+1, -1), (-1, +1), (-1, 0), (+1, 0), (0, +1), (0, -1)],
    "deltaCatch": [(+2, +2), (-2, -2), (+2, -2), (-2, +2), (-2, 0), (+2, 0), (0, +2), (0, -2)],
    "lastSelec": (None, None),
    "lastTarget": (None, None),
    "iaAffichage": False,
    "player": {
        0: {
            "pion": "\033[34m●\033[0m",
            "score": 0
        },
        1: {
            "pion": "\033[31m●\033[0m",
            "score": 0
        }
    },
    "message": {
        "get": lambda
            player: f"\n{space(15)}Joueur {player + 1} ({Data['player'][player]['pion']}), c'est a votre tour !\n{space(13)}Entez les coordonnés du pion à déplacer : ",
        "to": lambda player: f"\n{space(14)}Entrez les coordonnés d'arrivée du pion à déplacer : ",
        "error": lambda
            player: f"\n{space(13)}Joueur {player + 1} ({Data['player'][player]['pion']}), coordonnés sont invalides ... \n{space(14)}Saisissez de nouvelles coordonnées : "
    }
}

# Enfin j'actualise le terminale
clear()

# Je crée des textes pour toute mes demandes quand l'utilsateur lance le code.
iaText = f"{space(19)}Veux tu jouer contre un ordinateur ?\n{space(27)}(Oui / Non) : "
gridText = f"{space(20)}Sur quelle grille veux tu jouer :\n\n{space(27)}[1] : Grille N°1\n{space(27)}[2] : Grille N°2\n{space(27)}[3] : Grille N°3\n\n{space(21)}Saisie ta réponse : "
iaDifficulty = f"{space(20)}Avec quel niveau de difficulté :\n\n{space(27)}[1] : Difficulté 1\n{space(27)}[2] : Difficulté 2\n\n{space(21)}Saisie ta réponse : "

# En premier lieu je lui demande s'il veut jouer contre une IA et j'attends une réponse valide.
ia = input(iaText)
while getStart(ia) is None:
    ia = input(iaText)
clear()

# Puis sur quelle grille il veut jouer
gridType = input(gridText)
while getGrid(gridType) is None:
    gridType = input(gridText)
clear()

# Et enfin s'il joue contre une IA, avec quel niveau de difficulté.
if getStart(ia):
    Data['iaAffichage'] = True
    difficulty = input(iaDifficulty)
    if getDifficulty(difficulty) == 1:
        game(getGrid(gridType), True)
    else:
        game(getGrid(gridType), True)
else:
    game(getGrid(gridType))
