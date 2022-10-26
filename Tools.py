#2.1.2

from Fonctions.FonctionPierreFC import*
from Fonctions.FonctionNombrePerdu import*
from Fonctions.FonctionTranscodage import*
from Fonctions.FonctionCalculatrice import*
from Fonctions.FonctionGenPassword import*
from Fonctions.FonctionMorpion import*
from Fonctions.FonctionMorpionOrdiMoyen import*
from Fonctions.FonctionMorpionOrdiDifficile import*

Menu = 1

while Menu == 1:

    print("\n0 -- Quitter")
    print("1 -- Générateur de mot de passe")
    print("2 -- Jeux")
    print("3 -- Calculatrice")
    print("4 -- Transcodage")

    option = input("")

    option_digit = option.isdigit()

    while option_digit == False:
        print("\nOpération impossible, choisissé un bon chiffre.\n")
        print("\n0 -- Quitter")
        print("1 -- Générateur de mot de passe")
        print("2 -- Jeux")
        print("3 -- Calculatrice")
        print("4 -- Transcodage")

        option = input("")
        option_digit = option.isdigit()

    if option_digit == True:
        option = int(option)

        if (option > 4 or option < 0):
            print("\nOpération impossible, choisissé un bon chiffre.\n")
        elif option == 0:
            Menu = 0
        else:
            fin_calculatrice = 1
            fin_password = 1
            fin_jeu = 1
            fin_transcodage = 1

            print("")

            if option == 3:
                calculatrice()

            elif option == 1:
                gen_password()

            elif option == 2:
                while fin_jeu == 1:
                    print("0 -- Retour Menu")
                    print("1 -- Pierre, Feuille, Ciseaux")
                    print("2 -- Trouver le Nombre perdu")
                    print("3 -- Morpion 2 Joueurs")
                    print("4 -- Morpion VS Ordinateur Facile")
                    print("5 -- Morpion VS Ordinateur Moyen")
                    print("6 -- Morpion VS Ordinateur Difficile\n")

                    option_jeu = input("Que faire ?\n")

                    option_jeu_digit = option_jeu.isdigit()

                    if option_jeu_digit == True:
                        option_jeu = int(option_jeu)

                    while option_jeu_digit == False or option_jeu < 0 or option_jeu > 6:

                        print("\nOpération impossible\n")
                        print("0 -- Retour Menu")
                        print("1 -- Pierre, Feuille, Ciseaux")
                        print("2 -- Trouver le Nombre perdu")
                        print("3 -- Morpion 2 Joueurs")
                        print("4 -- Morpion VS Ordinateur Facile")
                        print("5 -- Morpion VS Ordinateur Moyen")
                        print("6 -- Morpion VS Ordinateur Difficile\n")

                        option_jeu = input("Que faire ?\n")

                        option_jeu_digit = option_jeu.isdigit()

                        if option_jeu_digit == True:
                            option_jeu = int(option_jeu)

                    if option_jeu_digit == True:
                        option_jeu = int(option_jeu)

                    if option_jeu == 0:
                        fin_jeu = 0

                    if (option > 6 or option < 0):
                        print("\nOpération impossible, choisissé un bon chiffre.\n")
                    else:
                        if option_jeu == 1:
                            pierre_feuille_ciseaux()
                        elif option_jeu == 2:
                            nombre_perdu()
                        elif option_jeu == 3:
                            morpion_2joueurs()
                        elif option_jeu == 4:
                            morpion_ordi_facile()
                        elif option_jeu == 5:
                            morpion_ordi_moyen()
                        elif option_jeu == 6:
                            morpion_ordi_diffi()

            elif option == 4:
                Menu_transcodage = 1

                while Menu_transcodage == 1:

                    print("0 -- Quitter")
                    print("1 -- Transcodage Décimal --> Binaire")
                    print("2 -- Transcodage Décimal --> Hexadécimal")
                    print("3 -- Transcodage Binaire --> Décimal")
                    print("4 -- Transcodage Hexadécimal --> Décimal")
                    print("5 -- Transcodage Hexadécimal --> Binaire")
                    print("6 -- Transcodage Binaire --> Hexadécimal")

                    option_transcodage = input("\nChoisi une option.\n")

                    option_transcodage_digit = option_transcodage.isdigit()

                    while option_transcodage_digit == False:
                        print("\n0 -- Quitter")
                        print("1 -- Transcodage Décimal --> Binaire")
                        print("2 -- Transcodage Décimal --> Hexadécimal")
                        print("3 -- Transcodage Binaire --> Décimal")
                        print("4 -- Transcodage Hexadécimal --> Décimal")
                        print("5 -- Transcodage Hexadécimal --> Binaire")
                        print("6 -- Transcodage Binaire --> Hexadécimal")

                        option_transcodage = input("\nChoisi une option.\n")

                        option_transcodage_digit = option_transcodage.isdigit()

                    if option_transcodage_digit == True:
                        option_transcodage = int(option_transcodage)

                        if (option_transcodage > 6 or option_transcodage < 0):
                            print("\nOpération impossible, choisissé un bon chiffre.\n")
                        elif option_transcodage == 0:
                            Menu_transcodage = 0

                    if option_transcodage == 1:

                        continuer = True

                        while continuer == True:
                            chiffre_demande_DB = input("\nChoisi un chiffre à transcoder en Binaire.\n")
                            try:
                                chiffre_demande_DB = int(chiffre_demande_DB)
                                if chiffre_demande_DB < 0:
                                    print("\nIl faut un chiffre ou nombre plus grand que 0")
                                else:
                                    continuer = False

                            except:
                                print("\nCeci n'est pas un chiffre ou nombre.\n")
                                continue

                        print("\nLe chiffre", chiffre_demande_DB, "en Décimal, vaut", deci_bin(chiffre_demande_DB),
                              "en Binaire.\n")

                    elif option_transcodage == 2:

                        continuer = True

                        while continuer == True:
                            chiffre_demande_DH = input("Choisi un chiffre à transcoder en Hexadécimal.\n")
                            try:
                                chiffre_demande_DH = int(chiffre_demande_DH)
                                if chiffre_demande_DH < 0:
                                    print("\nIl faut un chiffre ou nombre plus grand que 0")
                                else:
                                    continuer = False

                            except:
                                print("\nCeci n'est pas un chiffre ou nombre.\n")
                                continue

                        print("\nLe chiffre", chiffre_demande_DH, "en Décimal, vaut", deci_hexa(chiffre_demande_DH),
                              "en Hexadécimal.\n")

                    elif option_transcodage == 3:

                        continuer_trans_BD = 1
                        while continuer_trans_BD == 1:

                            chiffre_demande_BD = input("Choisi un chiffre en Binaire à transcoder en Décimal.\n")
                            option_caractere = 0
                            continuer_trans_BD_erreur1 = 0
                            continuer_trans_BD_erreur2 = 0

                            for i in range(len(chiffre_demande_BD)):
                                if chiffre_demande_BD[option_caractere] != "0" and chiffre_demande_BD[option_caractere] != "1":
                                    continuer_trans_BD_erreur1 = 1

                                elif chiffre_demande_BD[option_caractere] == "0" or chiffre_demande_BD[option_caractere] == "1":
                                    continuer_trans_BD_erreur2 = 1
                                option_caractere = option_caractere + 1
                            if continuer_trans_BD_erreur1 == 0 and continuer_trans_BD_erreur2 == 1:
                                continuer_trans_BD = 0
                            else:
                                print("\nEn Binaire il n'y a que des 1 et des 0.\n")

                        print("\nLe chiffre", chiffre_demande_BD, "en Binaire, vaut", bin_deci(chiffre_demande_BD),
                              "en Décimal.\n")

                    elif option_transcodage == 4:

                        continuer_trans_HD = 1
                        while continuer_trans_HD == 1:

                            chiffre_demande_HD = input("Choisi un chiffre en Hexadécimal à transcoder en Décimal.\n")
                            chiffre_demande_HD = chiffre_demande_HD.upper()
                            option_caractere = 0
                            continuer_trans_HD_erreur1 = 0
                            continuer_trans_HD_erreur2 = 0

                            for i in range(len(chiffre_demande_HD)):
                                if chiffre_demande_HD[option_caractere] != "0" and chiffre_demande_HD[option_caractere] != "1" and chiffre_demande_HD[option_caractere] != "2" and chiffre_demande_HD[option_caractere] != "3" and chiffre_demande_HD[option_caractere] != "4" and chiffre_demande_HD[option_caractere] != "5" and chiffre_demande_HD[option_caractere] != "6" and chiffre_demande_HD[option_caractere] != "7" and chiffre_demande_HD[option_caractere] != "8" and chiffre_demande_HD[option_caractere] != "9" and chiffre_demande_HD[option_caractere] != "A" and chiffre_demande_HD[option_caractere] != "B" and chiffre_demande_HD[option_caractere] != "C" and chiffre_demande_HD[option_caractere] != "D" and chiffre_demande_HD[option_caractere] != "E" and chiffre_demande_HD[option_caractere] != "F":
                                    continuer_trans_HD_erreur1 = 1

                                elif chiffre_demande_HD[option_caractere] == "0" or chiffre_demande_HD[option_caractere] == "1" or chiffre_demande_HD[option_caractere] == "2" or chiffre_demande_HD[option_caractere] == "3" or chiffre_demande_HD[option_caractere] == "4" or chiffre_demande_HD[option_caractere] == "5" or chiffre_demande_HD[option_caractere] == "6" or chiffre_demande_HD[option_caractere] == "7" or chiffre_demande_HD[option_caractere] == "8" or chiffre_demande_HD[option_caractere] == "9" or chiffre_demande_HD[option_caractere] == "A" or chiffre_demande_HD[option_caractere] == "B" or chiffre_demande_HD[option_caractere] == "C" or chiffre_demande_HD[option_caractere] == "D" or chiffre_demande_HD[option_caractere] == "E" or chiffre_demande_HD[option_caractere] == "F":

                                    continuer_trans_HD_erreur2 = 1
                                option_caractere = option_caractere + 1
                            if continuer_trans_HD_erreur1 == 0 and continuer_trans_HD_erreur2 == 1:
                                continuer_trans_HD = 0
                            else:
                                print("\nEn Hexadécimal il n'y a que les chiffres positifs et les lettres jusqu'à 'F' qui fonctionnes.\n")

                        print("\nLe chiffre", chiffre_demande_HD, "en Hexadécimal, vaut", hexa_deci(chiffre_demande_HD),
                              "en Décimal.\n")

                    elif option_transcodage == 5:

                        continuer_trans_HB = 1
                        while continuer_trans_HB == 1:

                            chiffre_demande_HB = input("Choisi un chiffre en Hexadécimal à transcoder en Binaire.\n")
                            chiffre_demande_HB = chiffre_demande_HB.upper()
                            option_caractere = 0
                            continuer_trans_HB_erreur1 = 0
                            continuer_trans_HB_erreur2 = 0

                            for i in range(len(chiffre_demande_HB)):
                                if chiffre_demande_HB[option_caractere] != "0" and chiffre_demande_HB[
                                    option_caractere] != "1" and chiffre_demande_HB[option_caractere] != "2" and \
                                        chiffre_demande_HB[option_caractere] != "3" and chiffre_demande_HB[
                                    option_caractere] != "4" and chiffre_demande_HB[option_caractere] != "5" and \
                                        chiffre_demande_HB[option_caractere] != "6" and chiffre_demande_HB[
                                    option_caractere] != "7" and chiffre_demande_HB[option_caractere] != "8" and \
                                        chiffre_demande_HB[option_caractere] != "9" and chiffre_demande_HB[
                                    option_caractere] != "A" and chiffre_demande_HB[option_caractere] != "B" and \
                                        chiffre_demande_HB[option_caractere] != "C" and chiffre_demande_HB[
                                    option_caractere] != "D" and chiffre_demande_HB[option_caractere] != "E" and \
                                        chiffre_demande_HB[option_caractere] != "F":
                                    continuer_trans_HB_erreur1 = 1

                                elif chiffre_demande_HB[option_caractere] == "0" or chiffre_demande_HB[
                                    option_caractere] == "1" or chiffre_demande_HB[option_caractere] == "2" or \
                                        chiffre_demande_HB[option_caractere] == "3" or chiffre_demande_HB[
                                    option_caractere] == "4" or chiffre_demande_HB[option_caractere] == "5" or \
                                        chiffre_demande_HB[option_caractere] == "6" or chiffre_demande_HB[
                                    option_caractere] == "7" or chiffre_demande_HB[option_caractere] == "8" or \
                                        chiffre_demande_HB[option_caractere] == "9" or chiffre_demande_HB[
                                    option_caractere] == "A" or chiffre_demande_HB[option_caractere] == "B" or \
                                        chiffre_demande_HB[option_caractere] == "C" or chiffre_demande_HB[
                                    option_caractere] == "D" or chiffre_demande_HB[option_caractere] == "E" or \
                                        chiffre_demande_HB[option_caractere] == "F":

                                    continuer_trans_HB_erreur2 = 1
                                option_caractere = option_caractere + 1
                            if continuer_trans_HB_erreur1 == 0 and continuer_trans_HB_erreur2 == 1:
                                continuer_trans_HB = 0
                            else:
                                print(
                                    "\nEn Hexadécimal il n'y a que les chiffres positifs et les lettres jusqu'à 'F' qui fonctionnes.\n")

                        print("\nLe chiffre", chiffre_demande_HB, "en Hexadécimal, vaut", hexa_bin(chiffre_demande_HB),
                              "en Binaire.\n")

                    elif option_transcodage == 6:

                        continuer_trans_BH = 1
                        while continuer_trans_BH == 1:

                            chiffre_demande_BH = input("Choisi un chiffre en Binaire à transcoder en Hexadécimal.\n")
                            option_caractere = 0
                            continuer_trans_BH_erreur1 = 0
                            continuer_trans_BH_erreur2 = 0

                            for i in range(len(chiffre_demande_BH)):
                                if chiffre_demande_BH[option_caractere] != "0" and chiffre_demande_BH[
                                    option_caractere] != "1":
                                    continuer_trans_BH_erreur1 = 1

                                elif chiffre_demande_BH[option_caractere] == "0" or chiffre_demande_BH[
                                    option_caractere] == "1":
                                    continuer_trans_BH_erreur2 = 1
                                option_caractere = option_caractere + 1
                            if continuer_trans_BH_erreur1 == 0 and continuer_trans_BH_erreur2 == 1:
                                continuer_trans_BH = 0
                            else:
                                print("\nEn Binaire il n'y a que des 1 et des 0.\n")

                        print("\nLe chiffre", chiffre_demande_BH, "en Binaire, vaut", bin_hexa(chiffre_demande_BH),
                              "en Hexadécimal.\n")