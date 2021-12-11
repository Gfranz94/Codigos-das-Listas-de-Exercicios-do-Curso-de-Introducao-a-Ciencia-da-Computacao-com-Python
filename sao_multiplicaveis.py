#Exercício 2: Matrizes multiplicáveis
#Duas matrizes são multiplicáveis se o número de colunas da
# primeira é igual ao número de linhas da segunda.
#Escreva a função sao_multiplicaveis(m1, m2)
#que recebe duas matrizes como parâmetro e devolve True
#se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário.

def sao_multiplicaveis(m1, m2):
    '''recebe duas matrizes como parâmetro e devolve True
    se as matrizes forem multiplicavéis (na ordem dada)
    e False caso contrário. '''
    numero_colunas = 0
    for linha in m1:
        for coluna in linha:
            numero_colunas += 1
    numero_linhas = len(m2)
    numero_colunas = numero_colunas // len(m1)
    if numero_colunas == numero_linhas:
        return True
    else:
        return False
