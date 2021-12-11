import re

def le_assinatura():
    #'''A funcao le os valores dos tracos linguisticos do modelo e devolve
    #uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    #'''A funcao le todos os textos a serem comparados e devolve
    #uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    #'''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    #'''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    #'''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    #'''Essa funcao recebe uma lista de palavras e devolve o numero de
    #palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    #'''Essa funcao recebe uma lista de palavras e devolve o numero de
    # palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    #Essa funcao recebe duas assinaturas de texto e
    #deve devolver o grau de similaridade nas assinaturas.'''
    subtracao = []
    somatorio = 0
    for x in range(len(as_a)):
        subtracao.append(abs(as_a[x] - as_b[x]))
    for x in subtracao:
        somatorio += x
    grau_similaridade = somatorio / 6

    return grau_similaridade

def calcula_assinatura(texto):
    #'''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a
    #assinatura do texto.'''
    lista_frases = []
    lista_palavras = []
    soma_tamanhos = 0
    soma_sentenca = 0
    soma_frases = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        lista_frases.extend(frases)
        soma_sentenca += len(sentenca)
    for frase in lista_frases:
        palavras = separa_palavras(frase)
        lista_palavras.extend(palavras)
        soma_frases += len(frase)
    for palavra in lista_palavras:
        soma_tamanhos += len(palavra)
    total_palavras = len(lista_palavras)
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    palavras_unicas = n_palavras_unicas(lista_palavras)
    wal_texto = soma_tamanhos / total_palavras #tamanho medio de palavra
    ttr_texto = palavras_diferentes / total_palavras #relação type token
    hlr_texto = palavras_unicas / total_palavras #razao Hapax Legomana
    sal_texto = soma_sentenca / len(sentencas) #tamanho medio de sentenca
    sac_texto = len(lista_frases) / len(sentencas) #complexidade de sentenca
    pal_texto = soma_frases / len(lista_frases) #tamanho medio frase

    return [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]

def avalia_textos(textos, ass_cp):
    #Essa funcao recebe uma lista de textos e
    #uma assinatura ass_cp e deve devolver o numero (1 a n) do texto
    #com maior probabilidade de ter sido infectado por COH-PIAH.'''
    as_b = []
    similaridade = 0
    lista_similaridades = []
    for texto in textos:
        as_b = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_cp, as_b)
        lista_similaridades.append(similaridade)
    infectado = lista_similaridades.index(min(lista_similaridades)) + 1
    return infectado

ass_cp = le_assinatura()
textos = le_textos()
aluno_infectado = avalia_textos(textos, ass_cp)
print("O autor do texto ", aluno_infectado, "está infectaco com COH-PIAH")
