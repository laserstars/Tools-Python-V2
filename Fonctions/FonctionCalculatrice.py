def calculatrice ():
    fin_calculatrice = 1
    while fin_calculatrice == 1:

        continuer = True

        while continuer == True:
            choix_chiffre1_calculatrice = input("Choisis ton premier nombre ")
            try:
                choix_chiffre1_calculatrice = int(choix_chiffre1_calculatrice)
                continuer = False

            except:
                print("\nCeci n'est pas un chiffre/nombre.\n")
                continue

            print("")

            print("0 -- Multiplier par ... ")
            print("1 -- Diviser par ... ")
            print("2 -- Additionner par ... ")
            print("3 -- Soustraire par ... ")

            print("")

            operation_calculatrice = input("Choisir une opération ")

            operation_calculatrice_digit = operation_calculatrice.isdigit()

            if operation_calculatrice_digit == True:
                operation_calculatrice = int(operation_calculatrice)

            while operation_calculatrice_digit == False or operation_calculatrice < 0 or operation_calculatrice > 3:

                print("\nOpération impossible\n")
                print("0 -- Multiplier par ... ")
                print("1 -- Diviser par ... ")
                print("2 -- Additionner par ... ")
                print("3 -- Soustraire par ... ")
                operation_calculatrice = input("\nChoisir une opération\n")
                operation_calculatrice_digit = operation_calculatrice.isdigit()

                if operation_calculatrice_digit == True:
                    operation_calculatrice = int(operation_calculatrice)

            if operation_calculatrice_digit == True:
                operation_calculatrice = int(operation_calculatrice)

                print("")

                continuer = True

                while continuer == True:
                    choix_chiffre2_calculatrice = input("Choisis ton deuxième nombre ")
                    try:
                        choix_chiffre2_calculatrice = int(choix_chiffre2_calculatrice)
                        continuer = False

                    except:
                        print("\nCeci n'est pas un chiffre/nombre.\n")
                        continue

                print("")

                if operation_calculatrice == 0:
                    multiplication_calculatrice = choix_chiffre1_calculatrice * choix_chiffre2_calculatrice
                    print("Le résultat est ", multiplication_calculatrice)

                elif operation_calculatrice == 1:
                    if choix_chiffre2_calculatrice == 0:
                        print("Division par zéro impossible !")
                    else:
                        division_calculatrice = choix_chiffre1_calculatrice / choix_chiffre2_calculatrice
                        print("Le résultat est ", division_calculatrice)

                elif operation_calculatrice == 2:
                    addition_calculatrice = choix_chiffre1_calculatrice + choix_chiffre2_calculatrice
                    print("Le résultat est ", addition_calculatrice)

                elif operation_calculatrice == 3:
                    soustration_calculatrice = choix_chiffre1_calculatrice - choix_chiffre2_calculatrice
                    print("Le résultat est ", soustration_calculatrice)

                print("")

                print("0 -- Retour au Menu")
                print("1 -- Nouvelle opération")

                print("")

                print("Que faire ?")

                menu_fin_calculatrice = input("")

                menu_fin_calculatrice_digit = menu_fin_calculatrice.isdigit()

                if menu_fin_calculatrice_digit == True:
                    menu_fin_calculatrice = int(menu_fin_calculatrice)

                while menu_fin_calculatrice_digit == False or menu_fin_calculatrice < 0 or menu_fin_calculatrice > 1:

                    print("\nOpération impossible\n")

                    print("0 -- Retour au Menu")
                    print("1 -- Nouvelle opération\n")

                    menu_fin_calculatrice = input("Que faire ?\n")
                    menu_fin_calculatrice_digit = menu_fin_calculatrice.isdigit()

                    if menu_fin_calculatrice_digit == True:
                        menu_fin_calculatrice = int(menu_fin_calculatrice)

                if menu_fin_calculatrice_digit == True:
                    menu_fin_calculatrice = int(menu_fin_calculatrice)

                if menu_fin_calculatrice == 0:
                    fin_calculatrice = 0
                elif menu_fin_calculatrice == 1:
                    fin_calculatrice = 1

                print("")