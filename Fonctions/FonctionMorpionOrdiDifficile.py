def morpion_ordi_diffi():
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
                if a == b == c == d == e == f == g == h == i == "-":
                    choix_ordi_ai_debut = random.randint(1, 2)
                    if choix_ordi_ai_debut == 1:
                        e = "O"
                        tours_joueur = 0

                    else:
                        choix_ordi = random.randint(1, 4)
                        if choix_ordi == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi == 2:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi == 3:
                            g = "O"
                            tours_joueur = 0

                        elif choix_ordi == 4:
                            i = "O"
                            tours_joueur = 0

                else:
                    # a - b - c
                    if a == b == "O" and c == "-":
                        c = "O"
                        tours_joueur = 0

                    elif a == c == "O" and b == "-":
                        b = "O"
                        tours_joueur = 0

                    elif b == c == "O" and a == "-":
                        a = "O"
                        tours_joueur = 0

                    # d - e - f
                    elif d == e == "O" and f == "-":
                        f = "O"
                        tours_joueur = 0
                        print("porbl1")

                    elif d == f == "O" and e == "-":
                        e = "O"
                        tours_joueur = 0

                    elif f == e == "O" and d == "-":
                        d = "O"
                        tours_joueur = 0

                    # g - h - i
                    elif g == h == "O" and i == "-":
                        i = "O"
                        tours_joueur = 0

                    elif g == i == "O" and h == "-":
                        h = "O"
                        tours_joueur = 0

                    elif h == i == "O" and g == "-":
                        g = "O"
                        tours_joueur = 0

                    # a - d - g
                    elif a == d == "O" and g == "-":
                        g = "O"
                        tours_joueur = 0

                    elif a == g == "O" and d == "-":
                        d = "O"
                        tours_joueur = 0

                    elif d == g == "O" and a == "-":
                        a = "O"
                        tours_joueur = 0

                    # b - e - h
                    elif b == e == "O" and h == "-":
                        h = "O"
                        tours_joueur = 0

                    elif b == h == "O" and e == "-":
                        e = "O"
                        tours_joueur = 0

                    elif e == h == "O" and b == "-":
                        b = "O"
                        tours_joueur = 0

                    # c - f - i
                    elif c == f == "O" and i == "-":
                        i = "O"
                        tours_joueur = 0

                    elif c == i == "O" and f == "-":
                        f = "O"
                        tours_joueur = 0
                        print("porbl2")

                    elif f == i == "O" and c == "-":
                        c = "O"
                        tours_joueur = 0

                    # a - e - i
                    elif a == e == "O" and i == "-":
                        i = "O"
                        tours_joueur = 0

                    elif a == i == "O" and e == "-":
                        e = "O"
                        tours_joueur = 0

                    elif e == i == "O" and a == "-":
                        a = "O"
                        tours_joueur = 0

                    # c - e - g
                    elif c == e == "O" and g == "-":
                        g = "O"
                        tours_joueur = 0

                    elif c == g == "O" and e == "-":
                        e = "O"
                        tours_joueur = 0

                    elif e == g == "O" and c == "-":
                        c = "O"
                        tours_joueur = 0

                    # a - b - c
                    elif a == b != "-" and c == "-":
                        c = "O"
                        tours_joueur = 0

                    elif a == c != "-" and b == "-":
                        b = "O"
                        tours_joueur = 0

                    elif b == c != "-" and a == "-":
                        a = "O"
                        tours_joueur = 0

                    # d - e - f
                    elif d == e != "-" and f == "-":
                        f = "O"
                        tours_joueur = 0
                        print("porbl3")

                    elif d == f != "-" and e == "-":
                        e = "O"
                        tours_joueur = 0

                    elif f == e != "-" and d == "-":
                        d = "O"
                        tours_joueur = 0

                    # g - h - i
                    elif g == h != "-" and i == "-":
                        i = "O"
                        tours_joueur = 0

                    elif g == i != "-" and h == "-":
                        h = "O"
                        tours_joueur = 0

                    elif h == i != "-" and g == "-":
                        g = "O"
                        tours_joueur = 0

                    # a - d - g
                    elif a == d != "-" and g == "-":
                        g = "O"
                        tours_joueur = 0

                    elif a == g != "-" and d == "-":
                        d = "O"
                        tours_joueur = 0

                    elif d == g != "-" and a == "-":
                        a = "O"
                        tours_joueur = 0

                    # b - e - h
                    elif b == e != "-" and h == "-":
                        h = "O"
                        tours_joueur = 0

                    elif b == h != "-" and e == "-":
                        e = "O"
                        tours_joueur = 0

                    elif e == h != "-" and b == "-":
                        b = "O"
                        tours_joueur = 0

                    # c - f - i
                    elif c == f != "-" and i == "-":
                        i = "O"
                        tours_joueur = 0

                    elif c == i != "-" and f == "-":
                        f = "O"
                        tours_joueur = 0
                        print("porbl4")

                    elif f == i != "-" and c == "-":
                        c = "O"
                        tours_joueur = 0

                    # a - e - i
                    elif a == e != "-" and i == "-":
                        i = "O"
                        tours_joueur = 0

                    elif a == i != "-" and e == "-":
                        e = "O"
                        tours_joueur = 0

                    elif e == i != "-" and a == "-":
                        a = "O"
                        tours_joueur = 0

                    # c - e - g
                    elif c == e != "-" and g == "-":
                        g = "O"
                        tours_joueur = 0

                    elif c == g != "-" and e == "-":
                        e = "O"
                        tours_joueur = 0

                    elif e == g != "-" and c == "-":
                        c = "O"
                        tours_joueur = 0


                    elif a == c == g == i == d == f == h == "-" and e == "O" and b == "X":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0
                        else:
                            c = "O"
                            tours_joueur = 0

                    elif a == c == g == i == b == f == h == "-" and e == "O" and d == "X":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0
                        else:
                            g = "O"
                            tours_joueur = 0

                    elif a == c == g == i == d == b == h == "-" and e == "O" and f == "X":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0
                        else:
                            i = "O"
                            tours_joueur = 0

                    elif a == c == g == i == d == f == b == "-" and e == "O" and h == "X":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            g = "O"
                            tours_joueur = 0
                        else:
                            i = "O"
                            tours_joueur = 0

                    elif c == g == d == f == h == "-" and e == "O" and b == "X" and a == "O" and i == "X":
                        d = "O"
                        tours_joueur = 0

                    elif a == i == d == f == h == "-" and e == "O" and b == "X" and c == "O" and g == "X":
                        f = "O"
                        tours_joueur = 0
                        print("porbl5")

                    elif c == g == b == f == h == "-" and e == "O" and d == "X" and a == "O" and i == "X":
                        b = "O"
                        tours_joueur = 0

                    elif a == i == b == f == h == "-" and e == "O" and d == "X" and g == "O" and c == "X":
                        h = "O"
                        tours_joueur = 0

                    elif a == i == d == b == h == "-" and e == "O" and f == "X" and c == "O" and g == "X":
                        b = "O"
                        tours_joueur = 0

                    elif c == g == d == b == h == "-" and e == "O" and f == "X" and i == "O" and a == "X":
                        h = "O"
                        tours_joueur = 0

                    elif a == c == g == i == d == f == b == "-" and e == "O" and h == "X" and g == "O" and c == "X":
                        d = "O"
                        tours_joueur = 0

                    elif a == c == g == i == d == f == b == "-" and e == "O" and h == "X" and i == "O" and a == "X":
                        f = "O"
                        tours_joueur = 0
                        print("porbl6")

                    elif b == d == e == c == g == "-" and a == "O" and ((f == h and i == "X") or (f == i and h == "X") or (i == h and f == "X")):
                        choix_ordi_ai = random.randint(1 , 2)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0

                        else:
                            g = "O"
                            tours_joueur = 0

                    #and ((d == h and g == "X") or (d == g and h == "X") or (g == h and d == "X"))
                    elif b == f == e == a == i == "-" and c == "O":
                        choix_ordi_ai = random.randint(1 , 2)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        else:
                            i = "O"
                            tours_joueur = 0

                    #and ((b == c and f == "X") or (b == f and c == "X") or (c == f and b == "X"))
                    elif a == d == e == h == i == "-" and g == "O":
                        choix_ordi_ai = random.randint(1 , 2)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        else:
                            i = "O"
                            tours_joueur = 0

                    #and ((a == b and d == "X") or (a == d and b == "X") or (b == d and a == "X"))
                    elif c == e == f == g == h == "-" and i == "O":
                        choix_ordi_ai = random.randint(1 , 2)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0

                        else:
                            g = "O"
                            tours_joueur = 0

                    elif d == e == g == "-" and a == c == "O" and b == "X":
                        g = "O"
                        tours_joueur = 0

                    elif b == e == c == "-" and a == g == "O" and d == "X":
                        c = "O"
                        tours_joueur = 0

                    elif f == e == i == "-" and c == a == "O" and b == "X":
                        i = "O"
                        tours_joueur = 0

                    elif a == b == e == "-" and c == i == "O" and f == "X":
                        a = "O"
                        tours_joueur = 0

                    elif g == e == h == "-" and i == c == "O" and f == "X":
                        g = "O"
                        tours_joueur = 0

                    elif c == f == e == "-" and i == g == "O" and h == "X":
                        c = "O"
                        tours_joueur = 0

                    elif a == d == e == "-" and g == i == "O" and h == "X":
                        a = "O"
                        tours_joueur = 0

                    elif e == h == i == "-" and g == a == "O" and d == "X":
                        i = "O"
                        tours_joueur = 0

                    elif a == b == c == d == f == h == i == "-" and e == "X" and g == "O":
                        c = "O"
                        tours_joueur = 0

                    elif a == b == c == d == f == g == h == "-" and e == "X" and i == "O":
                        a = "O"
                        tours_joueur = 0

                    elif a == b == d == f == g == h == i == "-" and e == "X" and c == "O":
                        g = "O"
                        tours_joueur = 0

                    elif b == c == d == f == g == h == i == "-" and e == "X" and a == "O":
                        i = "O"
                        tours_joueur = 0

                    elif g == c == "O" and e == "X" and a == b == d == "-":
                        a = "O"
                        tours_joueur = 0

                    elif g == c == "O" and e == "X" and f == h == i == "-":
                        i = "O"
                        tours_joueur = 0

                    elif a == i == "O" and e == "X" and b == c == f == "-":
                        c = "O"
                        tours_joueur = 0

                    elif a == i == "O" and e == "X" and d == g == h == "-":
                        g = "O"
                        tours_joueur = 0

                    elif a == b == c == d == f == g == h == i == "-" and e == "X":
                        choix_ordi_ai = random.randint(1, 4)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3:
                            g = "X"
                            tours_joueur = 0

                        elif choix_ordi_ai == 4:
                            i = "O"
                            tours_joueur = 0

                    elif b == d == e == f == g == h == i == "-" and a == "X" and c == "O":
                        g = "O"
                        tours_joueur = 0

                    elif b == d == e == f == g == h == c == "-" and a == "X" and i == "O":
                        c = "O"
                        tours_joueur = 0

                    elif b == d == e == f == i == h == c == "-" and a == "X" and g == "O":
                        c = "O"
                        tours_joueur = 0

                    elif b == d == e == f == g == h == i == "-" and c == "X" and a == "O":
                        i = "O"
                        tours_joueur = 0

                    elif b == d == e == f == g == h == a == "-" and c == "X" and i == "O":
                        a = "O"
                        tours_joueur = 0

                    elif b == d == e == f == i == h == a == "-" and c == "X" and g == "O":
                        a = "O"
                        tours_joueur = 0

                    elif b == d == e == f == c == h == i == "-" and g == "X" and a == "O":
                        i = "O"
                        tours_joueur = 0

                    elif b == d == e == f == i == h == a == "-" and g == "X" and c == "O":
                        a = "O"
                        tours_joueur = 0

                    elif b == d == e == f == c == h == a == "-" and g == "X" and i == "O":
                        a = "O"
                        tours_joueur = 0

                    elif b == d == e == f == c == h == g == "-" and i == "X" and a == "O":
                        c = "O"
                        tours_joueur = 0

                    elif b == d == e == f == g == h == a == "-" and i == "X" and c == "O":
                        g = "O"
                        tours_joueur = 0

                    elif b == d == e == f == c == h == a == "-" and i == "X" and g == "O":
                        c = "O"
                        tours_joueur = 0

                    elif a == b == c == d == e == f == g == h == "-" and i == "X":
                        choix_ordi_ai = random.randint(1, 3)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3:
                            g = "O"
                            tours_joueur = 0

                    elif a == b == d == e == f == g == h == i == "-" and c == "X":
                        choix_ordi_ai = random.randint(1, 3)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            i = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3:
                            g = "O"
                            tours_joueur = 0

                    elif b == c == d == e == f == g == h == i == "-" and a == "X":
                        choix_ordi_ai = random.randint(1, 3)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            i = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3:
                            g = "O"
                            tours_joueur = 0

                    elif a == b == c == d == e == f == h == i == "-" and g == "X":
                        choix_ordi_ai = random.randint(1, 3)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            i = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3:
                            a = "O"
                            tours_joueur = 0

                    elif a == b == c == e == f ==i == "-":
                        choix_ordi_ai = random.randint(1, 3)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3:
                            i = "O"
                            tours_joueur = 0

                    elif a == b == c == d == e ==g == "-":
                        choix_ordi_ai = random.randint(1, 3)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3:
                            g = "O"
                            tours_joueur = 0

                    elif c == e == f == g == h == i == "-":
                        choix_ordi_ai = random.randint(1, 3)
                        if choix_ordi_ai == 1:
                            i = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3:
                            g = "O"
                            tours_joueur = 0

                    elif a == d == e == g == h == i == "-":
                        choix_ordi_ai = random.randint(1, 3)
                        if choix_ordi_ai == 1:
                            i = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3:
                            g = "O"
                            tours_joueur = 0

                    elif a == b == d == e == g == "-" and c == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            g = "O"
                            tours_joueur = 0

                    elif c == b == d == e == g == "-" and a == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            g = "O"
                            tours_joueur = 0

                    elif c == b == d == e == a == "-" and g == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            a = "O"
                            tours_joueur = 0

                    elif b == c == e == f == i == "-" and a == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            i = "O"
                            tours_joueur = 0

                    elif b == a == e == f == i == "-" and c == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            i = "O"
                            tours_joueur = 0

                    elif b == a == e == f == c == "-" and i == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            c = "O"
                            tours_joueur = 0

                    elif e == f == g == h == i == "-" and c == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            i = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            g = "O"
                            tours_joueur = 0

                    elif e == f == g == h == c == "-" and i == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            g = "O"
                            tours_joueur = 0

                    elif e == f == i == h == c == "-" and g == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            i = "O"
                            tours_joueur = 0

                    elif d == e == g == h == i == "-" and a == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            g = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            i = "O"
                            tours_joueur = 0

                    elif d == e == a == h == i == "-" and g == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            i = "O"
                            tours_joueur = 0

                    elif d == e == a == h == g == "-" and i == "O":
                        choix_ordi_ai = random.randint(1, 2)
                        if choix_ordi_ai == 1:
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2:
                            g = "O"
                            tours_joueur = 0

                    else:
                        choix_ordi_ai = random.randint(1, 9)
                        if choix_ordi_ai == 1 and a == "-":
                            a = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 2 and b == "-":
                            b = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 3 and c == "-":
                            c = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 4 and d == "-":
                            d = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 5 and e == "-":
                            e = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 6 and f == "-":
                            f = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 7 and g == "-":
                            g = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 8 and h == "-":
                            h = "O"
                            tours_joueur = 0

                        elif choix_ordi_ai == 9 and i == "-":
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
