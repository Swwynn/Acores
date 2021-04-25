# Acores Project v5

## But du jeu :
Le principe du jeu, est de manger tout les pions adverses, afin qu'il ne reste plus qu'un joueur sur le plateau de jeu.

## Règles du jeu :

> Types de déplacements :
> - **Simple** : Tu peux déplacer un pion, d'une seule case, dans la direction de ton choix, du moment que la case est vide.
> - **Saut** : Tu peux "manger" un pion ennemi, pour cela, si il y a un pion ennemi autour de toi, et que derrière ce pion, se trouve une case vide, alors tu peux te déplacer derrière lui, et le manger.

> Sélectionner un pion : 
>  - Pour sélectionner un pion, tu peux tapper au choix, entre minuscule et majuscule : `c3` ou `C3`, te permettront de faire le même déplacement.
>  - Et pour le déplacer, tu dois saisir les coordonnées sous la même forme, le jeu te dira si tu peux faire le déplacement choisis ou non.

## Déroulement de la partie :

> Etape N°1 : 
>  - Lorsque vous verrez le message ci-dessous, vous devrez choisir entre jouer contre un ordinateur, ou jouer contre une autre personne (en local, sur le même PC). Il vous suffira de répondre par `Oui` ou `Non` (Vous pouvez répondre en anglais, ou juste mettre `y` ou `n`, le programme comprendra)
```shell
	            Veux tu jouer contre un ordinateur ?
                           (Oui / Non) :
```
> Etape N°2 : 
>  - Choisissez une grille, le jeu vous en propose 3 différentes : 
> > - Une grille classique de début de partie
> > - Une grille de milieu de partie, ou il manque quelque pion
> > - Enfin une grille de fin de partie ou il ne reste que très peu de pion
> - Pour choisir entre ces différentes grille, il vous faut saisir au clavier, `1`, `2`, `3`. Ou alors des mots simple comme `debut`, `milieu`, ou `fin`

````shell
                  Sur quelle grille veux tu jouer :

                           [1] : Grille N°1
                           [2] : Grille N°2
                           [3] : Grille N°3

                     Saisie ta réponse :
````

> Etape N°2 **BIS** : ***(NEW)***
> - Si vous avez demander à jouer contre une IA, le jeu vous demandera le niveau de difficulté auquel vous voulez jouer : 
````shell
                    Avec quel niveau de difficulté :

                           [1] : Difficulté 1
                           [2] : Difficulté 2

                        Saisie ta réponse :
````

> Etape 3 : 
> - Amusez vous bien ! ☻

> Etape 4 :
> - Félicitation pour votre victoire ! 
```py
	┌──────────────────────────────────┐
	│   Joueur 1 ● vous avez gagné !   │
	└──────────────────────────────────┘
```

## Lancement du Jeu:

> - Vous pouvez vous rendre sur le site de __[Repl.it](https://replit.com/@Swynnn/Acores#main.py)__ pour jouer au jeu, ou sinon, suivre les étapes qui suivent

> - Pensez à installer Python3 sur votre machine au préalable.
> - Si vous avez `make` d'installer, alors il vous suffit de lancer le makefile joint dans le code
> - Sinon, une fois avoir installer le jeu, il vous faut ouvrir un Terminal, et rentrer dans le dossier grâce à la commande `cd`.
> - Une fois dedans, éxécuter la commande `python3 main.py`, et le jeu se lancera de lui même. Amusez - vous bien ! 

## Bug Signaler :

- ~~Problème déplacement bizarre IA~~ (**Résolu**)
- ~~Problème affichage fin de partie~~ (**Résolu**)
- Problème déplacement IA (Parfois bloquée)
