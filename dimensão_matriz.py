#Exercício 1: Tamanho da matriz
#Escreva uma função dimensoes(matriz) que recebe uma matriz
#como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.

def dimensoes(matriz):
    linha = len(matriz)
    coluna = 0
    for i in matriz:
        for j in i:
            coluna += 1
    coluna = coluna // linha
    print (str(linha) + "X" + str(coluna))
