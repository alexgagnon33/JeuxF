#                              Characters 
#                      PC                      NPC
#         Speed «- Strenght «- Mentalist      Enemy
#                                              Boss

##Characters : Monstre allié et enemie
## PC : Monstre Speed Todag (Attaque en premier, petite attaque, mais plusieurs attaques), Monstre Strenght Tgohs (Lent mais fort plus 
## PC suite : résistant, attaque physique et buff) Monstre Mental Togrs (débuff et stun %?)
## Enemy : Mélange de tout, seulement monstre et type.
## Boss : Immunité contre type qui perd/attaque

### Characters class : PC et NPC 
'charcater'
'character_1 (Mental)'
'character_2 (Strenght)'
'chracter_3 (Speed)'
### PC class : Speed Strenght Mentalist = Vie, Dommage 'PEUT MIX LES DEUX???'
'Mental      Strenght       Speed'
'Vie            Vie             Vie'
'Dommage         dOMAMGE         Dommage'
'Armure          Armure          Armure'
'Vitesse        Vitesse          Vitesse'
### Speed : Attaque (dommage et desciption) Strenght : Attaque et buff () Mentalist (Debuff)
'Attaque Mental (dgt, dommage, armure)       Attaque Speed (dgt, dommage, armure)       Attaque strenght (dgt, dommage, armure)'
'AttaqueM_1 (10, 0, 0) bon contre strenght   AttaqueM_1 (10, 0, 0) bon contre strenght  AttaqueM_1 (10, 0, 0) bon contre strenght'
'AttaqueM_2 (10, 0, 0) bon contre speed      AttaqueM_2 (10, 0, 0) bon contre speed     AttaqueM_2 (10, 0, 0) bon contre speed'
'AttaqueM_3 (0, 20, 0)                       AttaqueM_3 (0, 20, 0)                      AttaqueM_3 (0, 20, 0)'
'AttaqueM-4 (10, 0, 0) Bn contre Mental      AttaqueM-4 (10, 0, 0) Bn contre Mental     AttaqueM-4 (10, 0, 0) Bn contre Menta'
### Enemy class : Réutiliser les classe des PC  et type
'PC class, Attaque Mental/Attaque Speed/ Attaque Strenght'

#### 1) Menu jeux (Start, Choisir type et exit (Peut-être guide??)) 2)Menu Choisir type (montre attaque et confirmation du choix avec
#### possibilité de retour) 3) Menu Guide (Explication des monstres et origines?) 4) Exit quitter tout 5) Start jeux ---» Début histoire
#### 20 secondes lettre par lettre a la undertale (avec musique???) 6) Début premier combat (donc il faut le bon PC, les stats du PC, 
#### les attaques du monstre AVEC TYPE, enemy aléatoire, stats enemy, attaque enemy, choix de tour (stats speed), attaque en premier et 
#### 2ième tour jusqu'à mort du monstre) 7) Choix de regagner de la vie (Attendre 5-10sec à l'utilisateur MUSIQUE??) 8) 2ième combat
#### 9) Boss : Immunité contre type qui perd/attaque

#SI J'AI LE TEMPS FAIRE MODE ALÉATOIRE ET EXPERT