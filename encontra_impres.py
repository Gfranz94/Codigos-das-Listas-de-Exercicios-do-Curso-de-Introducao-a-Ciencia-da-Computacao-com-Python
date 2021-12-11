#Exercício 2: Encontrando ímpares em uma lista
#Implemente a função encontra_impares(lista),
#que recebe como parâmetro uma lista de números inteiros e
#devolve uma outra lista apenas com os números ímpares da lista dada.
#Sua solução deve ser implementada utilizando recursão.
#Dica: você vai precisar do método extend() que as listas possuem.

def encontra_impares(lista):
    lista_impares = []
    if len(lista) == 1:
        if lista[0] % 2 != 0:
            return lista[:1]
        else:
            return lista[:0]
    else:
        if lista[0] % 2 != 0:
            lista_impares = lista[:1]
        lista = lista[1:]
        return lista_impares + encontra_impares(lista)



                                 
    
        
        


    
