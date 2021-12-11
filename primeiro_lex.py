#Exercício 2: Ordem lexicográfica
#Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista)
#que recebe uma lista de strings como parâmetro e devolve o primeiro string
#na ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

def primeiro_lex(lista_de_strings):
    primeiro_lex_string = []
    for string in lista_de_strings:
        primeiro_lex_string += [ord(string[0])]
    menor_string = lista_de_strings[primeiro_lex_string.index(min(primeiro_lex_string))]
    return menor_string
