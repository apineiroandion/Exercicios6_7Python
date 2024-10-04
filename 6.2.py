"""
Escribir funcións que dada unha cadea e un caracter:
Inserte o caracter entre cada letra da cadea. Ex: separar, debería devoltar s,e,p,a,r,a,r
Reemplace tódolos espacios polo caracter. Ex: meu arquivo de texto.txt e ‘\_’ debería devoltar meu\_arquivo\_de\_texto.txt
Reemplace tódolos díxitos na cadea polo caracter. Ex: Súa clave é: 1540 e ‘X’, debería devoltar Súa clave é: XXXX
Inserte o caracter cada 3 díxitos na cadea. Ex. 2552552550 e ‘.’ debería devoltar 255.255.255.0
"""
from pydoc import replace

saparar = "separar"

def separar(cadea, caracter):
    print(caracter.join(cadea))

separar(saparar, ",")

arquivo = "meu arquivo de texto.txt"
def reemplazar_espacios(cadea, caracter):
    print(cadea.replace(" ", caracter))

reemplazar_espacios(arquivo, "/")

clave = "Súa clave é: 1540"
def reemplazar_digitos(cadea, caracter):
    print(cadea.replace("1", caracter).replace("2", caracter).replace("3", caracter).replace("4", caracter).replace("5", caracter).replace("6", caracter).replace("7", caracter).replace("8", caracter).replace("9", caracter).replace("0", caracter))

reemplazar_digitos(clave, "X")

ip = "2552552550"
def concatenar_cada_tres(cadea, caracter):
    print(caracter.join([cadea[i:i+3] for i in range(0, len(cadea), 3)]))

concatenar_cada_tres(ip, ".")
