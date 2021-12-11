#Exercício 3 - Vogais
#Escreva a função vogal que recebe um único caractere como parâmetro
#e devolve True se ele for uma vogal e False se for uma consoante.

def vogal(n):
    if n == "a" or n == "e" or n == "i" or n == "o" or n == "u" or n == "A" or n == "E" or n == "I" or n == "O" or n == "U":
        x = True
    else:
        x = False
    return x
