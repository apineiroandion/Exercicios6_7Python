"""
Imprima os dous primeiros caracteres.
Imprima os tres últimos caracteres.
Imprima dita cadena cada dous caracteres. Ex.: recta debería imprimir rca
Dita cadea en sentido inverso. Ex.: Ola mundo! debe imprimir !odnum alO
Imprima a cadea nun sentido e en sentido inverso. Ex: reflexo imprime reflexooxelfer.
"""

cadea = "string de cousas"

def dous_primeiros(cadea):
    print(cadea[:2])

def tres_ultimos(cadea):
    print(cadea[-3:])

def cada_dous(cadea):
    print(cadea[::2])

def inverso(cadea):
    print(cadea[::-1])

def sentido_inverso(cadea):
    print(cadea + cadea[::-1])

if __name__ == '__main__':
    dous_primeiros(cadea)
    tres_ultimos(cadea)
    cada_dous(cadea)
    inverso(cadea)
    sentido_inverso(cadea)