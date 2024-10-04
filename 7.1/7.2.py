"""
Exercicio 7.1. Escribir unha función que reciba unha tupla de elementos e indique si se encontran ordenados de menor a maior ou non.
Exercicio 7.2. Dominó.
Escribir unha función que indique si duas fichas de dominó encaixan ou non. As fichas recíbense en duas tuplas, por exemplo: (3,4) y (5,4).
Escribir unha función que indique si duas fichas de dominó encaixan ou non. As fichas recíbense nunha cadea, por exemplo: 3-4 2-5. Nota: utilizar a función split dlas cadeas.

"""
tuplaOrdeada = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuplaDesordeada = (1, 2, 3, 4, 5, 6, 7, 8, 10, 9)

def ordenados(tupla):
    if tupla == tuple(sorted(tupla)):
        print("Están ordenados de menor a maior")
    else:
        print("Non están ordenados de menor a maior")

ordenados(tuplaOrdeada)
ordenados(tuplaDesordeada)

def domino(tupla1, tupla2):
    if tupla1[0] == tupla2[0] or tupla1[0] == tupla2[1] or tupla1[1] == tupla2[0] or tupla1[1] == tupla2[1]:
        print("Encaixan")
    else:
        print("Non encaixan")

domino((3, 4), (5, 4))
domino((3, 4), (2, 5))

def dominoCadea(cadea):
    fichas = cadea.split(" ")
    if fichas[0][0] == fichas[1][0] or fichas[0][0] == fichas[1][2] or fichas[0][2] == fichas[1][0] or fichas[0][2] == fichas[1][2]:
        print("Encaixan")
    else:
        print("Non encaixan")

dominoCadea("3-4 5-4")
dominoCadea("3-4 2-5")