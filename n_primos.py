#Exercício 1 - Primos
#Escreva a função n_primos que recebe como argumento um número inteiro maior
#ou igual a 2 como parâmetro e devolve a quantidade de números primos que
# existem entre 2 e n (incluindo 2 e, se for o caso, n).


def éPrimo(k):
    primo = True
    i = 2
    resto = 0
    while i < k and primo:
        resto = k % i  #Verifica se o número é primo pelo resto da divisao
        if resto == 0:
            primo = False
        i += 1
    return primo

def n_primos(n):
    quantidade = 0
    while n > 1:
        if éPrimo(n):
            quantidade += 1
            n -= 1
        else:
            n -= 1

    return quantidade
