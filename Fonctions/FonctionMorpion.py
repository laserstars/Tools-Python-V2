def morpion_2joueurs():
    a, b, c, d, e, f, g, h, i = "-", "-", "-", "-", "-", "-", "-", "-", "-"
    print(a, "\b", b, "\b", c)
    print(d, "\b", e, "\b", f)
    print(g, "\b", h, "\b", i)

    joueur1_gagne = 0
    joueur2_gagne = 0
    tours_joueur = 0
    jeu_morpion_fini = 0
    morpion_egalite =0

    while jeu_morpion_fini != 1:

        if tours_joueur == 0:
            while tours_joueur == 0:
                choix_joueur1 = input("Joueur 1 'X' choisi un chiffre entre 1 en 9\n")
                choix_joueur1_digit = choix_joueur1.isdigit()

                while choix_joueur1_digit == False:
                    choix_joueur1 = input("Joueur 1 'X' choisi un chiffre entre 1 en 9\n")
                    choix_joueur1_digit = choix_joueur1.isdigit()

                if choix_joueur1_digit == True:
                    choix_joueur1 = int(choix_joueur1)

                    if (choix_joueur1 > 9 or choix_joueur1 < 1):
                        print("\nOpération impossible, choisissé un bon chiffre.\n")
                    else:
                        if choix_joueur1 == 1:
                            if a == "-":
                                a = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 2:
                            if b == "-":
                                b = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 3:
                            if c == "-":
                                c = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 4:
                            if d == "-":
                                d = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 5:
                            if e == "-":
                                e = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 6:
                            if f == "-":
                                f = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 7:
                            if g == "-":
                                g = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 8:
                            if h == "-":
                                h = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 9:
                            if i == "-":
                                i = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")

        elif tours_joueur == 1:
            while tours_joueur == 1:
                choix_joueur2 = input("Joueur 2 'O' choisi un chiffre entre 1 en 9\n")
                choix_joueur2_digit = choix_joueur2.isdigit()

                while choix_joueur2_digit == False:
                    choix_joueur2 = input("Joueur 2 'O' choisi un chiffre entre 1 en 9\n")
                    choix_joueur2_digit = choix_joueur2.isdigit()

                if choix_joueur2_digit == True:
                    choix_joueur2 = int(choix_joueur2)

                    if (choix_joueur2 > 9 or choix_joueur2 < 1):
                        print("\nOpération impossible, choisissé un bon chiffre.\n")
                    else:
                        if choix_joueur2 == 1:
                            if a == "-":
                                a = "O"
                                tours_joueur = 0
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur2 == 2:
                            if b == "-":
                                b = "O"
                                tours_joueur = 0
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur2 == 3:
                            if c == "-":
                                c = "O"
                                tours_joueur = 0
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur2 == 4:
                            if d == "-":
                                d = "O"
                                tours_joueur = 0
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur2 == 5:
                            if e == "-":
                                e = "O"
                                tours_joueur = 0
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur2 == 6:
                            if f == "-":
                                f = "O"
                                tours_joueur = 0
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur2 == 7:
                            if g == "-":
                                g = "O"
                                tours_joueur = 0
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur2 == 8:
                            if h == "-":
                                h = "O"
                                tours_joueur = 0
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur2 == 9:
                            if i == "-":
                                i = "O"
                                tours_joueur = 0
                            else:
                                print("Cette zone est déja occupée.")

        morpion_egalite = morpion_egalite + 1

        if a == b == c:
            if a == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif a == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif d == e == f:
            if d == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif d == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif g == h == i:
            if h == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif h == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif a == d == g:
            if a == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif a == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif b == e == h:
            if e == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif e == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif c == f == i:
            if c == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif c == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif a == e == i:
            if a == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif a == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif c == e == g:
            if e == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif e == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif morpion_egalite == 9:
            jeu_morpion_fini = 1

        print("")
        print(a, "\b", b, "\b", c)
        print(d, "\b", e, "\b", f)
        print(g, "\b", h, "\b", i)





    if joueur1_gagne == 1:
        print("\nBravo, Joueur 1 à gagné!")
    elif joueur2_gagne == 1:
        print("\nBravo, Joueur 2 à gagné!")
    elif morpion_egalite == 9:
        print("\nDommage, il y a égalité!")


