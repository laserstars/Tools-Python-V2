def pierre_feuille_ciseaux ():
    from random import randint
    fin_jeu_PSF = 1

    while fin_jeu_PSF == 1:
        option_jeu = ['pierre', 'feuille', 'ciseaux']
        chiffre_option_jeu = randint(0, 2)
        choix_ordi = option_jeu[chiffre_option_jeu]

        choix_joueur = input("\npierre, feuille, ciseaux. Taper Fin pour quitter.\n")

        if (
                choix_joueur == 'pierre' or choix_joueur == 'Pierre' or choix_joueur == 'PIERRE' or choix_joueur == 'P' or choix_joueur == 'p'):

            choix_joueur = 'pierre'
            print('\nVous : ', choix_joueur, ' VS ', choix_ordi, ' : Ordinateur\n')

        elif (
                choix_joueur == 'feuille' or choix_joueur == 'Feuille' or choix_joueur == 'FEUILLE' or choix_joueur == 'F' or choix_joueur == 'f'):

            choix_joueur = 'feuille'
            print('\nVous : ', choix_joueur, ' VS ', choix_ordi, ' : Ordinateur\n')

        elif (
                choix_joueur == 'ciseaux' or choix_joueur == 'Ciseaux' or choix_joueur == 'CISEAUX' or choix_joueur == 'C' or choix_joueur == 'c' or choix_joueur == 'ciseau' or choix_joueur == 'Ciseau' or choix_joueur == 'CISEAU'):

            choix_joueur = 'ciseaux'
            print('\nVous : ', choix_joueur, ' VS ', choix_ordi, ' : Ordinateur\n')

        if choix_joueur == choix_ordi:
            print('Egalité!')

        elif choix_joueur == 'pierre':
            if choix_ordi == 'feuille':
                print('Perdu! La feuille recouvre la pierre')
            else:
                print('Gagné! La pierre écrase les ciseaux')
        elif choix_joueur == 'feuille':
            if choix_ordi == 'pierre':
                print('Gagné! La feuille recouvre la pierre.')
            else:
                print('Perdu! Les ciseaux coupent la feuille.')
        elif choix_joueur == 'ciseaux':
            if choix_ordi == 'feuille':
                print('Gagné! Les ciseaux coupent la feuille.')
            else:
                print('Perdu! Les ciseaux se font écraser par la pierre.')

        elif (choix_joueur == 'fin' or choix_joueur == 'Fin' or choix_joueur == 'FIN'):
            fin_jeu_PSF = 0

        else:
            print('\nOpération impossible.')

        menu_fin_jeu_PSF = input('\n0 -- Choix jeux\n1-- Rejouer\n')

        menu_fin_jeu_PSF_digit = menu_fin_jeu_PSF.isdigit()

        if menu_fin_jeu_PSF_digit == True:
            menu_fin_jeu_PSF = int(menu_fin_jeu_PSF)

        while menu_fin_jeu_PSF_digit == False or menu_fin_jeu_PSF < 0 or menu_fin_jeu_PSF > 1:

            print("\nOpération impossible\n")

            print("0 -- Choix jeux")
            print("1-- Rejouer\n")

            menu_fin_jeu_PSF = input("Que faire ?\n")
            menu_fin_jeu_PSF_digit = menu_fin_jeu_PSF.isdigit()

            if menu_fin_jeu_PSF_digit == True:
                menu_fin_jeu_PSF = int(menu_fin_jeu_PSF)

        if menu_fin_jeu_PSF_digit == True:
            menu_fin_jeu_PSF = int(menu_fin_jeu_PSF)

        if menu_fin_jeu_PSF == 0:
            fin_jeu_PSF = 0
        elif menu_fin_jeu_PSF == 1:
            fin_jeu_PSF = 1

        print("")