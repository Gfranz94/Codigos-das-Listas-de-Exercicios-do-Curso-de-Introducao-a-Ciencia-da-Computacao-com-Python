#Exercício 1: Ordenação com insertion sort
#Implemente a função insertion_sort(lista),
#que recebe uma lista com números inteiros como parâmetro e
#devolve esta lista ordenada. Utilize o algoritmo insertion sort.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        elemento_movendo = lista[i]
        j = i
        while j > 0 and lista[j - 1] > elemento_movendo:
            lista[j] = lista[j - 1]
            j -= 1
        lista[j] = elemento_movendo
    return lista
        
