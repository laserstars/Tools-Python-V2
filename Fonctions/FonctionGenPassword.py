def gen_password():
    import random

    fin_password = 1
    while fin_password == 1:
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number_password = "0123456789"
        symbols_password = "\/#@%&*$"

        Use_for = lower_case + upper_case + number_password + symbols_password
        lenght_for_pass = input("Quelle taille pour le mot de passe ? ")

        lenght_for_pass_digit = lenght_for_pass.isdigit()

        if lenght_for_pass_digit == True:
            lenght_for_pass = int(lenght_for_pass)

        while lenght_for_pass_digit == False or lenght_for_pass < 1:

            print("\nOpération impossible\n")

            lenght_for_pass = input("\nQuelle taille pour le mot de passe ?\n")
            lenght_for_pass_digit = lenght_for_pass.isdigit()

            if lenght_for_pass_digit == True:
                lenght_for_pass = int(lenght_for_pass)

        if lenght_for_pass_digit == True:
            lenght_for_pass = int(lenght_for_pass)

        print("")

        password = "".join(random.sample(Use_for, lenght_for_pass))
        print("Le nouveau mot de passe est " + password)

        print("")

        print("0 -- Retour au Menu")
        print("1 -- Nouveau mot de passe")

        print("")

        print("Que faire ?")

        menu_fin_password = input("")

        menu_fin_password_digit = menu_fin_password.isdigit()

        if menu_fin_password_digit == True:
            menu_fin_password = int(menu_fin_password)

        while menu_fin_password_digit == False or menu_fin_password < 0 or menu_fin_password > 1:

            print("\nOpération impossible\n")

            print("0 -- Retour au Menu")
            print("1 -- Nouveau mot de passe\n")

            menu_fin_password = input("Que faire ?\n")
            menu_fin_password_digit = menu_fin_password.isdigit()

            if menu_fin_password_digit == True:
                menu_fin_password = int(menu_fin_password)

        if menu_fin_password_digit == True:
            menu_fin_password = int(menu_fin_password)

        if menu_fin_password == 0:
            fin_password = 0
        elif menu_fin_password == 1:
            fin_password = 1

        print("")