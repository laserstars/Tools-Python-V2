def deci_bin(nombre_nombre_trans_DB):
    nombre_nombre_trans_DB = int(nombre_nombre_trans_DB)

    binaire = ""

    while nombre_nombre_trans_DB != 0 or len(binaire) % 4 != 0:

        reste_nombre_trans_DB = nombre_nombre_trans_DB % 2
        reste_nombre_trans_DB = str(reste_nombre_trans_DB)

        binaire = reste_nombre_trans_DB + binaire
        nombre_nombre_trans_DB = nombre_nombre_trans_DB // 2
    return binaire


def deci_hexa(nombre_trans_DH):
    nombre_trans_DH = int(nombre_trans_DH)

    hexadecimal = ""
    while nombre_trans_DH != 0:

        reste_nombre_trans_DH = nombre_trans_DH % 16

        if reste_nombre_trans_DH <= 9:
            reste_nombre_trans_DH = str(reste_nombre_trans_DH)
            hexadecimal = reste_nombre_trans_DH + hexadecimal
        else:
            if nombre_trans_DH % 16 == 10:
                hexadecimal = "A" + hexadecimal
            elif nombre_trans_DH % 16 == 11:
                hexadecimal = "B" + hexadecimal
            elif nombre_trans_DH % 16 == 12:
                hexadecimal = "C" + hexadecimal
            elif nombre_trans_DH % 16 == 13:
                hexadecimal = "D" + hexadecimal
            elif nombre_trans_DH % 16 == 14:
                hexadecimal = "E" + hexadecimal
            elif nombre_trans_DH % 16 == 15:
                hexadecimal = "F" + hexadecimal

        nombre_trans_DH = nombre_trans_DH // 16

    return hexadecimal


def bin_deci(nombre_debut_trans_BD):
    nombre_debut_trans_BD_len = len(nombre_debut_trans_BD)

    nombre_trans_BD_option = -1
    resultat_trans_BD = 0
    puissance_nombre_trans_BD = 0

    for j in range(nombre_debut_trans_BD_len):
        nombre_debut_choisi_option_BD = nombre_debut_trans_BD[nombre_trans_BD_option]
        nombre_debut_choisi_option_BD = int(nombre_debut_choisi_option_BD)

        resultat_trans_BD = resultat_trans_BD + nombre_debut_choisi_option_BD * (2 ** puissance_nombre_trans_BD)
        nombre_trans_BD_option = nombre_trans_BD_option - 1
        puissance_nombre_trans_BD = puissance_nombre_trans_BD + 1
    return resultat_trans_BD


def hexa_deci(nombre_debut_trans_HD):
    nombre_debut_trans_HD_len = len(nombre_debut_trans_HD)

    nombre_debut_trans_HD = nombre_debut_trans_HD.upper()

    nombre_trans_HD_option = -1
    resultat_trans_HD = 0
    puissance_nombre_trans_HD = 0

    for j in range(nombre_debut_trans_HD_len):

        nombre_debut_choisi_option_HD = nombre_debut_trans_HD[nombre_trans_HD_option]

        if nombre_debut_choisi_option_HD.isalpha() == True:
            nombre_debut_choisi_option_HD = nombre_debut_choisi_option_HD.upper()

        if nombre_debut_choisi_option_HD == 'A':
            nombre_debut_choisi_option_HD = 10
        elif nombre_debut_choisi_option_HD == 'B':
            nombre_debut_choisi_option_HD = 11
        elif nombre_debut_choisi_option_HD == 'C':
            nombre_debut_choisi_option_HD = 12
        elif nombre_debut_choisi_option_HD == 'D':
            nombre_debut_choisi_option_HD = 13
        elif nombre_debut_choisi_option_HD == 'E':
            nombre_debut_choisi_option_HD = 14
        elif nombre_debut_choisi_option_HD == 'F':
            nombre_debut_choisi_option_HD = 15

        nombre_debut_choisi_option_HD = int(nombre_debut_choisi_option_HD)

        resultat_trans_HD = resultat_trans_HD + nombre_debut_choisi_option_HD * (16 ** puissance_nombre_trans_HD)
        nombre_trans_HD_option = nombre_trans_HD_option - 1
        puissance_nombre_trans_HD = puissance_nombre_trans_HD + 1

    return resultat_trans_HD