def morpion_ordi_facile():
    import  random

    a, b, c, d, e, f, g, h, i = "-", "-", "-", "-", "-", "-", "-", "-", "-"
    print(a, "\b", b, "\b", c)
    print(d, "\b", e, "\b", f)
    print(g, "\b", h, "\b", i)

    joueur1_gagne = 0
    joueur2_gagne = 0

    choix_tours = random.randint(1, 2)
    if choix_tours == 1:
        tours_joueur = 0
        print("\nC'est à toi de commencer.\n")
    elif choix_tours == 2:
        tours_joueur = 1
        print("\nC'est l'ordinateur qui va commencé.")

    jeu_morpion_fini = 0
    morpion_egalite =0

    while jeu_morpion_fini != 1:

        if tours_joueur == 0:
            while tours_joueur == 0:
                choix_joueur1 = input("Joueur 1 'X' choisi un chiffre entre 1 en 9\n")
                choix_joueur1_digit = choix_joueur1.isdigit()

                while choix_joueur1_digit == False:
                    choix_joueur1 = input("Joueur 1 'X' choisi un chiffre entre 1 en 9\n")
                    choix_joueur1_digit = choix_joueur1.isdigit()

                if choix_joueur1_digit == True:
                    choix_joueur1 = int(choix_joueur1)

                    if (choix_joueur1 > 9 or choix_joueur1 < 1):
                        print("\nOpération impossible, choisissé un bon chiffre.\n")
                    else:
                        if choix_joueur1 == 1:
                            if a == "-":
                                a = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 2:
                            if b == "-":
                                b = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 3:
                            if c == "-":
                                c = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 4:
                            if d == "-":
                                d = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 5:
                            if e == "-":
                                e = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 6:
                            if f == "-":
                                f = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 7:
                            if g == "-":
                                g = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 8:
                            if h == "-":
                                h = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")
                        elif choix_joueur1 == 9:
                            if i == "-":
                                i = "X"
                                tours_joueur = 1
                            else:
                                print("Cette zone est déja occupée.")

        elif tours_joueur == 1:
            while tours_joueur == 1:
                choix_ordi = random.randint(1,9)
                if choix_ordi == 1:
                    if a == "-":
                        a = "O"
                        tours_joueur = 0

                elif choix_ordi == 2:
                    if b == "-":
                        b = "O"
                        tours_joueur = 0

                elif choix_ordi == 3:
                    if c == "-":
                        c = "O"
                        tours_joueur = 0

                elif choix_ordi == 4:
                    if d == "-":
                        d = "O"
                        tours_joueur = 0

                elif choix_ordi == 5:
                    if e == "-":
                        e = "O"
                        tours_joueur = 0

                elif choix_ordi == 6:
                    if f == "-":
                        f = "O"
                        tours_joueur = 0

                elif choix_ordi == 7:
                    if g == "-":
                        g = "O"
                        tours_joueur = 0

                elif choix_ordi == 8:
                    if h == "-":
                        h = "O"
                        tours_joueur = 0

                elif choix_ordi == 9:
                    if i == "-":
                        i = "O"
                        tours_joueur = 0
            print("\nL'ordinateur a joué.")
        morpion_egalite = morpion_egalite + 1

        if a == b == c:
            if a == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif a == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif d == e == f:
            if d == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif d == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif g == h == i:
            if h == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif h == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif a == d == g:
            if a == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif a == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif b == e == h:
            if e == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif e == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif c == f == i:
            if c == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif c == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif a == e == i:
            if a == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif a == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif c == e == g:
            if e == "O":
                joueur2_gagne = 1
                jeu_morpion_fini = 1
            elif e == "X":
                joueur1_gagne = 1
                jeu_morpion_fini = 1

        elif morpion_egalite == 9:
            jeu_morpion_fini = 1

        print("")
        print(a, "\b", b, "\b", c)
        print(d, "\b", e, "\b", f)
        print(g, "\b", h, "\b", i)





    if joueur1_gagne == 1:
        print("\nBravo, tu as réussi à gagné!")
    elif joueur2_gagne == 1:
        print("\nDommage, l'ordinateur à gagné!")
    elif morpion_egalite == 9:
        print("\nDommage, il y a égalité!")
