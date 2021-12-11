#Exercício 1: Letras maiúsculas
#Escreva a função maiusculas(frase) que recebe uma frase (uma string)
#como parâmetro e devolve uma string com as letras maiúsculas que existem
#nesta frase, na ordem em que elas aparecem.

def maiusculas(frase):
    ''' Esta função recebe uma frase (uma string) como parâmetro
    e devolve uma string com as letras maiúsculas que existem
    nesta frase, na ordem em que elas aparecem.'''
    maiusculas = ""
    for letra in frase:
        if ord(letra) < 91 and ord(letra) > 64:
            maiusculas += letra
    return maiusculas
