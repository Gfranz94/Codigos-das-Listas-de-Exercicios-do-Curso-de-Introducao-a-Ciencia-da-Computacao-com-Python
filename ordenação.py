#Exercício 5 - Verificando ordenação
#Receba 3 números inteiros na entrada e imprima
#crescente
#se eles forem dados em ordem crescente. Caso contrário, imprima
#não está em ordem crescente

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a<b<c:
    print("crescente")
else:
    print("não está em ordem crescente")
