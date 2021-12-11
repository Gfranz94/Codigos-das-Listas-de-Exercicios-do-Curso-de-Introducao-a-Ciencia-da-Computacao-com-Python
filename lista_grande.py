#Exercício 1: Gerando listas grandes
#Escreva a função lista_grande(n), que recebe como parâmetro
#um número inteiro n e devolve uma lista contendo n números inteiros aleatórios.
from random import randint
def lista_grande(n):
    lista_aleatória = []
    for i in range(n):
        lista_aleatória += [randint(-5*n,5*n)]
    return lista_aleatória
