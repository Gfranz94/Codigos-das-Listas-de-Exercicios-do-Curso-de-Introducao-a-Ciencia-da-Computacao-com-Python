#Exercício 2 - Primos
#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2
#como parâmetro e devolve o maior número primo menor ou igual ao
#número passado à função

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

def maior_primo(n):
    while n >= 2:
        éPrimo(n)
        if éPrimo(n):
            return n
        n -= 1
