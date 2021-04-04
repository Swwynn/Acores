# Acores Project

## But du jeu :
Le principe du jeu, est de manger tout les pions adverses, afin qu'il ne reste plus qu'un joueur sur le plateau de jeu.

## Règles du jeu :

> Types de déplacements :
> - **Simple** : Tu peux déplacer un pion, d'une seule case, dans la direction de ton choix, du moment que la case est vide.
> - **Saut** : Tu peux "manger" un pion ennemi, pour cela, si il y a un pion enemi autour de toi, et que derrière ce pion, ce trouve une case vide, alors tu peux te déplacer derrière lui, et le manger.

> Sélectionner un pion : 
>  - Pour sélectionner un pion, tu peux tapper au choix, entre minuscule et majuscule : `c3` ou `C3`, te permettrons de faire le même déplacement.
>  - Et pour le déplacer, tu dois saisir les coordonnées sous la même forme, le jeu te dira si tu peux faire le déplacement choisis ou non.

## Déroulement de la partie :

> Etape N°1 : 
>  - Lorsque vous verrez le message ci-dessous, vous devrez choisir entre jouer contre un ordinateur, ou jouer contre une autre personne (en local, sur le même PC). Il vous suffira de répondre par `Oui` ou `Non` (Vous pouvez répondre en anglais, ou juste mettre `y` ou `n`, le programme comprendra)
```py
	Veux tu jouer contre un ordinateur ?
	(Oui / Non) :
```
> Etape N°2 : 
>  - Dans la mesure du possible, il vous faut gagner !! 

> Etape Finale : 
> - Félicitation pour votre victoire ! 
```py
	┌──────────────────────────────────┐
	│   Joueur 1 ● vous avez gagné !   │
	└──────────────────────────────────┘
```

## Lancement du Jeu:

> - Pensez à installer Python3 sur votre machine au préalable.
> - Si vous avez `make` d'installer, alors il vous suffit de lancer le makefile joint dans le code
> - Sinon, une fois avoir installer le jeu, il vous faut ouvrir un Terminal, et rentrer dans le dossier grâce à la commande `cd`.
> - Une fois dedans, éxécuter la commande `python3 main.py`, et le jeu se lancera de lui même. Amusez - vous bien ! 

## Bug Signaler :

- ~~Problème déplacement bizarre IA~~ (**Résolu**)
- ~~Problème affichage fin de partie~~ (**Résolu**)
- Problème déplacement IA (Parfois bloquée)
