def nombre_perdu ():
    from random import randint
    fin_jeu_nombre_perdu = 1

    while fin_jeu_nombre_perdu == 1:
        nombre_perdu_option = input("\nL'intervalle est de 0 à combien ?\n")

        nombre_perdu_option_digit = nombre_perdu_option.isdigit()

        if nombre_perdu_option_digit == True:
            nombre_perdu_option = int(nombre_perdu_option)

        while nombre_perdu_option_digit == False or nombre_perdu_option < 1:

            print("\nOpération impossible\n")

            nombre_perdu_option = input("\nL'intervalle est de 0 à combien ?\n")
            nombre_perdu_option_digit = nombre_perdu_option.isdigit()

            if nombre_perdu_option_digit == True:
                nombre_perdu_option = int(nombre_perdu_option)

        if nombre_perdu_option_digit == True:
            nombre_perdu_option = int(nombre_perdu_option)

        nombre_perdu = randint(0, nombre_perdu_option)
        fin_partie_nombre_p = 1

        nombre_essai_nombre_p = 1
        nombre_joueur_nombre_p = input("\nA ton avis c'est quelle nombre ? Taper Fin pour arreter le jeu.\n")

        nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

        if nombre_joueur_nombre_p_digit == True:
            nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

        # elif nombre_joueur_nombre_p == 'Fin' or nombre_joueur_nombre_p == 'fin' or nombre_joueur_nombre_p == 'FIN' or nombre_joueur_nombre_p == 'F' or nombre_joueur_nombre_p == 'f':
        # fin_partie_nombre_p = 0
        # else:
        while (nombre_joueur_nombre_p_digit == False or nombre_joueur_nombre_p < 0) and (
                nombre_joueur_nombre_p != 'Fin' and nombre_joueur_nombre_p != 'fin' and nombre_joueur_nombre_p != 'FIN' and nombre_joueur_nombre_p != 'F' and nombre_joueur_nombre_p != 'f'):

            print("\nOpération impossible\n")

            nombre_joueur_nombre_p = input("\nA ton avis c'est quelle nombre ? Taper Fin pour arreter le jeu.\n")
            nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

            if nombre_joueur_nombre_p_digit == True:
                nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

        if nombre_joueur_nombre_p_digit == True:
            nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)
        elif nombre_joueur_nombre_p == 'Fin' or nombre_joueur_nombre_p == 'fin' or nombre_joueur_nombre_p == 'FIN' or nombre_joueur_nombre_p == 'F' or nombre_joueur_nombre_p == 'f':
            fin_partie_nombre_p = 0

        while fin_partie_nombre_p == 1:

            if nombre_perdu < nombre_joueur_nombre_p:

                print("\nLe chiffre à trouver est plus petit que ", nombre_joueur_nombre_p,
                      "\n")
                nombre_joueur_nombre_p = input("A ton avis c'est quelle nombre ?\n")

                nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                if nombre_joueur_nombre_p_digit == True:
                    nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                while nombre_joueur_nombre_p_digit == False or nombre_joueur_nombre_p < 0:

                    print("\nOpération impossible\n")

                    nombre_joueur_nombre_p = input("\nA ton avis c'est quelle nombre ?\n")
                    nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                    if nombre_joueur_nombre_p_digit == True:
                        nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                if nombre_joueur_nombre_p_digit == True:
                    nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                nombre_essai_nombre_p = nombre_essai_nombre_p + 1

            elif (nombre_perdu > nombre_joueur_nombre_p and nombre_joueur_nombre_p >= 0):

                print("\nLe chiffre à trouver est plus grand que ", nombre_joueur_nombre_p,
                      "\n")
                nombre_joueur_nombre_p = input("A ton avis c'est quelle nombre ?\n")

                nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                if nombre_joueur_nombre_p_digit == True:
                    nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                while nombre_joueur_nombre_p_digit == False or nombre_joueur_nombre_p < 0:

                    print("\nOpération impossible\n")

                    nombre_joueur_nombre_p = input("\nA ton avis c'est quelle nombre ?\n")
                    nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                    if nombre_joueur_nombre_p_digit == True:
                        nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                if nombre_joueur_nombre_p_digit == True:
                    nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                nombre_essai_nombre_p = nombre_essai_nombre_p + 1

            elif nombre_perdu == nombre_joueur_nombre_p:
                fin_partie_nombre_p = 0

        if nombre_joueur_nombre_p == nombre_perdu:
            print("\nBravo, tu as trouvé le nombre en ", nombre_essai_nombre_p, "essais.")

        print("\n0 -- Retour Menu Jeux")
        print("1 -- Rejouer")

        menu_fin_jeu_nombre_perdu = input("")

        menu_fin_jeu_nombre_perdu_digit = menu_fin_jeu_nombre_perdu.isdigit()

        if menu_fin_jeu_nombre_perdu_digit == True:
            menu_fin_jeu_nombre_perdu = int(menu_fin_jeu_nombre_perdu)

        while menu_fin_jeu_nombre_perdu_digit == False or menu_fin_jeu_nombre_perdu < 0 or menu_fin_jeu_nombre_perdu > 1:

            print("\nOpération impossible\n")

            print("0 -- Retour Menu Jeux")
            print("1-- Rejouer\n")

            menu_fin_jeu_nombre_perdu = input("Que faire ?\n")
            menu_fin_jeu_nombre_perdu_digit = menu_fin_jeu_nombre_perdu.isdigit()

            if menu_fin_jeu_nombre_perdu_digit == True:
                menu_fin_jeu_nombre_perdu = int(menu_fin_jeu_nombre_perdu)

        if menu_fin_jeu_nombre_perdu_digit == True:
            menu_fin_jeu_nombre_perdu = int(menu_fin_jeu_nombre_perdu)

        if menu_fin_jeu_nombre_perdu == 0:
            fin_jeu_nombre_perdu = 0
        elif menu_fin_jeu_nombre_perdu == 1:
            fin_jeu_nombre_perdu = 1

        print("")