#Exercício 2: Soma de matrizes
#Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes
#e devolve uma matriz que represente sua soma caso as matrizes
#tenham dimensões iguais. Caso contrário, a função deve devolver False.

def dimensoes(matriz):
    linha = len(matriz)
    coluna = 0
    for i in matriz:
        for j in i:
            coluna += 1
    coluna = coluna // linha
    return [linha, coluna]


def soma_matrizes(m1, m2):
    soma = []
    matriz_soma = []
    dimensao_m1 = dimensoes(m1)
    dimensao_m2 = dimensoes(m2)
    if dimensao_m1 != dimensao_m2:
        return False
    else:
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                soma.append(m1[i][j] + m2[i][j])
            matriz_soma += [soma[:]] 
            soma = []
        return matriz_soma
