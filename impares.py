#Exercício 2
#Receba um número inteiro positivo na entrada e imprima os n
#primeiros números ímpares naturais.

n = int(input("Digite o valor de n: "))
i = 1 #definindo o contador
impar = 1
while i <= n:
    impar = 2*impar - 1
    print(impar)
    i += 1 #incremento ao contador
    impar = i #fazendo o impar na forma n em 2*n - 1
