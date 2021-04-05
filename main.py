#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Bienvenue dans mon code ! Je vais essayer de vous expliquer pas à pas comment il fonctionne !
v1.4.3

PS : Attention, bug à signaler :
• Lorsque que le plateau est plein de pion, il se peut que l'IA se bloque
car elle ne peut pas ce déplacer naturellement !
ce que je vous conseil si vous tester le code, c'est de commencer à jouer de C2 en C3,
normalement vous devriez pas avoir trop de souci !
'''

import os
from random import choice


# Cette fonction me permet d'actualiser le terminal dans le quel s'execute le jeu
# C'est ce qui donne cette impression de rafraichissement.


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()

def space(n: int) -> str:
    return ' '*n


# Cete fonction me permet de tirer un coup aléatoire
def rand_coup() -> tuple:
    lettre = choice(Data['letter'])
    chiffre = choice(['1', '2', '3', '4', '5'])

    return Data['letter'].index(lettre), Data['number'].index(chiffre)


# Et cette fonction me permet de savoir si un joueur veux jouer contre une IA ou pas
# J'ai fais cette fonction, dans le cas ou l'utilisateur rentre pas oui mais autre chose
# Du genre y, yes ou autre.


def start(answer: str) -> int or bool:
    response = answer.upper()
    yes = ['OUI', 'YES', 'O', 'Y', 'U', 'I']
    no = ['NO', 'NON', 'N']

    return 1 if response in yes else 0 if response in no else False


def gridChoice(answer: str) -> int or bool:
    response = answer.lower()
    grid1 = ['start', 'début', 'debut', 'deb', 'begin', '1']
    grid2 = ['mid', 'middle', 'milieu', '2']
    grid3 = ['end', 'fin', 'last', 'derniere', 'dernière', '3']

    return default() if response in grid1 else mid() if response in grid2 else end() if response in grid3 else False


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
    clear()

    pion_player = lambda p: Data["player"][p]['pion']
    player1 = f'Score : {Data["player"][0]["score"]}'
    player2 = f'Score : {Data["player"][1]["score"]}'

    print(f"\n{space(25)}1   2   3   4   5")
    for i, cases in enumerate(grille):
        print(f"{space(23)}┌───┬───┬───┬───┬───┐") if i == 0 else print(f"{space(23)}├───┼───┼───┼───┼───┤     "
                                                                        f"{'Joueur 1 : Bleu' if i == 1 else player2 if i == 3 else ''}")
        print(
            f"{space(20)}{Data['letter'][i]}  │ {cases[0]} │ {cases[1]} │ {cases[2]} │ {cases[3]} │ {cases[4]} │     "
            f"{player1 if i == 1 else 'Joueur 2 : Rouge' if i == 2 else ''}")
        print(f"{space(23)}└───┴───┴───┴───┴───┘") if i == 4 else None

    print(
        f"\n{space(28)}Il reste :\n{space(31)}{pion_left(grille, pion_player(0))} {pion_player(0)}\n{space(31)}{pion_left(grille, pion_player(1))} {pion_player(1)}")


# Cette fonction me permet d'initialiser la grille par défaut.
def default() -> list:
    grille = [[Data['player'][0]['pion']] * 5 for _ in range(2)]
    [grille.append([Data['player'][0]['pion']] * 2 + [" "] + [Data['player'][1]['pion']] * 2)]
    [grille.append([Data['player'][1]['pion']] * 5) for _ in range(2)]

    for i in range(2):
        Data['player'][i]['score'] = 0

    return grille


def mid() -> list:
    J1 = Data['player'][0]['pion']
    J2 = Data['player'][1]['pion']
    midGrid = [[J1, J1, ' ', ' ', J1],
               [' ', J2, J1, ' ', J2],
               [J2, ' ', J2, ' ', J2],
               [' ', J1, ' ', J1, ' '],
               [J2, ' ', ' ', J2, J1]]

    return midGrid


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
    line, column = coordinates
    return bool(grille[line][column] == " ")


# Comme son nom l'indique, elle me permet de savoir si le joueur passer en entrée
# Est bien le joueur sur le plateau
def is_same_player(grille: list, player: int, coordinates: tuple) -> bool:
    line, column = coordinates
    current = Data['player'][player]['pion']
    return current == grille[line][column]


# Cette fonction me permet de regarder si ce que l'utilisateur rentre est sous le bon format
def is_in_grid(response: str) -> bool:
    if len(response) != 2:
        return False

    return (response[0] in Data['letter'] or response[0] in Data['mini']) and response[1] in Data['number']


# Celle ci me permet de mettre du vide, à l'endroit ou c'est fais manger un pion
def add_void_catch(grille: list, coordinates: tuple, x: int, y: int) -> list:
    line, column = coordinates
    grille[line + x][column + y] = " "
    return grille


# CEtte fonction me permet de voir si un pion peu être manger ou pas
def catch_pion(grille: list, enemy: int, fromCoordinates: str, toCoordinates) -> int:
    fromLine, fromColumn = fromCoordinates
    toLine, toColumn = toCoordinates

    opponent = Data['player'][enemy]['pion']

    if fromLine <= 2 and fromColumn <= 2:
        if grille[fromLine + 1][fromColumn + 1] == opponent:
            if grille[fromLine + 2][fromColumn + 2] == " ":
                if fromColumn + 2 == toColumn and fromLine + 2 == toLine:
                    return 1

    if fromLine >= 2 and fromColumn >= 2:
        if grille[fromLine - 1][fromColumn - 1] == opponent:
            if grille[fromLine - 2][fromColumn - 2] == " ":
                if fromColumn - 2 == toColumn and fromLine - 2 == toLine:
                    return 2

    if fromLine <= 2 <= fromColumn:
        if grille[fromLine + 1][fromColumn - 1] == opponent:
            if grille[fromLine + 2][fromColumn - 2] == " ":
                if fromColumn - 2 == toColumn and fromLine + 2 == toLine:
                    return 3

    if fromLine >= 2 >= fromColumn:
        if grille[fromLine - 1][fromColumn + 1] == opponent:
            if grille[fromLine - 2][fromColumn + 2] == " ":
                if fromColumn + 2 == toColumn and fromLine - 2 == toLine:
                    return 4

    if fromLine >= 2:
        if grille[fromLine - 1][fromColumn] == opponent:
            if grille[fromLine - 2][fromColumn] == " ":
                if fromColumn == toColumn and fromLine - 2 == toLine:
                    return 5

    if fromLine <= 2:
        if grille[fromLine + 1][fromColumn] == opponent:
            if grille[fromLine + 2][fromColumn] == " ":
                if fromColumn == toColumn and fromLine + 2 == toLine:
                    return 6

    if fromColumn <= 2:
        if grille[fromLine][fromColumn + 1] == opponent:
            if grille[fromLine][fromColumn + 2] == " ":
                if fromColumn + 2 == toColumn and fromLine == toLine:
                    return 7

    if fromColumn >= 2:
        if grille[fromLine][fromColumn - 1] == opponent:
            if grille[fromLine][fromColumn - 2] == " ":
                if fromColumn - 2 == toColumn and fromLine == toLine:
                    return 8
    return -1


# Cette fonction me permet simplement de pouvoir voir si il y a une case libre autour d'un pion donné
def est_jouable(fromCoordinates: tuple, toCoordinates: tuple) -> bool:
    fromLine, fromColumn = fromCoordinates
    toLine, toColumn = toCoordinates

    return bool(True if abs(fromLine - toLine) <= 1 and abs(fromColumn - toColumn) <= 1 else False)


# Et la c'est la même chose, sauf que c'est pour l'IA
def case_void_arround_ia(grille: list, coordinates: tuple) -> bool:
    line, column = coordinates
    for _ in range(len(Data['deltas'])):
        x, y = Data['deltas'][_]
        a = line + x
        b = column + y
        if 0 <= a <= 4 and 0 <= b <= 4:
            if grille[a][b] == " ":
                return True

    return False


# Ici c'te fonction demande à l'utilisateur de saisir une coordonnée
def saisir_coordonnees(grille: list, player: int, action: str) -> tuple:
    load_grid(grille)
    message = Data['message'].get(action, lambda x: "No message found")(player)

    answer = input(message)
    valide = is_in_grid(answer)
    while not valide:
        load_grid(grille)

        answer = input(Data['message']['error'](player))
        valide = is_in_grid(answer)

    return (Data['letter'] if answer[0] in Data['letter'] else Data['mini']).index(answer[0]), Data['number'].index(answer[1])


# Cette fonction me permet d'augmenter le score
def update_score(player: int, add: int) -> bool:
    Data['player'][player]['score'] += add
    return True


# Et ici voilà la fonction principale qui gère le tour de chaque joueur
def tour_joueur(grille: list, player: int, IA: bool = False) -> list:
    if IA:
        fromCoordinates = rand_coup()
        isPossibleFrom = is_same_player(grille, player, fromCoordinates) and case_void_arround_ia(grille,
                                                                                                  fromCoordinates)

        while not isPossibleFrom:
            fromCoordinates = rand_coup()
            isPossibleFrom = is_same_player(grille, player, fromCoordinates) and case_void_arround_ia(grille,
                                                                                                      fromCoordinates)
    else:
        fromCoordinates = saisir_coordonnees(grille, player, 'get')
        isPossibleFrom = is_same_player(grille, player, fromCoordinates)

        while not isPossibleFrom:
            fromCoordinates = saisir_coordonnees(grille, player, 'error')
            isPossibleFrom = is_same_player(grille, player, fromCoordinates)

    fromLine, fromColumn = fromCoordinates
    grille[fromLine][fromColumn] = "○"

    if IA:
        toCoordinates = rand_coup()
        catchPionValue = catch_pion(grille, enemy(player), fromCoordinates, toCoordinates)
        isPossibleTo = is_void(grille, toCoordinates) and case_void_arround_ia(grille, fromCoordinates) and (
                    est_jouable(fromCoordinates, toCoordinates) or catchPionValue != -1)
        while not isPossibleTo:
            toCoordinates = rand_coup()
            catchPionValue = catch_pion(grille, enemy(player), fromCoordinates, toCoordinates)
            isPossibleTo = is_void(grille, toCoordinates) and case_void_arround_ia(grille, fromCoordinates) and (
                        est_jouable(fromCoordinates, toCoordinates) or catchPionValue != -1)
    else:
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

    if catchPionValue != -1:
        dx, dy = Data['deltas'][catchPionValue - 1]
        print(dx, dy)
        if 0 <= fromLine + dx <= 5 and 0 <= fromColumn + dy <= 5:
            add_void_catch(grille, fromCoordinates, dx, dy)
            grille[toLine][toColumn] = Data['player'][player]['pion']
            grille[fromLine][fromColumn] = " "
            update_score(player, 1)

    else:
        grille[fromLine][fromColumn] = " "
        grille[toLine][toColumn] = Data['player'][player]['pion']

    return grille


# Cette fonction me per met de retourner le nombre de pion sur le plateau !
def pion_left(grille: list, player: str) -> int:
    compt = 0
    for x in range(len(grille)):

        for y in range(len(grille[0])):

            if grille[x][y] == player:
                compt += 1

    return compt


# Et cette fonction me permet de savoir si le jeu est finis
def gameFinished(grille: list) -> bool:
    pion1 = pion_left(grille, Data['player'][0]['pion'])
    pion2 = pion_left(grille, Data['player'][1]['pion'])

    if pion1 >= 1 and pion2 >= 1:
        return False
    return True


# Et c'te fonction me permet d'afficher le gagnant !
def load_end_game(winner: int) -> None:
    clear()
    print(f"""               ┌──────────────────────────────────┐
               │   {f"Joueur {winner + 1} {Data['player'][winner]['pion']} vous avez gagné !"}   │
               └──────────────────────────────────┘
    """)


# Et voilà la fonction qui permet de dérouler le jeu
def game(game, IA: bool = False) -> None:
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

# Et la je demande juste à l'utilisateur s'il veut jouer contre une IA
clear()
iaText = f"{space(19)}Veux tu jouer contre un ordinateur ?\n{space(27)}(Oui / Non) : "
gridText = f"{space(20)}Sur quelle grille veux tu jouer :\n\n{space(27)}[1] : Grille N°1\n{space(27)}[2] : Grille N°2\n{space(27)}[3] : Grille N°3\n\n{space(21)}Saisie ta réponse : "
ia = input(iaText)
while not start(ia):
    ia = input(iaText)
clear()
gridType = input(gridText)
while not gridChoice(gridType):
    gridType = input(gridText)
if start(ia) == 1:
    game(gridChoice(gridType), True)
else:
    game(gridChoice(gridType))