def bin_hexa(nombre_debut_trans_BD):
    nombre_debut_trans_BD_len = len(nombre_debut_trans_BD)

    nombre_trans_BD_option = -1
    resultat_trans_BD = 0
    puissance_nombre_trans_BD = 0

    for j in range(nombre_debut_trans_BD_len):
        nombre_debut_choisi_option_BD = nombre_debut_trans_BD[nombre_trans_BD_option]
        nombre_debut_choisi_option_BD = int(nombre_debut_choisi_option_BD)

        resultat_trans_BD = resultat_trans_BD + nombre_debut_choisi_option_BD * (2 ** puissance_nombre_trans_BD)
        nombre_trans_BD_option = nombre_trans_BD_option - 1
        puissance_nombre_trans_BD = puissance_nombre_trans_BD + 1

    nombre_trans_DH = resultat_trans_BD

    hexadecimal = ""
    while nombre_trans_DH != 0:

        if nombre_trans_DH % 16 == 0:
            hexadecimal = "0" + hexadecimal
        elif nombre_trans_DH % 16 == 1:
            hexadecimal = "1" + hexadecimal
        elif nombre_trans_DH % 16 == 2:
            hexadecimal = "2" + hexadecimal
        elif nombre_trans_DH % 16 == 3:
            hexadecimal = "3" + hexadecimal
        elif nombre_trans_DH % 16 == 4:
            hexadecimal = "4" + hexadecimal
        elif nombre_trans_DH % 16 == 5:
            hexadecimal = "5" + hexadecimal
        elif nombre_trans_DH % 16 == 6:
            hexadecimal = "6" + hexadecimal
        elif nombre_trans_DH % 16 == 7:
            hexadecimal = "7" + hexadecimal
        elif nombre_trans_DH % 16 == 8:
            hexadecimal = "8" + hexadecimal
        elif nombre_trans_DH % 16 == 9:
            hexadecimal = "9" + hexadecimal
        elif nombre_trans_DH % 16 == 10:
            hexadecimal = "A" + hexadecimal
        elif nombre_trans_DH % 16 == 11:
            hexadecimal = "B" + hexadecimal
        elif nombre_trans_DH % 16 == 12:
            hexadecimal = "C" + hexadecimal
        elif nombre_trans_DH % 16 == 13:
            hexadecimal = "D" + hexadecimal
        elif nombre_trans_DH % 16 == 14:
            hexadecimal = "E" + hexadecimal
        elif nombre_trans_DH % 16 == 15:
            hexadecimal = "F" + hexadecimal

        nombre_trans_DH = nombre_trans_DH // 16

        return hexadecimal


def hexa_bin(nombre_debut_trans_HD):
    nombre_debut_trans_HD_len = len(nombre_debut_trans_HD)

    nombre_debut_trans_HD = nombre_debut_trans_HD.upper()

    nombre_trans_HD_option = -1
    resultat_trans_HD = 0
    puissance_nombre_trans_HD = 0

    for j in range(nombre_debut_trans_HD_len):

        nombre_debut_choisi_option_HD = nombre_debut_trans_HD[nombre_trans_HD_option]

        if nombre_debut_choisi_option_HD.isalpha() == True:
            nombre_debut_choisi_option_HD = nombre_debut_choisi_option_HD.upper()

        if nombre_debut_choisi_option_HD == 'A':
            nombre_debut_choisi_option_HD = 10
        elif nombre_debut_choisi_option_HD == 'B':
            nombre_debut_choisi_option_HD = 11
        elif nombre_debut_choisi_option_HD == 'C':
            nombre_debut_choisi_option_HD = 12
        elif nombre_debut_choisi_option_HD == 'D':
            nombre_debut_choisi_option_HD = 13
        elif nombre_debut_choisi_option_HD == 'E':
            nombre_debut_choisi_option_HD = 14
        elif nombre_debut_choisi_option_HD == 'F':
            nombre_debut_choisi_option_HD = 15

        nombre_debut_choisi_option_HD = int(nombre_debut_choisi_option_HD)

        resultat_trans_HD = resultat_trans_HD + nombre_debut_choisi_option_HD * (16 ** puissance_nombre_trans_HD)
        nombre_trans_HD_option = nombre_trans_HD_option - 1
        puissance_nombre_trans_HD = puissance_nombre_trans_HD + 1

    nombre_nombre_trans_DB = resultat_trans_HD

    binaire = ""

    while nombre_nombre_trans_DB != 0 or len(binaire) % 4 != 0:

        if nombre_nombre_trans_DB % 2 == 0:
            binaire = '0' + binaire

        elif nombre_nombre_trans_DB % 2 == 1:
            binaire = '1' + binaire
        nombre_nombre_trans_DB = nombre_nombre_trans_DB // 2
    return binaire