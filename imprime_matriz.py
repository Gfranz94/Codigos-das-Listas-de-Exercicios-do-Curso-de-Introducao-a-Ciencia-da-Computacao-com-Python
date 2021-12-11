#Exercício 1: Imprimindo matrizes
#Como proposto na primeira vídeo-aula da semana,
# escreva uma função imprime_matriz(matriz),
# que recebe uma matriz como parâmetro e imprime a matriz,
#linha por linha.
#Note que NÃO se deve imprimir espaços após o último elemento de cada linha!

def imprime_matriz(matriz):
    '''Esta função recebe uma matriz como parâmetro e
    imprime a matriz, linha por linha '''
    for m in matriz:
        for elemento in m:
            if elemento != m[-1]:
                print(elemento, end =" ")
            else:
                print(elemento, end="")
        print()
