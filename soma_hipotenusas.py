#Exercício 2 - (Difícil) Soma das hipotenusas
#Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe
#um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número.
#Em outras palavras, nnn é uma hipotenusa se existem números inteiros iii e jjj
# tais que:
#
#n2=i2+j2 n^2 = i^2 + j^2 n2=i2+j2
#
#Escreva uma função soma_hipotenusas que receba como parâmetro
#um número inteiro positivo n n n e devolva a soma de todos os inteiros
#entre 1 e n n n que são comprimento da hipotenusa de algum triângulo
#retângulo com catetos inteiros.
#
#DIca1: um mesmo número pode ser hipotenusa de vários triângulos,
#mas deve ser somado apenas uma vez. Uma boa solução para este exercício é
#fazer um laço de 1 até n n n testando se o número é hipotenusa de algum
#triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar
#certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras
#encontradas.
#
#Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o
#comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

def é_hipotenusa(x):
    b = 1 #catetomenor
    a = 2
    hip = False
    while a*a + b*b != x*x and not hip and b < a:
        a = 2 #catetomaior
        while a*a + b*b != x*x and a < x:
                a += 1
        if a*a + b*b == x*x:
            hip = True
        else:
            hip = False
            b += 1

    return hip

def soma_hipotenusas(n):
    soma = 0
    while n > 0:
        if é_hipotenusa(n):
            soma = soma + n
        n -= 1
    return soma
