import random

Joueur = input("Jouer(0), pas jouer(1)")
if Joueur == "0" :
    listmot == "WHISKY", "JAZZEZ", "JOCKEY", "BOMBYX", "KAZAKH", "COCCYX", "JOYEUX", "JOYAUX", "ZAWIYA", "JOJOBA", "JINGXI", "TOTORO", "ATOUT"
    random = radom.randrange(0, len(listemot)-1)
    mot = listemot[random].replace("")
    motlist = []
    motmystere = ""
    nberreur = 0
    victoire = False
    lettrelist = []
    odre = len(motj[i])

    for i in range(len(mot)) :
        if mot[i] != ' ' :
            motlist.append('*')
        else :
            motlist.append('')
    for j in range (len(mot)) :
        motmystere = motmystere + motlist[j]
        print(motmystere)
    while (nberreur > 6 and victoire == False) :
        motJ = input("Enter Mot")
        erreur = True
        for i in range(len(mot)) :
            if mot[i] == motJ :
                motlist[i] == motJ
                erreur = False
        if ordre != listmot
            erreur == true
            nberreur = nberreur + 1
            print("C'est non")
            lettrelist.append(motj + 'R')
        else :
            lettrelist.append(motj + 'J')
        for l in range(len(lettreList)) :
            if lettreList[l][1] == 'V' :
                print(Fore.RED + lettreList[l][0], end='')
            else :
                print(Fore.Blue + lettreList[l][0], end='')
        print(Fore.RESET)

    if victoire == False :
        print("perdu")
        
elif joueur =="1" :
    print("Vous avez appuyé ici par curiosité, c'est ça ? Passer une bonne journée")