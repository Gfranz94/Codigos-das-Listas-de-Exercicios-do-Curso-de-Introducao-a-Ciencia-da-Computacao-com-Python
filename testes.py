# Testes da lista de exercícios 2

'''
#exercício 1
def maiusculas(frase):
    maiusculas = ""
    for letra in frase:
        if ord(letra) < 91 and ord(letra) > 64:
            maiusculas += letra
    return maiusculas

#testes automatizados exercício 1

def teste_maiusculas1():
    assert  maiusculas('Programamos em python 2?') == 'P'
def teste_maiusculas2():
    assert  maiusculas('Programamos em Python 3.') == 'PP'
def teste_maiusculas3():
    assert  maiusculas('PrOgRaMaMoS em python!') == 'PORMMS'
def teste_maiusculas4():
    assert  maiusculas('EU AMO A NATASHA') == 'EUAMOANATASHA'
def teste_maiusculas5():
    assert  maiusculas('TestandO esPaçaMento e PontuaCao.,;/?owiedjf') == 'TOPMPC'

#exercício 2

def menor_nome(lista_de_nomes):
    nomes_arrumados = []
    for nome in lista_de_nomes:
        nome = nome.strip().lower().capitalize()
        nomes_arrumados += [nome]
    nomes_arrumados.sort(key = len)
    return nomes_arrumados[0]

def teste_menor_nome1():
    assert menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == "José"

def teste_menor_nome2():
    assert menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == "José"

def teste_menor_nome3():
    assert menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == "José"

def teste_menor_nome4():
    assert menor_nome(['Bárbara', '    isa', 'JOSÉ  ', 'Bill']) == "Isa"

def teste_menor_nome5():
    assert menor_nome(['joélio', 'gabi     ', 'joao   ', '    NATASHA', 'Arleteee', 'Neném']) == "Gabi"


#exercicio adicional 1
def conta_letras(frase, contar="vogais"):
    frase = frase.lower().strip()
    num_vogais = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u')
    num_consoantes = len(frase) - num_vogais - frase.count(' ')
    if contar == 'vogais':
        return num_vogais
    if contar == 'consoantes':
        return num_consoantes

def test_conta_letras1():
    assert conta_letras('programamos em python') == 6

def test_conta_letras2():
    assert conta_letras('programamos em python', 'vogais') == 6

def test_conta_letras3():
    assert conta_letras('programamos em python', 'consoantes') == 13

def test_conta_letras4():
    assert conta_letras('que nome estranho', 'consoantes') == 8

def test_conta_letras4():
    assert conta_letras('te amo nenem') == 5

'''
def primeiro_lex(lista_de_strings):
    primeiro_lex_string = []
    for string in lista_de_strings:
        primeiro_lex_string += [ord(string[0])]
    menor_string = lista_de_strings[primeiro_lex_string.index(min(primeiro_lex_string))]
    return menor_string


def testa_primeiro_lex():
    assert primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA'
def testa_primeiro_lex2():
    assert primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A'
def testa_primeiro_lex3():
    assert primeiro_lex(['A', ')', 'pull mee under']) == ')'
