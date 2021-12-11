#Exercício 2 - Desafio do vídeo "Repetição com while"
#Escreva um programa que receba um número inteiro na entrada e
#verifique se o número recebido possui ao menos um dígito com um dígito
# adjacente igual a ele. Caso exista, imprima "sim";
# se não existir, imprima "não".

numero = int(input("Digite um número inteiro: "))
digito = 0
digitorepetido = False
anterior = -10000
while numero != 0:
    digito = numero % 10
    numero = numero // 10
    if anterior == digito:
        digitorepetido = True
    anterior = digito
if digitorepetido:
    print("sim")
else:
    print("não")
